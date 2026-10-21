"""Narrated 16:9 explainer video for YouTube (Cosmetic Safety Pro).

Voice: Kokoro-82M (Apache-2.0) run offline via kokoro-onnx. Model + voices come
from npm (kokoro-q8-shards, kokoro-js) — see TTS_DIR setup in README below.
Each scene = a title + bullet cards; every bullet has its own narration line, so
cards appear exactly when the voice reaches them. Background music from music.py
is mixed underneath.

    python3 tools/video.py <tts_dir> <out.mp4>
"""
import sys, os, json, subprocess
import numpy as np
import soundfile as sf
from scipy.signal import resample_poly
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF, WHATSAPP, SITE
import music, base64
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(os.path.dirname(__file__), "..", "branding", "logo-crop.png"), "rb").read()).decode()

W, H, FPS, SR = 1920, 1080, 30, 44100
VOICE, LANG, SPEED = "bf_emma", "en-gb", 1.0
GAP = 0.6          # silence between narration lines (s)
TAIL = 1.0          # pause at end of each scene (s)

DARK = (":root{--bg:#0A2350;--bg2:#13306A;--ink:#F3F6FA;--mint:#7CC47E;--mute:rgba(243,246,250,.74);--line:rgba(124,196,126,.30)}")
LIGHT = (":root{--bg:#F2F6F9;--bg2:#FFFFFF;--ink:#022356;--mint:#0B6A80;--mute:rgba(2,35,86,.70);--line:rgba(11,106,128,.24)}")

# (chapter, kicker, title_html, theme, [(narration, bullet or None), ...])
SCENES = [
 ("Introduction", "Full guide · UK &amp; EU", "How to sell cosmetics <em>legally</em> in the UK &amp; EU", DARK, [
   ("Want to sell skincare, cosmetics or perfume in the UK or Europe?", None),
   ("Before a single product reaches a customer, the law requires a few key things to be in place.", None),
   ("In the next few minutes, we'll walk you through exactly what you need, and how Cosmetic Safety Pro can get your products compliant, fast.", None)]),
 ("The four essentials", "Overview", "The <em>four essentials</em>", LIGHT, [
   ("There are four essentials for every cosmetic product.", None),
   ("A Cosmetic Product Safety Report.", "Cosmetic Product Safety Report (CPSR)"),
   ("A Responsible Person.", "A Responsible Person (UK and/or EU)"),
   ("A Product Information File.", "A Product Information File (PIF)"),
   ("And a product notification: through the Submit Cosmetic Product Notification service in Great Britain, or the Cosmetic Product Notification Portal in the European Union. Let's look at each one.", "A notification: SCPN (GB) or CPNP (EU)")]),
 ("CPSR: the safety report", "Essential 1", "The <em>CPSR</em>: your product's safety report", DARK, [
   ("The Cosmetic Product Safety Report is the heart of compliance. It's a safety assessment of your finished product, in two parts.", None),
   ("Part A gathers the safety information: the formula, stability and microbiological data, how much product people are exposed to, and the toxicology of every ingredient.", "Part A: formula, stability, microbiology, exposure, toxicology"),
   ("Part B is the assessment itself, where a qualified Safety Assessor reviews it all and confirms the product is safe to use.", "Part B: signed off by a qualified Safety Assessor"),
   ("And yes, you need one whether you sell on Etsy, on Amazon, at a local market, or through a major retailer.", "Required for Etsy, Amazon, markets and retail alike")]),
 ("Responsible Person", "Essential 2", "Who is your <em>Responsible Person</em>?", LIGHT, [
   ("Next, every cosmetic needs a Responsible Person: the legal point of contact for your product.", None),
   ("They make sure a valid safety report is in place,", "Ensures a valid CPSR is in place"),
   ("keep the Product Information File,", "Holds and maintains the PIF"),
   ("notify the product,", "Notifies the product (SCPN / CPNP)"),
   ("and report any serious undesirable effects to the authorities.", "Reports serious undesirable effects"),
   ("Their name and address must appear on your label. For Great Britain they must be based in the UK, and for the EU, in the EU.", "Name and address on your label, UK- or EU-based")]),
 ("SCPN and CPNP notifications", "Essential 3", "Notify <em>before</em> you sell", DARK, [
   ("Before your product goes on sale, it must be notified.", None),
   ("In Great Britain, that's done through the Submit Cosmetic Product Notification service, run by the Office for Product Safety and Standards.", "Great Britain → SCPN (OPSS)"),
   ("In the European Union, it's the Cosmetic Product Notification Portal.", "European Union → CPNP"),
   ("Northern Ireland follows the E U route.", "Northern Ireland → CPNP"),
   ("So if you sell in both markets, you need both notifications.", "Selling in both? You need both")]),
 ("Product Information File", "Essential 4", "Inside your <em>Product Information File</em>", LIGHT, [
   ("Your Product Information File brings everything together. It must include:", None),
   ("a description of the product,", "Product description"),
   ("the safety report,", "The CPSR"),
   ("the manufacturing method, with a statement of good manufacturing practice,", "Manufacturing method + GMP statement"),
   ("proof of any claims made on the label,", "Proof of label claims"),
   ("and data on any animal testing.", "Animal testing data"),
   ("The file must be kept ready for inspection for ten years after the last batch is placed on the market.", "Kept for 10 years after the last batch")]),
 ("Labelling requirements", "Your label", "What your <em>label</em> must show", DARK, [
   ("Finally, your label. Under U K and E U rules, it must show:", None),
   ("the Responsible Person's name and address,", "Responsible Person name + address"),
   ("the nominal content,", "Nominal content (ml or g)"),
   ("a best before date, or a period after opening symbol,", "Best-before date or PAO symbol"),
   ("a batch number, and any precautions for use,", "Batch number + precautions"),
   ("and a full ingredient list using International Nomenclature of Cosmetic Ingredients names, including fragrance allergens above the labelling thresholds.", "Full INCI list incl. labelled allergens")]),
 ("Rules keep changing", "Regulatory update", "The rules keep <em>changing</em>", LIGHT, [
   ("Regulations also keep changing.", None),
   ("In the E U, the list of fragrance allergens that may need labelling has grown from twenty-six to eighty-one.", "EU: labelled fragrance allergens 26 → 81"),
   ("In the U K, new bans have recently come into force, including the U V filter four-methylbenzylidene camphor, and trimethylbenzoyl diphenylphosphine oxide, used in gel nail products.", "UK: new bans incl. 4-MBC and TPO"),
   ("Staying compliant means keeping your safety reports and labels up to date.", "Keep your CPSR and labels up to date")]),
 ("How Cosmetic Safety Pro helps", "How we help", "Compliance, <em>done for you</em>", DARK, [
   ("That's where Cosmetic Safety Pro comes in.", None),
   ("We prepare your Cosmetic Product Safety Report with a qualified Safety Assessor,", "CPSR by a qualified Safety Assessor"),
   ("act as your U K and E U Responsible Person,", "UK & EU Responsible Person"),
   ("handle your notifications on both the U K and E U portals,", "SCPN & CPNP notifications"),
   ("build your Product Information File, and review your labels.", "PIF + label & CLP review"),
   ("Standard reports take one to two weeks, and our express service can deliver in as little as twenty-four to forty-eight hours.", "Express CPSR in 24–48 hours")]),
 ("Free formula review", "Get started", "Start with a <em>free formula review</em>", DARK, [
   ("Start with a free, confidential review of your formula.", None),
   ("Message us on WhatsApp at plus four four, seven eight six eight, seven three seven, four nine seven.", "WhatsApp " + WHATSAPP),
   ("Email info at cosmetic safety pro dot com,", "info@cosmeticsafetypro.com"),
   ("or visit cosmetic safety pro dot com. Launch legally, and sell with confidence.", SITE)]),
]

def synth(tts_dir):
    from kokoro_onnx import Kokoro
    k = Kokoro(os.path.join(tts_dir, "kokoro-q8.onnx"), os.path.join(tts_dir, "voices.bin"))
    timeline, audio, t = [], [], 0.0
    for si, (chapter, kicker, title, theme, segs) in enumerate(SCENES):
        start = t; seg_times = []
        for text, bullet in segs:
            s, sr = k.create(text, voice=VOICE, speed=SPEED, lang=LANG)
            s = resample_poly(s, SR, sr).astype(np.float32)
            seg_times.append(t - start)
            audio.append(s); t += len(s) / SR
            gap = np.zeros(int(GAP * SR), np.float32); audio.append(gap); t += GAP
        tail = np.zeros(int(TAIL * SR), np.float32); audio.append(tail); t += TAIL
        timeline.append({"start": start, "dur": t - start, "seg": seg_times})
    lead = np.zeros(int(1.0 * SR), np.float32)
    voice = np.concatenate([lead] + audio)
    for sc in timeline: sc["start"] += 1.0
    return voice, timeline

JS = r"""
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3);
window.render=function(t){
  const T=window.TL; let cur=0;
  for(let i=0;i<T.length;i++){ if(t>=T[i].start) cur=i; }
  document.querySelectorAll('.scene').forEach((el,i)=>{
    const s=T[i], lt=t-s.start, end=s.dur;
    let o = i===cur ? Math.min(ease(lt/0.5), 1-ease((lt-(end-0.45))/0.45)) : 0;
    if(i===0 && t<0.6) o=ease(t/0.6);
    el.style.opacity=Math.max(0,o); el.style.visibility=o>0?'visible':'hidden';
    if(i!==cur) return;
    const h=el.querySelector('.ttl'); const p=ease(lt/0.7); h.style.transform=`translateY(${(1-p)*50}px)`;
    el.querySelectorAll('.card').forEach(c=>{const st=s.seg[+c.dataset.seg];const q=ease((lt-st)/0.5);
      c.style.opacity=q; c.style.transform=`translateX(${(1-q)*-80}px)`;});
  });
  const total=T[T.length-1].start+T[T.length-1].dur;
  document.getElementById('bar').style.width=(Math.min(t/total,1)*100)+'%';
  document.getElementById('chap').textContent=window.CH[cur];
  document.getElementById('fr').className='frame s'+cur;
  const m=document.getElementById('mot'); m.style.transform=`rotate(${t*2}deg)`; m.style.opacity=(cur===0||cur===T.length-1)?0:.14;
};
"""

def scene_html(i, sc):
    chapter, kicker, title, theme, segs = sc
    cards = "".join(
        f'<div class="item card" data-seg="{j}" style="opacity:0;padding:22px 30px"><div class="num" style="width:54px;height:54px;font-size:26px">{n}</div>'
        f'<div class="itext" style="font-size:36px">{b}</div></div>'
        for n, (j, b) in enumerate([(j, b) for j, (_, b) in enumerate(segs) if b], 1))
    big = not any(b for _, b in segs)
    cls = f"scene s{i}"
    body = (f'<div class="kicker" style="font-size:30px;margin-bottom:30px">{kicker}</div>'
            f'<h1 class="ttl" style="font-size:{112 if big else 84}px;max-width:{1050 if big else 1600}px">{title}</h1>')
    if cards:
        body += f'<div class="items" style="gap:16px;margin-top:48px;max-width:{1000 if i in (0, len(SCENES)-1) else 1300}px">{cards}</div>'
    if i in (0, len(SCENES) - 1):
        body = f'<div style="max-width:1050px">{body}</div>' + (
            f'<div class="ttl" style="position:absolute;right:0;top:{-40 if big else 40}px;width:480px;height:480px;background:#fff;border-radius:40px;'
            f'display:flex;align-items:center;justify-content:center;box-shadow:0 30px 80px rgba(0,0,0,.25)"><img src="{LOGO}" style="width:400px"></div>')
    return (f'<style>.s{i}{{{theme.split("{",1)[1].rstrip("}")}}}</style>'
            f'<div class="{cls}" style="position:absolute;inset:0;background:var(--bg);opacity:0">'
            f'<div style="position:absolute;left:150px;right:150px;top:{300 if big else 170}px">{body}</div></div>')

def page(timeline):
    scenes = "".join(scene_html(i, sc) for i, sc in enumerate(SCENES))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{DARK}
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
<script>window.TL={json.dumps(timeline)};window.CH={json.dumps([s[0] for s in SCENES])};{JS}</script></body></html>"""

def build(tts_dir, out):
    voice, timeline = synth(tts_dir)
    total = len(voice) / SR + 0.4
    # music bed, ducked well under the voice
    bed = music.make(total, seed=11).astype(np.float32) / 32767
    bed = bed[:, 0] * 0.22
    v = np.zeros_like(bed); v[:len(voice)] = voice / (np.abs(voice).max() or 1) * 0.8
    mix = np.clip(v + bed, -0.98, 0.98)
    wav = out + ".wav"; sf.write(wav, np.stack([mix, mix], 1), SR)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        pg.set_content(page(timeline)); pg.wait_for_timeout(300)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
            "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for f in range(int(total * FPS)):
            pg.evaluate(f"render({f / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
        ff.stdin.close(); ff.wait(); b.close()
    os.remove(wav)
    chapters = [(sc["start"], SCENES[i][0]) for i, sc in enumerate(timeline)]
    with open(out + ".chapters.txt", "w") as fh:
        for i, (s, name) in enumerate(chapters):
            s = 0 if i == 0 else s
            fh.write(f"{int(s // 60)}:{int(s % 60):02d} {name}\n")
    print("ok", out, round(total, 1), "s")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
