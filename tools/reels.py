import sys, os, json, subprocess
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF, WHATSAPP, SITE, theme_css

OUT = os.path.join(os.path.dirname(__file__), "..", "reels")
os.makedirs(OUT, exist_ok=True)
FPS = 30
W, H = 1080, 1920

REELS = [
 ("2026-10-19-sell-uk", "Before you sell", "3 things you need before selling cosmetics in the <em>UK</em>",
  "Your checklist", ["A Cosmetic Product Safety Report (CPSR)", "A UK-based Responsible Person", "An SCPN notification before launch"]),
 ("2026-10-20-etsy-myth", "Myth vs fact", "“I only sell on Etsy, so I don't need a <em>CPSR</em>.”",
  "Fact", ["Every cosmetic sold in the UK or EU needs a CPSR", "Etsy, Amazon, markets: same law", "No size exemption for small makers"]),
 ("2026-10-21-cpnp-steps", "EU launch", "How to notify your product on the <em>CPNP</em>",
  "The process", ["Appoint an EU Responsible Person", "Complete your CPSR and PIF", "Submit the CPNP notification", "Start selling across the EU"]),
 ("2026-10-22-pif", "Audit-ready?", "Could you show an inspector your <em>PIF</em> today?",
  "It must contain", ["Product description", "Safety report (CPSR)", "GMP statement", "Proof of claims", "Animal testing data"]),
 ("2026-10-23-label", "Label check", "Is your cosmetic label <em>legally compliant</em>?",
  "It must show", ["Responsible Person name + address", "Nominal content", "Best-before or PAO symbol", "Batch number", "Full INCI ingredient list"]),
 ("2026-10-24-scpn-cpnp", "UK vs EU", "<em>SCPN</em> or <em>CPNP</em>? Which do you need?",
  "Quick answer", ["Great Britain → SCPN", "EU countries → CPNP", "Northern Ireland → CPNP", "Selling in both → you need both"]),
 ("2026-10-25-rp", "Explained", "What is a <em>Responsible Person</em>?",
  "They", ["Are your legal contact for regulators", "Keep your PIF and CPSR on file", "Notify your products", "Appear on your label"]),
 ("2026-10-26-how-long", "FAQ", "How long does a <em>CPSR</em> take?",
  "With us", ["Free formula review first", "Standard report: 1–2 weeks", "Express: 24–48 hours", "Valid for UK and EU"]),
]

JS = r"""
const ease=t=>t<0?0:t>1?1:1-Math.pow(1-t,3);
function show(el,t0,t,dur=0.6,dy=60){const p=ease((t-t0)/dur);el.style.opacity=p;el.style.transform=`translateY(${(1-p)*dy}px)`;}
function hide(el,t1,t,dur=0.4){const p=ease((t-t1)/dur);if(t>=t1){el.style.opacity=Math.min(+el.style.opacity,1-p);}}
window.render=function(t){
  const D=window.D, n=D.n;
  const listStart=3.2, itemGap=1.0, ctaStart=listStart+0.8+n*itemGap+1.6, total=ctaStart+3.4;
  document.getElementById('bar').style.width=(Math.min(t/total,1)*100)+'%';
  // hook
  const hk=document.getElementById('hookK'), hh=document.getElementById('hookH');
  show(hk,0.1,t); show(hh,0.35,t,0.8,90); hide(hk,listStart-0.5,t); hide(hh,listStart-0.5,t);
  // list
  const lk=document.getElementById('listK'); show(lk,listStart,t); hide(lk,ctaStart-0.4,t);
  document.querySelectorAll('.ri').forEach((el,i)=>{show(el,listStart+0.6+i*itemGap,t,0.55,0);
     const p=ease((t-(listStart+0.6+i*itemGap))/0.55); el.style.transform=`translateX(${(1-p)*-120}px)`; hide(el,ctaStart-0.4,t);});
  // cta
  ['ctaA','ctaB','ctaC'].forEach((id,i)=>show(document.getElementById(id),ctaStart+i*0.35,t));
  // motif slow drift
  document.getElementById('mot').style.transform=`rotate(${t*3}deg)`;
  return total;
};
"""

def html(reel):
    name, kicker, hook, listk, items = reel
    rows = "".join(f'<div class="item ri" style="opacity:0;padding:30px 34px"><div class="num" style="width:68px;height:68px;font-size:34px">{i+1}</div>'
                   f'<div class="itext" style="font-size:44px">{t}</div></div>' for i, t in enumerate(items))
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{theme_css(name)}
.L{{position:absolute;left:90px;right:90px}}</style></head><body>
<div class="frame" style="width:{W}px;height:{H}px">
 <div id="mot" style="position:absolute;right:-260px;top:520px;width:760px;opacity:.22">{MOTIF}</div>
 <div style="position:absolute;left:0;top:0;height:10px;background:var(--mint)" id="bar"></div>
 <div class="L brand" style="top:150px;font-size:28px"><div><span class="dot"></span>COSMETIC SAFETY PRO</div><div class="pill" style="font-size:24px">UK · EU</div></div>
 <div class="L" style="top:640px">
   <div id="hookK" class="kicker" style="opacity:0;font-size:34px;margin-bottom:34px">{kicker}</div>
   <h1 id="hookH" style="opacity:0;font-size:{108 if len(hook)<60 else 96}px">{hook}</h1>
 </div>
 <div class="L" style="top:560px">
   <div id="listK" class="kicker" style="opacity:0;font-size:34px;margin-bottom:40px">{listk}</div>
   <div class="items" style="gap:22px">{rows}</div>
 </div>
 <div class="L" style="top:700px;text-align:left">
   <h1 id="ctaA" style="opacity:0;font-size:104px;margin-bottom:46px">Get compliant <em>with confidence.</em></h1>
   <div id="ctaB" style="opacity:0;display:inline-block" class="cta"><span style="font-size:40px;padding:6px 10px;display:inline-block">Free formula review</span></div>
   <div id="ctaC" style="opacity:0;margin-top:56px;font-size:40px;color:var(--mute);line-height:1.5">WhatsApp <b style="color:var(--ink)">{WHATSAPP}</b><br>{SITE}</div>
 </div>
</div>
<script>window.D={{n:{len(items)}}};{JS}</script></body></html>"""

def render_reel(pg, reel):
    name = reel[0]
    pg.set_content(html(reel)); pg.wait_for_timeout(200)
    total = pg.evaluate("render(0)")
    nframes = int(total * FPS)
    out = os.path.join(OUT, name + ".mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
        "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "20", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
    for f in range(nframes):
        pg.evaluate(f"render({f / FPS})")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
    ff.stdin.close(); ff.wait()
    # cover frame (mid-hook)
    pg.evaluate("render(2.5)"); pg.screenshot(path=os.path.join(OUT, name + "-cover.jpg"), type="jpeg", quality=90)
    print("ok", name, round(total, 1), "s")

if __name__ == "__main__":
    which = sys.argv[1:] or [r[0] for r in REELS]
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": W, "height": H})
        for r in REELS:
            if r[0] in which: render_reel(pg, r)
        b.close()
