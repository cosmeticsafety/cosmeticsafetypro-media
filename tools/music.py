"""Original, royalty-free background music for reels.

Generates a soft, upbeat "corporate/lifestyle" loop (pad chords, plucked
arpeggio, light kick + hat) procedurally, so there are no copyright issues.
Each seed gives a different key / tempo / progression, so every day's reel
sounds a little different.

    python3 tools/music.py in.mp4 out.mp4 [seed]
"""
import sys, subprocess, json, hashlib
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

SR = 44100
PROGS = [  # scale degrees (semitones from root) for 4-bar progressions
    [[0, 4, 7, 11], [9, 12, 16, 19], [5, 9, 12, 16], [7, 11, 14, 17]],   # I - vi - IV - V (maj7 colour)
    [[0, 4, 7, 14], [7, 11, 14, 19], [9, 12, 16, 21], [5, 9, 12, 16]],   # I - V - vi - IV
    [[9, 12, 16, 19], [5, 9, 12, 16], [0, 4, 7, 11], [7, 11, 14, 17]],   # vi - IV - I - V
    [[0, 4, 7, 11], [5, 9, 12, 16], [2, 5, 9, 12], [7, 11, 14, 17]],     # I - IV - ii - V
]

def hz(midi): return 440.0 * 2 ** ((midi - 69) / 12)

def env(n, a, r):
    e = np.ones(n); a = min(a, n); r = min(r, n - a)
    if a: e[:a] = np.linspace(0, 1, a)
    if r: e[-r:] = np.linspace(1, 0, r)
    return e

def lowpass(x, cut):
    b, a = butter(2, cut / (SR / 2)); return lfilter(b, a, x)

def make(duration, seed=0):
    rng = np.random.default_rng(seed)
    root = 48 + int(rng.integers(0, 8))            # C3..G3
    bpm = float(rng.choice([96, 100, 104, 108, 112]))
    prog = PROGS[int(rng.integers(0, len(PROGS)))]
    beat = 60 / bpm; bar = 4 * beat
    n = int(duration * SR); t = np.arange(n) / SR
    out = np.zeros(n)

    # pads: detuned triangles per chord, one chord per bar
    for b in range(int(np.ceil(duration / bar))):
        chord = prog[b % 4]; s = int(b * bar * SR); e = min(n, int((b + 1) * bar * SR))
        if s >= n: break
        seg = np.arange(e - s) / SR; tone = np.zeros(e - s)
        for k, iv in enumerate(chord):
            for det in (-0.12, 0.12):
                f = hz(root + 12 + iv + det)
                tone += (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * f * seg)) * (0.9 if k else 1.0)
        out[s:e] += 0.035 * lowpass(tone, 1800) * env(e - s, int(.25 * SR), int(.3 * SR))
        # bass on beats 1 and 3
        for bb in (0, 2):
            bs = s + int(bb * beat * SR); be = min(n, bs + int(beat * 1.6 * SR))
            if bs >= n: continue
            seg2 = np.arange(be - bs) / SR
            out[bs:be] += 0.11 * np.sin(2 * np.pi * hz(root - 12 + chord[0]) * seg2) * np.exp(-seg2 * 2.2)

    # plucked arpeggio, 8th notes
    step = beat / 2; i = 0
    while i * step < duration:
        b = int(i * step // bar); chord = prog[b % 4]
        note = root + 24 + chord[[0, 1, 2, 3, 2, 1, 2, 3][i % 8]]
        s = int(i * step * SR); e = min(n, s + int(0.45 * SR)); seg = np.arange(e - s) / SR
        pl = (np.sin(2 * np.pi * hz(note) * seg) + 0.3 * np.sin(4 * np.pi * hz(note) * seg)) * np.exp(-seg * 7)
        out[s:e] += 0.05 * pl; i += 1

    # drums: soft kick on beats, hat on off-beats (start after 1 bar for a gentle intro)
    k = 0
    while k * beat < duration:
        s = int(k * beat * SR)
        if k * beat >= bar:
            e = min(n, s + int(.25 * SR)); seg = np.arange(e - s) / SR
            f = 110 * np.exp(-seg * 18) + 45
            out[s:e] += 0.22 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-seg * 14)
            hs = s + int(beat / 2 * SR); he = min(n, hs + int(.05 * SR))
            if hs < n:
                noise = rng.standard_normal(he - hs)
                out[hs:he] += 0.025 * (noise - lowpass(noise, 6000)) * np.linspace(1, 0, he - hs)
        k += 1

    # master: fade in/out, normalise to about -16 dBFS RMS
    fade_in, fade_out = int(.6 * SR), int(1.4 * SR)
    out[:fade_in] *= np.linspace(0, 1, fade_in); out[-fade_out:] *= np.linspace(1, 0, fade_out)
    out = np.tanh(out * 1.4)
    rms = np.sqrt(np.mean(out ** 2)) or 1
    out *= 0.158 / rms
    out = np.clip(out, -0.95, 0.95)
    stereo = np.stack([out, np.roll(out, 90)], axis=1)
    return (stereo * 32767).astype(np.int16)

def duration_of(path):
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", path],
                       capture_output=True, text=True, check=True)
    return float(json.loads(p.stdout)["format"]["duration"])

def add_music(src, dst, seed=None):
    if seed is None:
        seed = int(hashlib.md5(src.encode()).hexdigest()[:8], 16)
    d = duration_of(src)
    wav = dst + ".wav"; wavfile.write(wav, SR, make(d + 0.2, seed))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", wav, "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", dst], check=True)
    import os; os.remove(wav)

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    add_music(src, dst, int(sys.argv[3]) if len(sys.argv) > 3 else None)
    print("ok", dst)
