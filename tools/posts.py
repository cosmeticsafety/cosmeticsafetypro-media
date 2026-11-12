import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from theme import CSS, MOTIF, WHATSAPP, SITE, theme_css

OUT = os.path.join(os.path.dirname(__file__), "..", "posts")
os.makedirs(OUT, exist_ok=True)

POSTS = [
 ("2026-11-13-eu-microplastics-timeline", "⚡ Regulatory update · EU", "EU microplastics ban: your <em>deadlines</em> by product type",
  ["Rinse-off cosmetics: can be sold until 16 Oct 2027",
   "Leave-on cosmetics: can be sold until 16 Oct 2029",
   "Make-up, lip and nail products: can be sold until 16 Oct 2035",
   "Make-up, lip and nail: microplastics label needed from 17 Oct 2031",
   "Covers synthetic polymer microparticles added on purpose (Reg. (EU) 2023/2055)"]),
 ("2026-11-14-label-items-besides-inci", "Labelling · Article 19", "6 label items you need <em>besides</em> the INCI list",
  ["Responsible Person name and address (plus country of origin if imported)",
   "Nominal content (weight or volume)",
   "Minimum durability date, or PAO if durability is over 30 months",
   "Precautions for use and warnings",
   "Batch number or other product reference",
   "Function, unless it is obvious from the product"]),
 ("2026-11-15-colourants-annex-iv", "Ingredients · Annex IV", "Colourants: only <em>Annex IV</em> colours are allowed",
  ["Colorants not listed in Annex IV cannot be used (hair dyes follow separate rules)",
   "Annex IV sets the conditions of use for each listed colorant",
   "Check every supplier’s CI number against the Annex before you formulate",
   "On the label, colorants may follow the other ingredients, named by CI number",
   "Make-up with several shades: add “may contain” or “+/-”"]),
 ("2026-11-16-spf-sun-care-claims", "Sun care · EU claims rules", "Selling sunscreen? Your <em>SPF claims</em> have rules",
  ["Show the protection level: low, medium, high or very high",
   "A protection claim needs at least SPF 6, with UVA protection of one third of the SPF",
   "Never claim “100% protection”, “sunblock” or “total protection”",
   "Add advice: limit time in the sun, keep babies out of direct sunlight",
   "Tell users to apply before exposure and to reapply often"]),
 ("2026-11-17-banned-vs-restricted-ingredients", "Ingredients · Annexes II &amp; III", "Banned vs restricted: <em>check both lists</em> before launch",
  ["Annex II = prohibited substances: they cannot be in your product",
   "Annex III = restricted: allowed only within the listed limits and conditions",
   "Check every ingredient and every supplier raw material against both",
   "The lists change: Regulation (EU) 2026/909 added new bans and limits in 2026",
   "Your Responsible Person is accountable for compliance"]),
 ("2026-11-18-handmade-cosmetics-same-rules", "Small brands · UK &amp; EU", "Handmade or small-batch? <em>Same rules</em> apply",
  ["The rules cover every cosmetic supplied commercially, even free ones",
   "A safety assessment (CPSR) by a qualified assessor before you sell",
   "A Responsible Person established in the UK (or EU/NI for those markets)",
   "Notify your product before sale (SCPN in GB, CPNP in the EU)",
   "Keep your PIF for 10 years after the last batch is sold"]),
 ("2026-11-19-candles-diffusers-clp", "Home fragrance · UK &amp; EU", "Candles and diffusers are <em>not cosmetics</em>",
  ["No cosmetic CPSR, PIF or SCPN/CPNP notification applies",
   "They are mixtures, so CLP hazard labelling rules apply",
   "Sensitiser ingredients at 0.1% or more trigger CLP label statements",
   "General product safety law applies: no unnecessary risk in normal use",
   "Candle standards (BS EN 15426, 15493, 15494) help show due diligence in the UK"]),
 ("2026-11-20-free-from-hypoallergenic-claims", "Claims · EU guidance", "“Free-from” and “hypoallergenic”: <em>what you can claim</em>",
  ["No “preservative free” on a product that would not contain one anyway",
   "“Fragrance free” fails if any perfuming ingredient is present",
   "“Allergen free” is not allowed: zero allergy risk cannot be guaranteed",
   "“Hypoallergenic” needs a product designed to minimise allergenic potential, with robust evidence",
   "Do not put down ingredients that are legally used"]),
 ("2026-11-21-who-can-sign-safety-assessment", "CPSR · Article 10", "Who can <em>legally sign</em> your safety assessment?",
  ["Every product needs a safety assessment before it is placed on the market",
   "It must be carried out by a qualified person",
   "Qualification: a diploma in pharmacy, toxicology, medicine or a similar discipline",
   "Ask to see your assessor’s credentials before you pay",
   "Keep the signed CPSR in your Product Information File"]),
 ("2026-11-22-selling-online-uk-eu", "E-commerce · UK &amp; EU", "Selling online to UK and EU buyers? <em>Both</em> have rules",
  ["Online sales count as selling on that market, just like a shop",
   "Shipping from abroad and targeting UK or EU buyers brings you under the rules",
   "GB needs a UK-based Responsible Person, the EU needs an EU-based one",
   "Notify on SCPN for GB and on CPNP for the EU and Northern Ireland",
   "Label details must be in the language required where you sell"]),
 ("2026-11-23-natural-does-not-mean-safe", "Claims · UK &amp; EU", "“Natural” does not mean <em>safe</em>",
  ["“Natural” and “organic” have no legal definition in EU or UK cosmetics rules",
   "Natural ingredients have no built-in safety advantage, and claiming one may mislead",
   "Every cosmetic follows the same safety rules, natural or not",
   "Certification for natural claims is not a legal requirement",
   "Natural brands still need a CPSR, a PIF and notification"]),
 ("2026-11-24-scpn-step-by-step", "UK · SCPN", "Notifying in the UK: <em>SCPN</em> step by step",
  ["First: a UK Responsible Person and a completed safety assessment",
   "Open the Submit cosmetic product notification (SCPN) service on GOV.UK",
   "Enter category, product name, Responsible Person and where the PIF is kept",
   "Add any CMR 1A/1B substances (CAS/EC numbers), the label and a pack photo",
   "Nanomaterials: notify 6 months before sale. Update SCPN if anything changes"]),
 ("2026-11-25-northern-ireland-cosmetics", "Northern Ireland · Windsor Framework", "Selling in Northern Ireland? <em>EU</em> cosmetic rules apply",
  ["NI follows EU Regulation 1223/2009 under the Windsor Framework",
   "Notify your product on the EU portal (CPNP)",
   "Your Responsible Person must be in NI or the EU, not in Great Britain",
   "Also selling in Great Britain? Notify on SCPN as well",
   "Bringing goods from GB into NI makes the NI importer the Responsible Person"]),
 ("2026-11-26-gift-sets-advent-calendars", "Gift season · EU", "Gift sets and advent calendars: <em>label every item</em>",
  ["Sets are usually “marketing kits”: each product is notified separately",
   "Each product keeps its own label: brand, function, RP, origin, PAO, batch",
   "The outer box must show full details for every product, ingredients and warnings included",
   "Items under 5 ml or 5 g can omit the nominal quantity",
   "National language rules still apply"]),
 ("2026-11-27-safety-gate-recalls", "Enforcement · EU Safety Gate", "Cosmetics top the EU <em>Safety Gate</em> alert list",
  ["2025: 4,671 alerts, the most since 2003, and 36% were cosmetics",
   "Think your product is non-compliant? Act at once: correct, withdraw or recall",
   "Risk to health? Tell the authorities promptly with the corrective steps taken",
   "Authorities can order a withdrawal or recall within a set time limit",
   "Keep your PIF ready: you must provide documents on request"]),
 ("2026-11-28-eu-reg-2026-909-tpp-ban", "⚡ Regulatory update · EU", "EU Regulation 2026/909: <em>TPP banned</em>, new ingredient limits",
  ["Triphenyl phosphate (TPP) is now banned in cosmetics",
   "New or stricter limits for benzyl salicylate and aluminium compounds",
   "Affected products cannot be placed on the EU market from 1 Jan 2027",
   "Most affected products must be off shelves by 1 Jul 2028",
   "Check formulas and supplier specs now: in force since 18 May 2026"]),
 ("2026-11-29-importer-duties", "Importing · UK &amp; EU", "Importing cosmetics? <em>You</em> become the Responsible Person",
  ["An importer placing a product on the market is the Responsible Person",
   "Or appoint a Responsible Person in writing, who must accept in writing",
   "Before selling: safety assessment (CPSR) done and PIF ready",
   "Check labels, including the language required where you sell",
   "Non-compliant product? Correct, withdraw or recall it at once"]),
 ("2026-11-30-launch-checklist-2027", "Checklist · UK &amp; EU", "Launching in 2027? Your <em>7-step</em> checklist",
  ["Check every ingredient against Annexes II to VI",
   "Get a CPSR from a qualified safety assessor",
   "Build your PIF and keep it for 10 years",
   "Label it: Article 19 items, ingredient list, local language",
   "Appoint a Responsible Person in each market",
   "Notify before sale: SCPN (GB) and/or CPNP (EU, NI)",
   "Report serious undesirable effects; recall if needed"]),
]

def page_html(body, w, h, name):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{theme_css(name)}</style></head>
<body><div class="frame" style="width:{w}px;height:{h}px">{body}</div></body></html>"""

def list_post(kicker, title, items):
    n = len(items)
    rows = "".join(f'<div class="item" style="padding:{12 if n>6 else 20 if n>4 else 26}px 30px"><div class="num" style="width:56px;height:56px;font-size:28px">{i+1}</div>'
                   f'<div class="itext" style="font-size:{31 if n>4 else 34}px">{t}</div></div>' for i, t in enumerate(items))
    return f"""<div class="motif">{MOTIF}</div>
<div style="position:relative;height:100%;padding:80px 84px 70px;display:flex;flex-direction:column;gap:36px">
 <div class="brand"><div><span class="dot"></span>COSMETIC SAFETY PRO</div><div class="pill">UK · EU</div></div>
 <div style="display:flex;flex-direction:column;gap:26px;margin-top:14px">
  <div class="kicker">{kicker}</div>
  <h1 style="font-size:{74 if len(title)>60 else 82}px;max-width:900px">{title}</h1>
 </div>
 <div class="items" style="gap:{10 if n>6 else 16 if n>4 else 20}px">{rows}</div>
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
