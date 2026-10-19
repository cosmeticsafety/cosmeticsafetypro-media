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
}

def theme_css(name):
    bg, card, ink, acc = THEMES[name[:10]]
    return (f":root{{--bg:{bg};--bg2:{card};--ink:{ink};--mint:{acc};--mute:{_rgba(ink,.72)};--line:{_rgba(acc,.28)}}}"
            ".motif svg,#mot svg{stroke:var(--mint)}")
