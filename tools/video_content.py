"""Scripts for extra 16:9 narrated videos (YouTube / LinkedIn / Facebook).
    python3 tools/video.py <tts_dir> <out.mp4> <key>
Each entry: {"seed": music seed, "scenes": [(chapter, kicker, title_html, theme, [(narration, bullet or None), ...])]}
Facts verified 10 Nov 2026 (CTPA, IFRA, Reg (EU) 2023/1545, Business Companion GB CLP guide, legislation.gov.uk)."""
from theme import WHATSAPP, SITE

def _t(bg, bg2, ink, acc):
    r = lambda h, a: "rgba(%d,%d,%d,%s)" % (int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16), a)
    return ":root{--bg:%s;--bg2:%s;--ink:%s;--mint:%s;--mute:%s;--line:%s}" % (bg, bg2, ink, acc, r(ink, ".74"), r(acc, ".30"))

# perfume video: aubergine + champagne gold
PD, PL = _t("#2A1338", "#3A1D4C", "#FBF6EE", "#E8C27A"), _t("#FBF6EE", "#FFFFFF", "#2A1338", "#8A5A12")
# marketplace video: graphite + coral
MD, ML = _t("#1B1F27", "#272D38", "#F5F6F8", "#FF7A66"), _t("#F6F3F1", "#FFFFFF", "#1B1F27", "#C4372A")

_CTA = [
   ("Start with a free, confidential review of your formula.", None),
   ("Message us on WhatsApp at plus four four, seven eight six eight, seven three seven, four nine seven.", "WhatsApp " + WHATSAPP),
   ("Email info at cosmetic safety pro dot com,", "info@cosmeticsafetypro.com"),
   ("or visit cosmetic safety pro dot com. Launch legally, and sell with confidence.", SITE)]

VIDEOS = {
 "perfume": {"seed": 23, "scenes": [
  ("Introduction", "Perfume brands · UK &amp; EU", "Launching a <em>perfume</em> brand? Don't miss these steps", PD, [
    ("Launching a perfume brand in the U K or Europe?", None),
    ("A beautiful scent and a beautiful bottle are not enough. The law has its own checklist.", None),
    ("Here are the compliance steps most founders miss, and how to get them right before launch.", None)]),
  ("Perfume is a cosmetic", "Step 1", "In law, perfume is a <em>cosmetic</em>", PL, [
    ("First, the basics. In U K and E U law, perfume is a cosmetic product. So every fragrance you sell needs four things.", None),
    ("A Cosmetic Product Safety Report, signed by a qualified safety assessor.", "Cosmetic Product Safety Report (CPSR)"),
    ("A Responsible Person, based in the U K for Great Britain, and in the E U for Europe.", "Responsible Person: UK-based and / or EU-based"),
    ("A Product Information File.", "Product Information File (PIF)"),
    ("And a notification before the first sale, on the U K portal, the E U portal, or both.", "Notification before sale: SCPN (GB) · CPNP (EU)")]),
  ("IFRA certificate", "Step 2", "Ask your supplier for the <em>IFRA</em> certificate", PD, [
    ("Step two is the one most founders have never heard of: the IFRA certificate.", None),
    ("IFRA, the International Fragrance Association, sets maximum levels for fragrance ingredients in each type of product.", "IFRA Standards set maximum use levels"),
    ("Fine fragrance is category four.", "Fine fragrance = IFRA Category 4"),
    ("Ask your fragrance supplier for three documents: the IFRA certificate, the allergen declaration, and the safety data sheet.", "Ask for: IFRA certificate · allergen declaration · SDS"),
    ("Your safety assessor cannot sign off your perfume without them.", "Your safety assessor needs all three")]),
  ("Fragrance allergens", "Step 3", "Declare your <em>allergens</em> on the label", PL, [
    ("Step three: fragrance allergens.", None),
    ("In the E U, the list of allergens that must be named on the label has grown from twenty-six to more than eighty.", "EU: 26 → 80+ fragrance allergens"),
    ("Perfume is a leave-on product, so each allergen above zero point zero zero one percent must appear in your ingredient list.", "Leave-on products: label above 0.001%"),
    ("New products placed on the E U market since the thirty-first of July twenty twenty-six must already comply. Older stock can be sold until the thirty-first of July twenty twenty-eight.", "New products: since 31 Jul 2026 · old stock until 31 Jul 2028"),
    ("Great Britain has its own allergen list, so if you sell in both markets, check both.", "Great Britain has its own list: check both")]),
  ("Label requirements", "Step 4", "What your <em>label</em> must show", PD, [
    ("Step four: the label on your bottle and box. It must show:", None),
    ("the name and address of your Responsible Person,", "Responsible Person name + address"),
    ("the nominal content, in millilitres,", "Nominal content (ml)"),
    ("a batch number,", "Batch number"),
    ("the full ingredient list, including the allergens,", "Ingredient list (INCI) incl. allergens"),
    ("and any warnings from your safety report.", "Warnings from your safety report")]),
  ("Candles and diffusers", "Step 5", "Candles &amp; diffusers follow <em>different</em> rules", PL, [
    ("Step five catches many growing brands. Planning to add candles, reed diffusers or room sprays?", None),
    ("These are not cosmetics.", "Candles, diffusers, room sprays ≠ cosmetics"),
    ("They follow the chemical labelling rules, known as C L P.", "They follow CLP (chemical labelling) rules"),
    ("That can mean hazard pictograms, warning statements, and allergen statements on the label.", "Pictograms · warnings · “Contains…” allergens"),
    ("So one fragrance, in two products, needs two different kinds of label.", "One scent, two products = two kinds of label")]),
  ("Common mistakes", "Avoid these", "Three mistakes we see <em>every week</em>", PD, [
    ("Finally, three mistakes we see every week.", None),
    ("Thinking the IFRA certificate is the safety report. It is not. You need both.", "IFRA certificate ≠ safety report"),
    ("Selling before the product is notified.", "Selling before notification"),
    ("And copying the label of another brand, instead of using your own formula.", "Copying another brand's label")]),
  ("How Cosmetic Safety Pro helps", "How we help", "Perfume compliance, <em>done for you</em>", PL, [
    ("That's where Cosmetic Safety Pro comes in.", None),
    ("We prepare your safety report with a qualified safety assessor,", "CPSR by a qualified Safety Assessor"),
    ("check your IFRA documents and allergens,", "IFRA + allergen check"),
    ("act as your U K and E U Responsible Person, and handle your notifications,", "UK &amp; EU Responsible Person + notifications"),
    ("and review your perfume labels, and your candle and diffuser labels too.", "Label review: cosmetics + CLP")]),
  ("Free formula review", "Get started", "Start with a <em>free formula review</em>", PD, _CTA),
 ]},

 "marketplace": {"seed": 31, "scenes": [
  ("Introduction", "Amazon · Etsy · UK &amp; EU", "7 mistakes that get cosmetics <em>removed</em> from Amazon &amp; Etsy", MD, [
    ("Selling skincare, cosmetics or perfume on Amazon or Etsy?", None),
    ("Marketplaces can ask for your compliance documents at any time. If you cannot show them, your listing can be removed.", None),
    ("Here are seven mistakes that put your shop at risk, and how to fix each one.", None)]),
  ("1. No safety report", "Mistake 1", "No <em>safety report</em>", ML, [
    ("Mistake one: no Cosmetic Product Safety Report.", None),
    ("Every cosmetic product needs one before it is sold, in the U K and in the E U.", "Every product needs a CPSR before sale"),
    ("That includes handmade products and small batches.", "Handmade and small batch included"),
    ("And a supplier's data sheet is not a safety report.", "A supplier data sheet is not a CPSR")]),
  ("2. No Responsible Person", "Mistake 2", "No <em>Responsible Person</em> on the label", MD, [
    ("Mistake two: no Responsible Person.", None),
    ("Every cosmetic needs a Responsible Person, with their name and address on the label.", "Name + address on every label"),
    ("They must be based in the U K for Great Britain, and in the E U for Europe.", "UK-based for GB · EU-based for the EU"),
    ("If your business is outside those markets, you must appoint one.", "Selling from abroad? Appoint one")]),
  ("3. Not notified", "Mistake 3", "Product <em>not notified</em>", ML, [
    ("Mistake three: the product was never notified.", None),
    ("Before the first sale, each product must be notified on the U K portal for Great Britain,", "Great Britain → SCPN"),
    ("and on the E U portal for Europe.", "European Union → CPNP"),
    ("Selling in both markets means two notifications.", "Both markets = both notifications")]),
  ("4. Wrong ingredient list", "Mistake 4", "An incomplete <em>ingredient list</em>", MD, [
    ("Mistake four: an incomplete ingredient list.", None),
    ("Ingredients must be listed with their official I N C I names,", "Official INCI names"),
    ("in descending order of weight,", "Descending order of weight"),
    ("with fragrance allergens named above the legal thresholds.", "Fragrance allergens named"),
    ("The words natural or handmade do not remove this rule.", "“Natural” and “handmade” are not exemptions")]),
  ("5. Medical claims", "Mistake 5", "Claims that sound like <em>medicine</em>", ML, [
    ("Mistake five: medical claims.", None),
    ("Words like heals eczema, or treats acne, can turn your cosmetic into a medicine in the eyes of the regulator.", "“Heals eczema” · “treats acne” = medicinal claims"),
    ("Every claim you make must be truthful, and backed by evidence.", "Every claim needs evidence"),
    ("Claims are one of the fastest ways to get a listing flagged.", "Claims get listings flagged fast")]),
  ("6. Banned ingredients", "Mistake 6", "Banned or <em>restricted</em> ingredients", MD, [
    ("Mistake six: banned or restricted ingredients.", None),
    ("The rules keep changing. The E U now limits retinol in cosmetics,", "EU: retinol limits now apply"),
    ("and Great Britain has banned T P O, an ingredient used in gel nail products.", "GB: TPO in gel nails banned"),
    ("A formula that was legal last year may not be legal today.", "Legal last year ≠ legal today")]),
  ("7. Formula changed", "Mistake 7", "Changing the formula, <em>not the paperwork</em>", ML, [
    ("Mistake seven: changing the formula, but not the paperwork.", None),
    ("A new fragrance, a new preservative, or a new supplier can change the safety of your product.", "New fragrance · preservative · supplier"),
    ("Your safety report and Product Information File must be updated,", "Update the CPSR and the PIF"),
    ("and so must your label and your notification.", "Update the label and notification")]),
  ("How Cosmetic Safety Pro helps", "How we help", "All seven, <em>fixed for you</em>", MD, [
    ("Cosmetic Safety Pro can fix all seven for you.", None),
    ("We prepare your safety report with a qualified safety assessor,", "CPSR by a qualified Safety Assessor"),
    ("act as your U K and E U Responsible Person,", "UK &amp; EU Responsible Person"),
    ("handle your notifications and your Product Information File,", "SCPN &amp; CPNP notifications + PIF"),
    ("and review your labels and claims before a marketplace does.", "Label and claims review")]),
  ("Free formula review", "Get started", "Start with a <em>free formula review</em>", MD, _CTA),
 ]},
}
