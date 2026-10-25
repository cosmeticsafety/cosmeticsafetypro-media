import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF, WHATSAPP, SITE, theme_css

OUT = os.path.join(os.path.dirname(__file__), "..", "posts")
os.makedirs(OUT, exist_ok=True)

POSTS = [
 ("2026-10-27-omnibus-vi", "⚡ Regulatory update · EU", "EU Parliament approves <em>Omnibus VI</em> for cosmetics",
  ["Final vote 22 Oct 2026: 477 for, 59 against", "New CMR timelines replace the 18-month withdrawal",
   "No exemption sought: 6 months to stop placing, 12 to sell out", "Next: Council adoption, then the Official Journal"]),
 ("2026-10-28-perfume-launch", "Fragrance brands", "Launching a <em>perfume</em> in the UK or EU?",
  ["IFRA certificate from your fragrance supplier", "Allergen data for the label and the CPSR",
   "CPSR signed by a qualified safety assessor", "Responsible Person + CPNP / SCPN notification",
   "Label check: INCI, warnings, batch, nominal content"]),
 ("2026-10-29-claims", "Marketing claims", "Can you prove your <em>cosmetic claims</em>?",
  ["Legal compliance", "Truthfulness", "Evidential support", "Honesty", "Fairness", "Informed decision-making"]),
 ("2026-10-30-pfhxa", "⚡ Regulatory update · EU", "EU <em>PFHxA</em> limits now apply to cosmetics",
  ["In force since 10 Oct 2026 (REACH Annex XVII)", "PFHxA + salts: under 25 ppb in the formula",
   "PFHxA-related substances: under 1,000 ppb", "Check raw materials for PFAS impurities"]),
 ("2026-10-31-shelf-life", "Label basics", "<em>PAO</em> or best-before date? Get it right.",
  ["Lasts 30 months or less: show a best-before date", "Lasts over 30 months: PAO jar symbol, e.g. 12M",
   "Stability testing must back the shelf life", "Both are checked in your CPSR"]),
 ("2026-11-01-nano", "Nanomaterials", "Using <em>nano</em> ingredients? Notify 6 months early.",
  ["EU: notify via CPNP 6 months before sale", "GB: notify OPSS 6 months before sale",
   "List them on the label as [nano]", "Safety data must cover the nano form"]),
]

def page_html(body, w, h, name):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{theme_css(name)}</style></head>
<body><div class="frame" style="width:{w}px;height:{h}px">{body}</div></body></html>"""

def list_post(kicker, title, items):
    n = len(items)
    rows = "".join(f'<div class="item" style="padding:{20 if n>4 else 26}px 30px"><div class="num" style="width:56px;height:56px;font-size:28px">{i+1}</div>'
                   f'<div class="itext" style="font-size:{31 if n>4 else 34}px">{t}</div></div>' for i, t in enumerate(items))
    return f"""<div class="motif">{MOTIF}</div>
<div style="position:relative;height:100%;padding:80px 84px 70px;display:flex;flex-direction:column;gap:36px">
 <div class="brand"><div><span class="dot"></span>COSMETIC SAFETY PRO</div><div class="pill">UK · EU</div></div>
 <div style="display:flex;flex-direction:column;gap:26px;margin-top:14px">
  <div class="kicker">{kicker}</div>
  <h1 style="font-size:{74 if len(title)>60 else 82}px;max-width:900px">{title}</h1>
 </div>
 <div class="items" style="gap:{16 if n>4 else 20}px">{rows}</div>
 <div style="flex:1"></div>
 <div class="footer"><div>WhatsApp <b>{WHATSAPP}</b><br>{SITE}</div><div class="cta">Free formula review</div></div>
</div>"""

def compare_post():
    def col(flag, name, law, rp, notif):
        return f"""<div class="col"><h3>{name}</h3>
<div class="row"><small>LAW</small><span>{law}</span></div>
<div class="row"><small>RESPONSIBLE PERSON</small><span>{rp}</span></div>
<div class="row"><small>NOTIFICATION</small><span>{notif}</span></div></div>"""
    return f"""<div class="motif">{MOTIF}</div>
<div style="position:relative;height:100%;padding:80px 84px 70px;display:flex;flex-direction:column;gap:34px">
 <div class="brand"><div><span class="dot"></span>COSMETIC SAFETY PRO</div><div class="pill">UK · EU</div></div>
 <div style="display:flex;flex-direction:column;gap:26px;margin-top:20px">
  <div class="kicker">One product · Two markets</div>
  <h1 style="font-size:82px">UK vs <em>EU</em> compliance at a glance</h1>
 </div>
 <div>
  <div class="cols">{col('', 'Great Britain', 'UK Cosmetics Regulation', 'UK-based', 'SCPN')}{col('', 'European Union', 'Reg. (EC) 1223/2009', 'EU-based', 'CPNP')}</div>
  <div class="same"><b>Same in both:</b> a CPSR, a Product Information File and a compliant label.</div>
 </div>
 <div style="flex:1"></div>
 <div class="footer"><div>WhatsApp <b>{WHATSAPP}</b><br>{SITE}</div><div class="cta">Free formula review</div></div>
</div>"""

def render(pairs, w=1080, h=1350):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": h})
        for name, body in pairs:
            pg.set_content(page_html(body, w, h, name)); pg.wait_for_timeout(150)
            png = os.path.join(OUT, name + ".png"); pg.screenshot(path=png)
            Image.open(png).convert("RGB").save(png[:-4] + ".jpg", quality=92); os.remove(png)
            print("ok", name)
        b.close()

if __name__ == "__main__":
    pairs = [(n, list_post(k, t, i)) for n, k, t, i in POSTS]  # compare_post() made 2026-10-26-uk-vs-eu
    render(pairs)
