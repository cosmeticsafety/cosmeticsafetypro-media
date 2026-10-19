import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF, WHATSAPP, SITE, theme_css

OUT = os.path.join(os.path.dirname(__file__), "..", "posts")
os.makedirs(OUT, exist_ok=True)

POSTS = [
 ("2026-10-20-etsy-cpsr", "FAQ · Small brands", "Selling on Etsy or Amazon? You still need a <em>CPSR</em>.",
  ["Required for every cosmetic sold in the UK &amp; EU", "Same rules for kitchen-table makers and global brands",
   "Free, confidential formula review", "Express reports in 24–48 hours"]),
 ("2026-10-21-cpnp", "EU market · CPNP", "Notify the <em>CPNP</em> before you sell in the EU.",
  ["Product name and category", "EU Responsible Person details", "Frame formulation or exact composition",
   "Label and packaging artwork", "Any nanomaterials or CMR substances"]),
 ("2026-10-22-pif", "Checklist · PIF", "What goes inside your <em>Product Information File</em>?",
  ["Product description", "Cosmetic Product Safety Report (CPSR)", "Manufacturing method + GMP statement",
   "Proof of label claims", "Animal testing data"]),
 ("2026-10-23-benefits", "Safety assessment", "5 reasons your brand needs a <em>safety assessment</em>.",
  ["Legal access to UK &amp; EU markets", "Consumer safety, checked by a qualified assessor", "Product liability insurance cover",
   "Retailer and marketplace approval", "Fewer recalls, fines and relabels"]),
 ("2026-10-24-scpn", "Great Britain · SCPN", "Selling in Great Britain? Notify via <em>SCPN</em>.",
  ["EU CPNP does not cover England, Scotland, Wales", "A UK-based Responsible Person is required",
   "A valid CPSR must be in place", "Notify before the product goes on sale"]),
 ("2026-10-25-rp", "Responsible Person", "What does a <em>Responsible Person</em> actually do?",
  ["Ensures a valid CPSR is in place", "Holds and maintains the PIF", "Notifies via CPNP / SCPN",
   "Checks label compliance", "Reports serious undesirable effects"]),
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
    pairs = [(n, list_post(k, t, i)) for n, k, t, i in POSTS] + [("2026-10-26-uk-vs-eu", compare_post())]
    render(pairs)
