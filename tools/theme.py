CSS = r"""
:root{--bg:#0F2E28;--bg2:#163C34;--ink:#F4EFE4;--mint:#8FD9BC;--mute:#B9CCC4;--line:rgba(143,217,188,.22)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--bg);color:var(--ink);font-family:'Inter Display','Inter',sans-serif;-webkit-font-smoothing:antialiased}
.frame{position:relative;overflow:hidden;background:var(--bg)}
.motif{position:absolute;right:-230px;top:150px;width:560px;opacity:.28}
.motif2{position:absolute;left:-160px;bottom:-140px;width:520px;opacity:.35;transform:rotate(18deg)}
.brand{display:flex;justify-content:space-between;align-items:center;font-weight:700;letter-spacing:.22em;font-size:24px;color:var(--mint)}
.brand .dot{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--mint);margin-right:14px;vertical-align:middle}
.pill{border:2px solid var(--mint);color:var(--mint);border-radius:999px;padding:8px 20px;font-size:20px;letter-spacing:.14em}
.kicker{font-weight:700;letter-spacing:.24em;font-size:26px;color:var(--mint);text-transform:uppercase}
h1{font-weight:800;letter-spacing:-.025em;line-height:1.02;color:var(--ink)}
h1 em{font-style:normal;color:var(--mint)}
.items{display:flex;flex-direction:column}
.item{display:flex;align-items:center;gap:26px;background:var(--bg2);border:1.5px solid var(--line);border-radius:22px}
.num{flex:none;display:flex;align-items:center;justify-content:center;border-radius:50%;background:var(--mint);color:var(--bg);font-weight:800}
.itext{font-weight:500;color:var(--ink);line-height:1.2}
.footer{display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid var(--line);padding-top:30px;font-size:26px;color:var(--mute)}
.footer b{color:var(--ink);font-weight:700}
.cta{background:var(--mint);color:var(--bg);font-weight:800;border-radius:999px;padding:16px 30px;font-size:26px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.col{background:var(--bg2);border:1.5px solid var(--line);border-radius:24px;padding:36px}
.col h3{font-size:40px;font-weight:800;margin-bottom:24px}
.row{border-top:1.5px solid var(--line);padding:18px 0}
.row small{display:block;font-size:20px;letter-spacing:.16em;color:var(--mint);font-weight:700;margin-bottom:6px}
.row span{font-size:30px;font-weight:600}
.same{margin-top:24px;background:var(--mint);color:var(--bg);border-radius:24px;padding:28px 36px;font-size:30px;font-weight:600;line-height:1.3}
.same b{font-weight:800}
"""

# hexagonal molecule outline motif (cosmetic chemistry)
MOTIF = """<svg viewBox="0 0 400 400" fill="none" stroke="currentColor" style="color:var(--mint)" stroke-width="3" aria-hidden="true">
<polygon points="200,60 270,100 270,180 200,220 130,180 130,100" opacity=".9"/>
<polygon points="270,180 340,220 340,300 270,340 200,300 200,220" opacity=".6"/>
<line x1="130" y1="100" x2="70" y2="60"/><line x1="200" y1="220" x2="200" y2="300" opacity=".0"/>
<line x1="130" y1="180" x2="70" y2="220"/><line x1="340" y1="300" x2="390" y2="340" opacity=".6"/>
<circle cx="70" cy="60" r="12"/><circle cx="70" cy="220" r="12"/><circle cx="390" cy="340" r="10" opacity=".6"/>
<polygon points="200,90 244,115 244,165 200,190 156,165 156,115" opacity=".35"/>
</svg>"""

WHATSAPP = "+44 7868 737497"
SITE = "cosmeticsafetypro.com"

def _rgba(h, a):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) for i in (0, 2, 4)); return f"rgba({r},{g},{b},{a})"

# one theme per day: (bg, card, ink, accent)
THEMES = {
 "2026-10-19": ("#0F2E28", "#163C34", "#F4EFE4", "#8FD9BC"),  # forest + mint
 "2026-10-20": ("#13233F", "#1C3157", "#F6F1EA", "#FF8A65"),  # navy + coral
 "2026-10-21": ("#F4EFE4", "#FFFFFF", "#1E2A28", "#2F7A5F"),  # cream + green
 "2026-10-22": ("#2B1630", "#3A2140", "#F7EEF2", "#F2A7C3"),  # plum + pink
 "2026-10-23": ("#F8E7E1", "#FFF6F2", "#3A1F1D", "#B84A3A"),  # blush + terracotta
 "2026-10-24": ("#1A1A1A", "#262626", "#F5F0E6", "#E7C26B"),  # charcoal + gold
 "2026-10-25": ("#0E3B47", "#134B59", "#EEF7F7", "#7FE0E0"),  # ocean + aqua
 "2026-10-26": ("#ECE8F7", "#FFFFFF", "#231C3D", "#5B45C2"),  # lavender + violet
 "2026-10-27": ("#1F2933", "#2A3742", "#F2F5F7", "#B8E35A"),  # slate + lime (post: Omnibus VI)
 "2026-10-28": ("#F5EEDC", "#FFFBF1", "#2E2416", "#9A6B1F"),  # champagne + bronze (post: perfume launch)
 "2026-10-29": ("#3B0764", "#4C1D95", "#FAF5FF", "#FCD34D"),  # violet + sunflower (post: claims)
 "2026-10-30": ("#FFF7CC", "#FFFDF0", "#1F2A12", "#4D7C0F"),  # lemon + olive (post: PFHxA)
 "2026-10-31": ("#134E4A", "#1B5F5A", "#F0FDFA", "#F9A8D4"),  # teal + candy pink (post: shelf life)
 "2026-11-01": ("#F7EEF6", "#FFFFFF", "#1E1B2E", "#C026D3"),  # pink-grey + magenta (post: nano)
 "2026-11-02": ("#E9F2F7", "#FFFFFF", "#0F2A3D", "#0E7490"),  # ice + petrol (post: formula change, posted 3 Nov 13:00)
 "2026-11-03": ("#EDEAE4", "#FFFFFF", "#1F1A24", "#7A3E9D"),  # stone + amethyst (post: SUE reporting)
 "2026-11-04": ("#E8EEE6", "#FFFFFF", "#1B2A41", "#1E3A8A"),  # pale sage + navy (post: animal testing ban)
 "2026-11-05": ("#FBF6E9", "#FFFFFF", "#12302F", "#0F5E63"),  # buttercream + deep teal (post: INCI list rules)
 "2026-11-06": ("#FFF1E6", "#FFFFFF", "#2B1B14", "#C2410C"),  # peach + burnt orange (post: GMP / ISO 22716)
 "2026-11-07": ("#FAF3DC", "#FFFFFF", "#2A2410", "#047857"),  # pale gold + emerald (post: fragrance allergens 80+)
 "2026-11-08": ("#E6F1FB", "#FFFFFF", "#10253B", "#B91C1C"),  # sky + crimson (post: CPSR Part A/B)
 "2026-11-09": ("#F7EFE8", "#FFFFFF", "#2A1418", "#9F1239"),  # linen + burgundy (post: EU retinol limits)
 "2026-11-10": ("#16213E", "#1F2D52", "#F2F4FA", "#A5B4FC"),  # indigo + periwinkle (post: IFRA 52nd Amendment)
 "2026-11-11": ("#FDF0F0", "#FFFFFF", "#1F1416", "#166534"),  # pale rose + forest green (post: UK TPO/4-MBC ban)
 "2026-11-12": ("#F3EDE2", "#FFFFFF", "#141B2D", "#1D4ED8"),  # oat + cobalt (post: stability & challenge testing)
 "2026-11-13": ("#E8F5EF", "#FFFFFF", "#10291F", "#0F7A55"),  # mint + emerald (update)
 "2026-11-14": ("#EAF4FB", "#FFFFFF", "#0F2A3D", "#9D174D"),  # sky mist + berry (post: label items)
 "2026-11-15": ("#FFF1E0", "#FFFFFF", "#2B1A0E", "#0F766E"),  # apricot + teal (post: colourants Annex IV)
 "2026-11-16": ("#FFF6D6", "#FFFFFF", "#2A2410", "#6D28D9"),  # sun yellow + purple (post: SPF claims)
 "2026-11-17": ("#ECEFF3", "#FFFFFF", "#141B2D", "#B45309"),  # cool grey + ochre (post: Annex II/III)
 "2026-11-18": ("#FCE8EF", "#FFFFFF", "#3A1424", "#1E6B52"),  # petal pink + pine (post: handmade)
 "2026-11-19": ("#EAF2E3", "#FFFFFF", "#1C2B14", "#9333EA"),  # pale fern + orchid (post: candles CLP)
 "2026-11-20": ("#FFEFE8", "#FFFFFF", "#2D1810", "#0369A1"),  # shell + ocean blue (post: free-from claims)
 "2026-11-21": ("#F1EEFB", "#FFFFFF", "#1F1B38", "#A16207"),  # wisteria + antique gold (post: assessor)
 "2026-11-22": ("#E6F4F1", "#FFFFFF", "#0F2A26", "#C2255C"),  # sea glass + cherry (post: online selling)
 "2026-11-23": ("#F6F0E4", "#FFFFFF", "#2A2112", "#3F6212"),  # parchment + moss (post: natural)
 "2026-11-24": ("#E9EEF9", "#FFFFFF", "#121A33", "#E11D48"),  # periwinkle mist + rose red (post: SCPN)
 "2026-11-25": ("#F5EDE6", "#FFFFFF", "#2B1B14", "#155E75"),  # almond + deep cyan (post: Northern Ireland)
 "2026-11-26": ("#FFF3E6", "#FFFFFF", "#2B1A10", "#B91C1C"),  # warm cream + festive red (post: gift sets)
 "2026-11-27": ("#E8F1F5", "#FFFFFF", "#0F2733", "#7E22CE"),  # frost + grape (post: Safety Gate)
 "2026-11-28": ("#F3F7E8", "#FFFFFF", "#1E2A12", "#BE123C"),  # pale pistachio + raspberry (update: Reg 2026/909)
 "2026-11-29": ("#FBEFE4", "#FFFFFF", "#2A1A10", "#0B7285"),  # sand peach + lagoon (post: importer)
 "2026-11-30": ("#EEF6EF", "#FFFFFF", "#12291A", "#A21CAF"),  # soft mint + fuchsia (post: 2027 checklist)
}

# Reels get their OWN palette per day, different from that day's post (rule from 21 Oct 2026)
REEL_THEMES = {
 "2026-10-22": ("#E3EEE4", "#FFFFFF", "#1F3B2C", "#2F7A4F"),  # sage + leaf green
 "2026-10-23": ("#073B3A", "#0B4F4D", "#F2F7F5", "#F2C14E"),  # deep teal + saffron
 "2026-10-24": ("#E6F1FB", "#FFFFFF", "#0B2545", "#1E6FD9"),  # sky + cobalt
 "2026-10-25": ("#F6EAD7", "#FFF8EE", "#3B2A1A", "#B4541A"),  # sand + rust
 "2026-10-26": ("#3A0D16", "#521421", "#FBEFF1", "#FF9AA9"),  # wine + rose
 # paused English update reels keep their original palettes (moved here from THEMES on 25 Oct)
 "2026-10-27": ("#141414", "#222222", "#F7F3E8", "#FFD23F"),  # ink + yellow (update reel, paused)
 "2026-10-30": ("#0B1F3A", "#132C50", "#F3F6FB", "#6FB1FF"),  # midnight + sky (update reel, paused)
 "2026-11-03": ("#2A1A12", "#3A251A", "#F6EDE3", "#E3A86B"),  # espresso + amber (IFRA 52 update reel, paused; moved from THEMES 2 Nov)
 # English reels 19-29 Nov 2026 (dark backgrounds; posts use light ones)
 "2026-11-19": ("#2C1E4A", "#3B2A5E", "#F6F2FF", "#7EE8FA"),  # grape + ice cyan (supplier documents)
 "2026-11-20": ("#101828", "#1B2740", "#F3F6FB", "#FF7A45"),  # slate navy + hot orange (fake cosmetics update)
 "2026-11-22": ("#0F3D2E", "#175240", "#F1FBF6", "#FF9FCE"),  # deep green + pink (contract manufacturer)
 "2026-11-23": ("#2E1A2B", "#432640", "#FBF1F9", "#A7F3D0"),  # plum-brown + mint (EU green claims update)
 "2026-11-25": ("#33280A", "#473813", "#FFF9E6", "#93C5FD"),  # dark ochre + baby blue (children under 3)
 "2026-11-26": ("#1E1B4B", "#2B2766", "#F2F1FF", "#FCA5A5"),  # navy-violet + salmon (CPSR red flags)
 "2026-11-28": ("#0C1B2A", "#14293F", "#F1F6FB", "#FDBA74"),  # deep marine + apricot (exposure)
 "2026-11-29": ("#1E293B", "#2A3A52", "#F4F7FB", "#FCD34D"),  # blue-grey + yellow (samples/testers)
}

def theme_css(name, reel=False):
    key = name[:10]
    bg, card, ink, acc = (REEL_THEMES if reel and key in REEL_THEMES else THEMES)[key]
    return (f":root{{--bg:{bg};--bg2:{card};--ink:{ink};--mint:{acc};--mute:{_rgba(ink,.72)};--line:{_rgba(acc,.28)}}}"
            ".motif svg,#mot svg{stroke:var(--mint)}")
