# Instagram content log — @cosmeticsafetypro
Posts 18:00 Asia/Karachi, reels 20:00 Asia/Karachi. Metricool brand id 7514762.
Media public URL base: https://raw.githubusercontent.com/cosmeticsafety/cosmeticsafetypro-media/main/

## Blogs already turned into posts
- Why Cosmetic Product Safety Report Essential for Cosmetics? (posted by owner)
- Cosmetic Product Notification Portal (CPNP) Explained (21 Oct)
- Top 10 Benefits of Cosmetic Product Safety Assessment (23 Oct)
- Cosmetic Safety Solutions for UK and EU Compliance (26 Oct)

## Themes used (bg / accent)
- 19 Oct forest+mint, 20 navy+coral, 21 cream+green, 22 plum+pink, 23 blush+terracotta, 24 charcoal+gold, 25 ocean+aqua, 26 lavender+violet
- Posts 27 Oct slate+lime, 28 champagne+bronze, 29 violet+sunflower, 30 lemon+olive, 31 teal+candy pink, 1 Nov pink-grey+magenta
- Reels: 22 sage+leaf, 23 deep teal+saffron, 24 sky+cobalt, 25 sand+rust, 26 wine+rose; paused English update reels keep ink+yellow (27 Oct) and midnight+sky (30 Oct) — moved to REEL_THEMES on 25 Oct. Language reels (lang_reels.py) use navy+green / light grey+teal.

## Topics used
Posts: Etsy/Amazon need CPSR; CPNP notification; PIF contents; 5 benefits of safety assessment; SCPN for GB; Responsible Person duties; UK vs EU at a glance
Posts week 27 Oct–1 Nov (English reels paused; image posts only): 27 Omnibus VI approved by EP (update); 28 perfume launch checklist; 29 6 common criteria for claims; 30 PFHxA limits apply (update); 31 PAO vs best-before; 1 Nov nanomaterial 6-month notification
Reels: 3 things before selling in UK; Etsy myth vs fact; CPNP in 4 steps; PIF audit-ready; label compliance checklist; SCPN vs CPNP; what is a Responsible Person; how long a CPSR takes

## Weekly reel mix (from week of 27 Oct 2026)
Each week's 7 reels = 2–3 "Regulatory update" reels (cosmetics AND perfume/fragrance news) + 4–5 general tip reels. Update reels use the NEWS list in tools/reels.py (6th field = source line shown on screen; kicker starts with "⚡ Regulatory update · EU/UK" or "⚡ Perfume update · IFRA"). Re-verify every fact with a web search before using; drop items that are outdated.

## English reels paused until 17 Nov 2026
Multi-language reel series runs instead (reels/lang/). Rendered-but-unscheduled English NEWS reels (27 Oct allergens-81, 30 Oct 4-MBC/TPO, 3 Nov IFRA 52, 6 Nov retinol, 10 Nov Omnibus VI, 13 Nov microplastics) need new dates when reels resume on 18 Nov; Omnibus VI reel text must be updated (EP final vote 22 Oct 2026) and PFHxA/Omnibus were already used as posts 27/30 Oct.

## Regulatory update backlog (researched 19 Oct 2026; re-verify before use)
- UPDATE 25 Oct 2026: Omnibus VI — EP final plenary approval 22 Oct 2026 (477/59/41). Staggered CMR timelines replace 18-month withdrawal: no exemption sought 6 months stop placing / 12 months sell-out; unsafe 3/9 months; safe but alternatives exist 2/3 years. Next: Council formal adoption, OJ, in force +20 days. (Premium Beauty News 23 Oct; Agence Europe.) Watch for Council adoption/OJ publication.
- UPDATE 25 Oct 2026: PFHxA (Reg (EU) 2024/2462) applies to cosmetics from 10 Oct 2026 — confirmed (Personal Care Insights 9 Oct 2026). Used as post 30 Oct.
- EU fragrance allergens: Reg (EU) 2023/1545 adds 56 allergens (total 81). Label above 0.001% leave-on / 0.01% rinse-off. New units placed on EU market from 31 Jul 2026 must comply; non-compliant stock already on market may be sold until 31 Jul 2028.
- UK annex amendments (SI published 15 Jan 2026): 4-MBC banned (placing 15 Jul 2026, making available 14 Jan 2027); 16 CMRs incl. TPO (gel nails) banned (placing 15 Aug 2026, making available 14 Feb 2027); "releases formaldehyde" warning above 0.001% (15 Jul 2026 / 14 Jan 2027). Source: CTPA / OPSS.
- IFRA 52nd Amendment: consultation closed 12 Jun 2026, End of Consultation Letter 31 Aug 2026, Notification expected Jan 2027; new creations 11 months after notification, existing creations 30 months after; 48 new dermal sensitisation restriction standards; furocoumarins in NCS standard (1 ppm sun-exposure / 5 ppm other leave-on). Source: ifrafragrance.org.
- EU retinol / vitamin A, Reg (EU) 2024/996: max 0.3% RE face & hand, 0.05% RE body lotion; new products from 1 Nov 2025; off shelves by 1 May 2027; vitamin A intake warning on label. Not applicable in GB.
- EU Omnibus VI (political agreement June 2026, formal adoption pending at that time — check status): CMR ban kept; withdrawal 6 months stop placing / 12 months full withdrawal; 12 months to request derogation; nanomaterial prior notification kept.
- EU microplastics, Reg (EU) 2023/2055: rinse-off Oct 2027; leave-on Oct 2029; make-up/lip/nail Oct 2035, with microparticle labelling for those from Oct 2031.
- EU PFAS (PFHxA) REACH restriction: transitional period ended 10 Oct 2026 for relevant uses (25 ppb PFHxA / 1000 ppb related substances) — verify cosmetics scope before using.

## Reel audio (from 20 Oct 2026)
Every reel must have background music. tools/reels.py calls tools/music.py automatically (original procedurally generated music, royalty-free; needs numpy + scipy — `pip install numpy scipy` if missing). After rendering, confirm each mp4 has an audio stream (`ffprobe -show_streams`) and mean volume around -16 dB (`ffmpeg -af volumedetect`). 19 Oct reel went out silent; 20–26 Oct reels were replaced with *-music.mp4 versions.

## Rule: post and reel on the same day must cover DIFFERENT topics (from 20 Oct 2026)
On 20 Oct the post and reel were both about Etsy/CPSR; user asked that this never repeat. When planning a week, check each day's post topic vs reel topic (and YouTube Short) and make sure they don't overlap (e.g. never PIF post + PIF reel, CPNP post + CPNP reel, SCPN post + SCPN-vs-CPNP reel).
21–25 Oct reels were reshuffled: 21 label checklist, 22 CPNP 4 steps, 23 SCPN vs CPNP, 24 Responsible Person, 25 PIF audit-ready.

## Rule: post and reel on the same day must ALSO look different (from 21 Oct 2026)
User saw a post and reel on the same day in the same colour theme and asked that this not happen. Posts use THEMES[date]; reels use REEL_THEMES[date] (tools/theme.py, `theme_css(name, reel=True)`). Each week, fill BOTH dicts with 7 entries each, all 14 palettes distinct (no reel palette may match or closely resemble the same day's post palette). 22–26 Oct reels were re-rendered as *-r.mp4 with their own palettes.

## Blog check
- 25 Oct 2026: WebFetch of cosmeticsafetypro.com/blogs/ was not permitted (permission request timed out in unattended run); no new blog used this week. Retry next run.

## Networks (from 26 Oct 2026) — Metricool Pro
Every image post and reel goes to Instagram + Facebook + LinkedIn in ONE Metricool post (facebookData type POST/REEL; linkedinData type post). YouTube Shorts stay separate. Captions use the full URL https://cosmeticsafetypro.com (no "link in bio").
26 Oct: back-filled all earlier Instagram content (6 posts 20–25 Oct + reels 19–23 Oct, fr, de) to Facebook + LinkedIn, 15:15–21:15 every 30 min. All queued IG posts/reels (26 Oct–17 Nov) got FB + LinkedIn added.
Language reels: intro scene is fully visible from frame 0 (no fade from black) so auto thumbnails aren't black. it re-rendered 26 Oct; es/nl/pt due 27 Oct; de was posted manually with the old version.

## European language reel series — remaining schedule (one language per day, local midday)
Posting time (Asia/Karachi): CET countries 16:00, EET countries 15:00.
30 Oct pl (pl_PL-gosia-medium, CET) · 31 Oct sv (sv_SE-alma-medium, CET) · 1 Nov da (da_DK-talesyntese-medium, CET) · 2 Nov fi (fi_FI-harri-medium, EET) · 3 Nov cs (cs_CZ-jirka-medium, CET) · 4 Nov sk (sk_SK-lili-medium, CET) · 5 Nov hu (hu_HU-anna-medium, CET) · 6 Nov ro (ro_RO-mihai-medium, EET) · 7 Nov bg (bg_BG-dimitar-medium, EET) · 8 Nov el (el_GR-rapunzelina-medium, EET) · 9 Nov hr (NO Croatian Piper voice — owner to decide; until then text + music only, no voiceover) · 10 Nov sl (sl_SI-artur-medium, CET) · 11 Nov lt (lt_LT-ingute-medium, EET) · 12 Nov lv (lv_LV-aivars-medium, EET) · 13 Nov et (et_EE-news-medium, EET) · 14 Nov no (no_NO-talesyntese-medium, CET).
How to build one: add the language to LANGS in tools/lang_content.py (same 4-scene structure as fr/de; natural native translation; keep 35–45 s), add a unique (dark, light) palette to PALETTES in tools/lang_reels.py, download the voice with `PIPER_DIR=piper tools/get_piper_voice.sh <voice>` (needs `pip install piper-tts kokoro-onnx soundfile scipy numpy --break-system-packages`), then `PIPER_DIR=piper python3 tools/lang_reels.py /tmp/none <code>`. Check duration 35–45 s and that frame 0 is not black.
Schedule each language reel as ONE Metricool post to instagram (REEL, isAiGenerated true) + facebook (REEL) + linkedin, plus a separate YouTube Short (isAiGeneratedContent true, madeForKids false, category EDUCATION). Captions in that language, same structure as the it/es/nl/pt captions (checklist + WhatsApp + https://cosmeticsafetypro.com + local hashtags ending #CosmeticSafetyPro).

## Daily routine (from 26 Oct 2026)
Content is created ONE DAY AHEAD only, by a daily scheduled task at ~21:35 Asia/Karachi, which reports to the owner at ~22:00.
31 Oct sv reel: deep blue + yellow, built 31 Oct 08:00
