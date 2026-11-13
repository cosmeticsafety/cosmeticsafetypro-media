"""One English 16:9 video + extra-language audio tracks (same length) for YouTube multi-audio.

    PIPER_DIR=piper python3 tools/rp_video.py <kokoro_dir> <out_dir> [audio|video|all]
Outputs: <out_dir>/rp-overseas-brands.mp4 (English), audio-<lang>.mp3 per extra language,
chapters.txt, timeline.json. Each cue's slot is long enough for every language, so cards stay in sync.
"""
import sys, os, json, subprocess, base64
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF, WHATSAPP, SITE
from rp_video_content import SCENES
import music

ROOT = os.path.join(os.path.dirname(__file__), "..")
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "branding", "logo-crop.png"), "rb").read()).decode()
W, H, FPS, SR = 1920, 1080, 30, 44100
GAP, TAIL, LEAD, END = 0.45, 0.8, 0.5, 2.5
STRETCH = 1.15   # other languages may be sped up by at most this much to fit a slot
PRE = {"hi": 1.18}  # voices that are slow at their natural speed get this speed-up first
PIPER_DIR = os.environ.get("PIPER_DIR", "piper")
TTS = {"en": ("kokoro", "bf_emma", "en-gb", 1.0), "hi": ("kokoro", "hf_alpha", "hi", 1.0),
       "ar": ("piper", "ar_JO-kareem-medium", 0.72), "ur": ("piper", "ur_PK-fasih-medium", 0.95)}
LANGS = ["en", "ar", "ur", "hi"]
DARK = "--bg:#0A2350;--bg2:#13306A;--ink:#F3F6FA;--mint:#7CC47E;--mute:rgba(243,246,250,.74);--line:rgba(124,196,126,.30)"
LIGHT = "--bg:#F2F6F9;--bg2:#FFFFFF;--ink:#022356;--mint:#0B6A80;--mute:rgba(2,35,86,.70);--line:rgba(11,106,128,.24)"

_k = None
def say(text, lang, kdir):
    global _k
    t = TTS[lang]
    if t[0] == "kokoro":
        from kokoro_onnx import Kokoro
        if _k is None: _k = Kokoro(os.path.join(kdir, "kokoro-v1.0.int8.onnx"), os.path.join(kdir, "voices-v1.0.bin"))
        s, sr = _k.create(text, voice=t[1], lang=t[2], speed=t[3])
    else:
        tmp = "/tmp/_rp_piper.wav"
        subprocess.run(["python3", "-m", "piper", "-m", os.path.join(PIPER_DIR, t[1] + ".onnx"), "-f", tmp, "--length-scale", str(t[2])],
                       input=text.encode(), check=True, capture_output=True)
        s, sr = sf.read(tmp, dtype="float32")
        if s.ndim > 1: s = s.mean(1)
    s = resample_poly(np.asarray(s, np.float32), SR, sr).astype(np.float32)
    nz = np.where(np.abs(s) > 0.01 * (np.abs(s).max() or 1))[0]          # trim silence at both ends
    if len(nz): s = s[max(0, nz[0] - 800): nz[-1] + 2500]
    return s / (np.abs(s).max() or 1) * 0.85

def fit(s, slot):
    """Speed a clip up (pitch kept) so it lasts at most `slot` seconds."""
    d = len(s) / SR
    if d <= slot: return s
    a, b = "/tmp/_rp_a.wav", "/tmp/_rp_b.wav"; sf.write(a, s, SR)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", a, "-af", f"atempo={d / slot + 0.005:.4f}", b], check=True)
    o, _ = sf.read(b, dtype="float32"); return o[: int(slot * SR)]

def synth(kdir, cache):
    os.makedirs(cache, exist_ok=True)
    clips = {}
    for l in LANGS:
        for si, sc in enumerate(SCENES):
            for j, (_, txt) in enumerate(sc[4]):
                f = os.path.join(cache, f"{l}-{si}-{j}.wav")
                if not os.path.exists(f): sf.write(f, say(txt[l], l, kdir), SR)
                c = sf.read(f, dtype="float32")[0]
                clips[l, si, j] = fit(c, len(c) / SR / PRE[l]) if l in PRE else c
        print("voiced", l, flush=True)
    tl, t, tracks, worst = [], LEAD, {l: [] for l in LANGS}, {l: 1.0 for l in LANGS}
    for si, sc in enumerate(SCENES):
        st, seg = t, []
        for j in range(len(sc[4])):
            d = {l: len(clips[l, si, j]) / SR for l in LANGS}
            slot = max(d["en"], max(d[l] / STRETCH for l in LANGS))
            for l in LANGS:
                worst[l] = max(worst[l], d[l] / slot)
                tracks[l].append((t, fit(clips[l, si, j], slot)))
            seg.append(t - st); t += slot + GAP
        t += TAIL; tl.append({"start": st, "dur": t - st, "seg": seg})
    tl[0]["dur"] += tl[0]["start"]; tl[0]["seg"] = [x + tl[0]["start"] for x in tl[0]["seg"]]; tl[0]["start"] = 0.0
    tl[-1]["dur"] += END; total = t + END
    print("total", round(total, 1), "s; max speed-up", {l: round(v, 2) for l, v in worst.items()}, flush=True)
    return tl, tracks, total

def mixdown(tracks, total, out_dir):
    n = int(total * SR)
    bed = music.make(total + 1, seed=23).astype(np.float32)[:n, 0] / 32767 * 0.20
    fade = int(1.5 * SR); bed[-fade:] *= np.linspace(1, 0, fade)
    paths = {}
    for l, parts in tracks.items():
        v = np.zeros(n, np.float32)
        for t0, s in parts:
            i = int(t0 * SR); v[i:i + len(s)] += s[: n - i]
        mix = np.clip(v + bed, -0.98, 0.98); wav = os.path.join(out_dir, f"_{l}.wav")
        sf.write(wav, np.stack([mix, mix], 1), SR); paths[l] = wav
        if l != "en":
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-af", "loudnorm=I=-14:TP=-1.5", "-ar", "44100",
                            "-c:a", "libmp3lame", "-b:a", "192k", "-t", f"{total:.3f}", os.path.join(out_dir, f"audio-{l}.mp3")], check=True)
    return paths

JS = r"""
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3);
window.render=function(t){
  const T=window.TL; let cur=0, busy=false;
  for(let i=0;i<T.length;i++){ if(t>=T[i].start) cur=i; }
  document.querySelectorAll('.scene').forEach((el,i)=>{
    const s=T[i], lt=t-s.start, last=i===T.length-1;
    let o = i===cur ? Math.min(i===0?1:ease(lt/0.5), last?1:1-ease((lt-(s.dur-0.45))/0.45)) : 0;
    el.style.opacity=Math.max(0,o); el.style.visibility=o>0?'visible':'hidden';
    if(i!==cur) return;
    if((i>0&&lt<0.75)||(!last&&lt>s.dur-0.5)) busy=true;
    const h=el.querySelector('.ttl'); const p=i===0?1:ease(lt/0.7); h.style.transform=`translateY(${(1-p)*50}px)`;
    el.querySelectorAll('.card').forEach(c=>{const st=s.seg[+c.dataset.seg];const q=ease((lt-st)/0.5);
      if(lt>st-0.05&&lt<st+0.55) busy=true;
      c.style.opacity=q; c.style.transform=`translateX(${(1-q)*-80}px)`;});
  });
  const total=T[T.length-1].start+T[T.length-1].dur, sec=Math.floor(t);
  document.getElementById('bar').style.width=(Math.min(sec/total,1)*100)+'%';
  document.getElementById('chap').textContent=window.CH[cur];
  document.getElementById('fr').className='frame s'+cur;
  document.getElementById('mot').style.opacity=(cur===0||cur===T.length-1)?0:.14;
  return busy?'':cur+'|'+sec;   // '' = animating; otherwise a key that is equal for identical frames
};
"""

def scene_html(i, sc):
    chapter, kicker, title, theme, segs = sc
    cards = "".join(
        f'<div class="item card" data-seg="{j}" style="opacity:0;padding:22px 30px"><div class="num" style="width:54px;height:54px;font-size:26px">{n}</div>'
        f'<div class="itext" style="font-size:36px">{b}</div></div>'
        for n, (j, b) in enumerate([(j, b) for j, (b, _) in enumerate(segs) if b], 1))
    big = not cards; edge = i in (0, len(SCENES) - 1)
    body = (f'<div class="kicker" style="font-size:30px;margin-bottom:30px">{kicker}</div>'
            f'<h1 class="ttl" style="font-size:{112 if big else 84}px;max-width:{1050 if big or edge else 1600}px">{title}</h1>')
    if cards: body += f'<div class="items" style="gap:16px;margin-top:48px;max-width:{1000 if edge else 1400}px">{cards}</div>'
    if edge:
        body = f'<div style="max-width:1050px">{body}</div>' + (
            f'<div style="position:absolute;right:0;top:{-40 if big else 40}px;width:480px;height:480px;background:#fff;border-radius:40px;'
            f'display:flex;align-items:center;justify-content:center;box-shadow:0 30px 80px rgba(0,0,0,.25)"><img src="{LOGO}" style="width:400px"></div>')
    return (f'<style>.s{i}{{{DARK if theme == "D" else LIGHT}}}</style>'
            f'<div class="scene s{i}" style="position:absolute;inset:0;background:var(--bg);opacity:0">'
            f'<div style="position:absolute;left:150px;right:150px;top:{300 if big else 170}px">{body}</div></div>')

def page(tl):
    scenes = "".join(scene_html(i, sc) for i, sc in enumerate(SCENES))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}:root{{{DARK}}}
.scene .kicker{{color:var(--mint)}} .scene h1{{color:var(--ink)}} .scene h1 em{{color:var(--mint)}}
.scene .item{{background:var(--bg2);border-color:var(--line)}} .scene .num{{background:var(--mint);color:var(--bg)}} .scene .itext{{color:var(--ink)}}
#hud{{position:absolute;left:150px;right:150px;bottom:56px;display:flex;justify-content:space-between;align-items:center;font-size:24px;letter-spacing:.06em;color:var(--mute);z-index:5}}
</style></head><body>
<div id="fr" class="frame s0" style="width:{W}px;height:{H}px">
 {scenes}
 <div id="mot" style="position:absolute;right:-260px;top:120px;width:900px;opacity:.14;z-index:3;pointer-events:none;color:var(--mint)">{MOTIF}</div>
 <div style="position:absolute;left:150px;right:150px;top:40px;display:flex;justify-content:space-between;align-items:center;z-index:5" class="brand">
   <div style="display:flex;align-items:center;gap:18px"><span style="background:#fff;border-radius:16px;padding:6px 10px;display:inline-flex"><img src="{LOGO}" style="height:76px"></span>COSMETIC SAFETY PRO</div><div class="pill">UK · EU</div></div>
 <div id="hud"><span id="chap"></span><span>{SITE} · WhatsApp {WHATSAPP}</span></div>
 <div style="position:absolute;left:0;bottom:0;height:8px;background:var(--mint);z-index:6" id="bar"></div>
</div>
<script>window.TL={json.dumps(tl)};window.CH={json.dumps([s[0] for s in SCENES])};{JS}</script></body></html>"""

def film(tl, total, wav, out, stills=None):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.set_content(page(tl)); pg.wait_for_timeout(400)
        if stills:                       # preview: last second of each scene + frame 0
            for i, s in enumerate([{"start": 0, "dur": 0.2}] + tl):
                pg.evaluate(f"render({s['start'] + s['dur'] - 0.6 if i else 0})")
                pg.screenshot(path=os.path.join(stills, f"still-{i}.jpg"), type="jpeg", quality=85)
            b.close(); return
        tmp = out.replace(".mp4", ".part.mp4")
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-", "-i", wav,
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "veryfast", "-r", str(FPS), "-af", "loudnorm=I=-14:TP=-1.5",
            "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
        key, img, shots = None, None, 0
        for f in range(int(total * FPS)):
            k = pg.evaluate(f"render({f / FPS})")
            if not k or k != key:
                img = pg.screenshot(type="jpeg", quality=92); shots += 1
            key = k; ff.stdin.write(img)
        ff.stdin.close(); rc = ff.wait(); b.close()
        if rc == 0: os.replace(tmp, out)
        print("filmed", out, "screenshots", shots, "rc", rc, flush=True)

if __name__ == "__main__":
    kdir, out_dir = sys.argv[1], sys.argv[2]; mode = sys.argv[3] if len(sys.argv) > 3 else "all"
    os.makedirs(out_dir, exist_ok=True)
    tl, tracks, total = synth(kdir, "/tmp/rp_tts_cache")
    json.dump({"total": total, "timeline": tl}, open(os.path.join(out_dir, "timeline.json"), "w"))
    with open(os.path.join(out_dir, "chapters.txt"), "w") as fh:
        for i, s in enumerate(tl): fh.write(f"{int(s['start'] // 60)}:{int(s['start'] % 60):02d} {SCENES[i][0]}\n")
    if mode == "stills": film(tl, total, None, None, stills=out_dir); sys.exit()
    paths = mixdown(tracks, total, out_dir)
    if mode in ("video", "all"): film(tl, total, paths["en"], os.path.join(out_dir, "rp-overseas-brands.mp4"))
    for p_ in paths.values(): os.remove(p_)
