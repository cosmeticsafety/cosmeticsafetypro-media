"""Croatian reel from a supplied voiceover (no Piper voice exists for Croatian).
Timings were taken from the pauses in reels/lang/hr-voice-ttsmaker.mp3 (ffmpeg silencedetect).
    python3 tools/hr_reel.py
"""
import os, sys, subprocess
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
sys.path.insert(0, os.path.dirname(__file__))
import lang_reels as L
from lang_content import LANGS
from playwright.sync_api import sync_playwright
import music

PAD = 0.2  # voice starts almost immediately
# absolute speech times in the mp3 (s): scene starts and each segment start
SCENES = [(0.0, [0.0]),
          (7.3, [7.63, 10.14, 12.42, 16.09, 18.59]),
          (21.4, [21.90, 24.6, 27.98]),
          (32.65, [33.15, 38.4])]
src = os.path.join(L.ROOT, LANGS["hr"]["tts"][1])
wav = "/tmp/_hr_src.wav"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", "44100", wav], check=True)
v, sr = sf.read(wav, dtype="float32")
v = v / (np.abs(v).max() or 1) * 0.85
voice = np.concatenate([np.zeros(int(PAD * L.SR), np.float32), v])
total = len(voice) / L.SR + 0.6
tl = []
for i, (st, segs) in enumerate(SCENES):
    s = 0.0 if i == 0 else st + PAD
    e = (SCENES[i + 1][0] + PAD) if i + 1 < len(SCENES) else total
    tl.append({"start": s, "dur": e - s, "seg": [max(0.0, t + PAD - s) for t in segs]})
scenes, tl, total = L.with_end("hr", LANGS["hr"]["scenes"], tl, start=len(voice) / L.SR + 0.3)
bed = music.make(total, seed=hash("hr") % 1000).astype(np.float32)[:, 0] / 32767 * 0.20
vv = np.zeros_like(bed); vv[:len(voice)] = voice[:len(bed)]
mix = np.clip(vv + bed, -0.98, 0.98)
out = os.path.join(L.ROOT, "reels", "lang", "hr-cosmetics-checklist.mp4"); w2 = out + ".wav"
sf.write(w2, np.stack([mix, mix], 1), L.SR)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": L.W, "height": L.H})
    pg.set_content(L.page("hr", scenes, tl)); pg.wait_for_timeout(300)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(L.FPS), "-i", "-", "-i", w2,
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-r", str(L.FPS), "-af", "loudnorm=I=-14:TP=-1.5",
        "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for f in range(int(total * L.FPS)):
        pg.evaluate(f"render({f / L.FPS})"); ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
    ff.stdin.close(); ff.wait()
    pg.evaluate(f"render({tl[1]['start'] + tl[1]['dur'] - 1})")
    pg.screenshot(path=out.replace(".mp4", "-cover.jpg"), type="jpeg", quality=88); b.close()
os.remove(w2)
print("ok hr", round(total, 1), "s")
