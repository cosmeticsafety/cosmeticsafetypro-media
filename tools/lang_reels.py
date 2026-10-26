"""Voiced 9:16 reels per language (35–45 s), brand colours + logo + music bed.

    python3 tools/lang_reels.py <tts_dir> fr [de it ...]
Output: reels/lang/<code>-cosmetics-checklist.mp4
"""
import sys, os, json, subprocess, base64
import numpy as np, soundfile as sf
from scipy.signal import resample_poly
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF
from lang_content import LANGS
import music

W, H, FPS, SR = 1080, 1920, 30, 44100
GAP, TAIL, LEAD = 0.3, 0.5, 1.0
ROOT = os.path.join(os.path.dirname(__file__), "..")
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "branding", "logo-crop.png"), "rb").read()).decode()
DARK = "--bg:#0A2350;--bg2:#13306A;--ink:#F3F6FA;--mint:#7CC47E;--mute:rgba(243,246,250,.74);--line:rgba(124,196,126,.30)"
LIGHT = "--bg:#F2F6F9;--bg2:#FFFFFF;--ink:#022356;--mint:#0B6A80;--mute:rgba(2,35,86,.70);--line:rgba(11,106,128,.24)"

def _v(bg, card, ink, acc):
    def rgba(h, a):
        h = h.lstrip('#'); return "rgba(%d,%d,%d,%s)" % (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)
    return f"--bg:{bg};--bg2:{card};--ink:{ink};--mint:{acc};--mute:{rgba(ink,.74)};--line:{rgba(acc,.30)}"

# Each language gets its own (dark, light) palette pair. fr/de use the brand navy.
PALETTES = {
 "de": (_v("#14181F", "#1F2530", "#F2F4F8", "#4FB3FF"), _v("#EEF3F8", "#FFFFFF", "#14181F", "#1F6FD1")),  # graphite + electric blue
 "it": (_v("#3B1410", "#52201A", "#FBF1EC", "#F2A65A"), _v("#FBF3EA", "#FFFFFF", "#3B1410", "#B5452B")),  # terracotta + apricot
 "es": (_v("#2A1B3D", "#3A2854", "#FBF6FF", "#FFC857"), _v("#FFF8E6", "#FFFFFF", "#2A1B3D", "#B4541A")),  # aubergine + saffron
 "nl": (_v("#2B1A0E", "#3D2716", "#FFF4EA", "#FF9F43"), _v("#FFF4EA", "#FFFFFF", "#2B1A0E", "#C2410C")),  # cocoa + orange
 "pt": (_v("#0F3B2E", "#16503F", "#F1FAF5", "#F2C14E"), _v("#EEF6F0", "#FFFFFF", "#0F3B2E", "#2E7D4F")),  # forest + gold
}

_kok = None
PIPER_DIR = os.environ.get("PIPER_DIR", "")
def say(text, tts):
    global _kok
    if tts[0] == "kokoro":
        from kokoro_onnx import Kokoro
        if _kok is None:
            _kok = Kokoro(os.path.join(TTS_DIR, "kokoro-q8.onnx"), os.path.join(TTS_DIR, "voices.bin"))
        s, sr = _kok.create(text, voice=tts[1], lang=tts[2], speed=1.12)
    elif tts[0] == "piper":
        tmp = "/tmp/_piper.wav"
        model = os.path.join(PIPER_DIR, tts[1] + ".onnx")
        subprocess.run(["python3", "-m", "piper", "-m", model, "-f", tmp, "--length-scale", str(tts[2] if len(tts) > 2 else 0.92)],
                       input=text.encode(), check=True, capture_output=True)
        s, sr = sf.read(tmp, dtype="float32")
        if s.ndim > 1: s = s.mean(1)
    else:
        tmp = "/tmp/_esp.wav"
        subprocess.run(["espeak-ng", "-v", tts[1], "-s", "165", "-w", tmp, text], check=True, capture_output=True)
        s, sr = sf.read(tmp, dtype="float32")
        if s.ndim > 1: s = s.mean(1)
    s = resample_poly(np.asarray(s, np.float32), SR, sr).astype(np.float32)
    return s / (np.abs(s).max() or 1) * 0.85

def synth(scenes, tts):
    tl, parts, t = [], [np.zeros(int(LEAD * SR), np.float32)], LEAD
    for kicker, title, big, segs in scenes:
        st, seg = t, []
        for text, _ in segs:
            a = say(text, tts); seg.append(t - st); parts.append(a); t += len(a) / SR
            parts.append(np.zeros(int(GAP * SR), np.float32)); t += GAP
        parts.append(np.zeros(int(TAIL * SR), np.float32)); t += TAIL
        tl.append({"start": st, "dur": t - st, "seg": seg})
    return np.concatenate(parts), tl

JS = r"""
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3);
window.render=function(t){
  const T=window.TL; let cur=0; for(let i=0;i<T.length;i++) if(t>=T[i].start) cur=i;
  document.querySelectorAll('.scene').forEach((el,i)=>{
    const s=T[i], lt=t-s.start; let o=i===cur?Math.min(ease(lt/0.45),1-ease((lt-(s.dur-0.4))/0.4)):0;
    if(i===0&&t<s.start) o=ease(t/0.6);
    if(i===T.length-1&&i===cur) o=Math.min(1,ease(lt/0.45));
    el.style.opacity=Math.max(0,o); el.style.visibility=o>0?'visible':'hidden'; if(i!==cur&&!(i===0&&t<s.start)) return;
    el.querySelectorAll('.ttl').forEach(h=>{const p=ease((Math.max(lt,0))/0.7); h.style.transform=`translateY(${(1-p)*60}px)`;});
    el.querySelectorAll('.card').forEach(c=>{const q=ease((lt-s.seg[+c.dataset.seg])/0.5); c.style.opacity=q; c.style.transform=`translateX(${(1-q)*-90}px)`;});
  });
  const tot=T[T.length-1].start+T[T.length-1].dur; document.getElementById('bar').style.width=(Math.min(t/tot,1)*100)+'%';
  document.getElementById('fr').className='frame s'+cur;
  const m=document.getElementById('mot'); m.style.transform=`rotate(${t*3}deg)`;
};
"""

def page(lang, scenes, tl):
    css = ""; html = ""
    for i, (kicker, title, big, segs) in enumerate(scenes):
        dk, lt = PALETTES.get(lang, (DARK, LIGHT)); css += f".s{i}{{{dk if i % 2 == 0 else lt}}}"
        cards = "".join(
            f'<div class="item card" data-seg="{j}" style="opacity:0;padding:24px 30px"><div class="num" style="width:62px;height:62px;font-size:30px">{n}</div>'
            f'<div class="itext" style="font-size:42px">{b}</div></div>'
            for n, (j, b) in enumerate([(j, b) for j, (_, b) in enumerate(segs) if b], 1))
        logo = (f'<div class="ttl" style="width:420px;height:420px;background:#fff;border-radius:44px;display:flex;align-items:center;justify-content:center;'
                f'box-shadow:0 30px 80px rgba(0,0,0,.28);margin-bottom:70px"><img src="{LOGO}" style="width:350px"></div>') if big else ""
        html += (f'<div class="scene s{i}" style="position:absolute;inset:0;background:var(--bg);opacity:0">'
                 f'<div style="position:absolute;left:90px;right:90px;top:{330 if big else 380}px">{logo}'
                 f'<div class="kicker" style="font-size:32px;margin-bottom:30px">{kicker}</div>'
                 f'<h1 class="ttl" style="font-size:{100 if big else 92}px">{title}</h1>'
                 f'<div class="items" style="gap:20px;margin-top:56px">{cards}</div></div></div>')
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}{css}
.scene .kicker{{color:var(--mint)}} .scene h1{{color:var(--ink)}} .scene h1 em{{color:var(--mint)}}
.scene .item{{background:var(--bg2);border-color:var(--line)}} .scene .num{{background:var(--mint);color:var(--bg)}} .scene .itext{{color:var(--ink)}}
</style></head><body><div id="fr" class="frame s0" style="width:{W}px;height:{H}px">{html}
<div id="mot" style="position:absolute;right:-300px;top:1150px;width:820px;opacity:.13;color:var(--mint);z-index:3;pointer-events:none">{MOTIF}</div>
<div class="brand" style="position:absolute;left:90px;right:90px;top:90px;z-index:5">
 <div style="display:flex;align-items:center;gap:20px"><span style="background:#fff;border-radius:18px;padding:8px 12px;display:inline-flex"><img src="{LOGO}" style="height:96px"></span><span style="font-size:28px">COSMETIC SAFETY PRO</span></div>
 <div class="pill" style="font-size:26px">{LANGS[lang]['flag']} · UK · EU</div></div>
<div style="position:absolute;left:90px;right:90px;bottom:120px;font-size:30px;color:var(--mute);z-index:5;line-height:1.5">cosmeticsafetypro.com<br>WhatsApp +44 7868 737497</div>
<div id="bar" style="position:absolute;left:0;bottom:0;height:12px;background:var(--mint);z-index:6"></div>
</div><script>window.TL={json.dumps(tl)};{JS}</script></body></html>"""

def build(lang):
    spec = LANGS[lang]; scenes = spec["scenes"]
    voice, tl = synth(scenes, spec["tts"])
    total = len(voice) / SR + 0.6
    bed = music.make(total, seed=hash(lang) % 1000).astype(np.float32)[:, 0] / 32767 * 0.20
    v = np.zeros_like(bed); v[:len(voice)] = voice
    mix = np.clip(v + bed, -0.98, 0.98)
    out_dir = os.path.join(ROOT, "reels", "lang"); os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"{lang}-cosmetics-checklist.mp4"); wav = out + ".wav"
    sf.write(wav, np.stack([mix, mix], 1), SR)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.set_content(page(lang, scenes, tl)); pg.wait_for_timeout(300)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-", "-i", wav,
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-r", str(FPS), "-af", "loudnorm=I=-14:TP=-1.5",
            "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for f in range(int(total * FPS)):
            pg.evaluate(f"render({f / FPS})"); ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
        ff.stdin.close(); ff.wait()
        pg.evaluate(f"render({tl[1]['start'] + tl[1]['dur'] - 1})")
        pg.screenshot(path=out.replace(".mp4", "-cover.jpg"), type="jpeg", quality=88); b.close()
    os.remove(wav)
    print("ok", lang, round(total, 1), "s", flush=True)

if __name__ == "__main__":
    TTS_DIR = sys.argv[1]
    for l in sys.argv[2:]: build(l)
