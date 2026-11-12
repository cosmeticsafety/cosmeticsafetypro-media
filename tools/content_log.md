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
Posts week 27 Oct–1 Nov (English reels paused; image posts only): 27 Omnibus VI approved by EP (update); 28 perfume launch checklist; 29 6 common criteria for claims; 30 PFHxA limits apply (update); 31 PAO vs best-before; 1 Nov nanomaterial 6-month notification; 3 Nov SUE reporting (cosmetovigilance); 4 Nov animal testing ban; 5 Nov INCI ingredient list rules
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
1 Nov da reel: Danish red + peach (#3A0A10 / #FFB38A), 40.8 s, built 31 Oct ~21:40 PKT; IG+FB+LI 16:00 + YT Short 16:00. 1 Nov 18:00 post (nanomaterials) already existed — skipped.
31 Oct run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted (permission timed out); no blog used.
3 Nov post (18:00 IG+FB+LI): SUE reporting / cosmetovigilance (Art. 23; GB SUE form to OPSS — gov.uk) — stone + amethyst (#EDEAE4/#7A3E9D). THEMES["2026-11-03"] espresso+amber (paused IFRA 52 reel) moved to REEL_THEMES.
3 Nov cs reel: ink navy + Czech red (#12203F / #FF5C5C), 44.9 s, Piper jirka length-scale 0.74; IG+FB+LI 16:00 + YT Short 16:00. Built 2 Nov ~21:45 PKT.
2 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used.
2 Nov fi reel: missed (task was off 1 Nov). Video exists in reels/lang/ (built by a catch-up session) but NOT scheduled by the routine — owner to decide.
2 Nov 18:00 post missed (task off); replacement post 'Changed your formula? Update these' (ice + petrol) posted 3 Nov 13:00. Finnish reel posted 3 Nov 10:05.
9 Nov hr reel: built 3 Nov from owner-supplied TTSMaker Croatian voiceover (reels/lang/hr-voice-ttsmaker.mp3) with tools/hr_reel.py; olive + lavender; 43.5 s; scheduled 9 Nov 16:00 IG+FB+LI + YT Short. Daily task: SKIP hr, already scheduled.
4 Nov post (18:00 IG+FB+LI): animal testing ban (2004 finished / 2009 ingredients / 2013 full marketing ban; GB same — EC single-market page, legislation.gov.uk Art. 18) — pale sage + navy (#E8EEE6/#1E3A8A). Built 3 Nov ~21:40 PKT.
4 Nov sk reel: deep plum + aqua (#2B1030 / #5EEAD4), 35.5 s, Piper lili length-scale 0.8; IG+FB+LI 16:00 + YT Short 16:00. Built 3 Nov ~21:40 PKT.
3 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used.
5 Nov post (18:00 IG+FB+LI) + Pinterest pin 18:05 (Cosmetic Labelling Tips): INCI ingredient list — 5 rules (Art. 19(1)(g) Reg 1223/2009, legislation.gov.uk) — buttercream + deep teal (#FBF6E9/#0F5E63). Built 4 Nov ~21:40 PKT.
5 Nov hu reel: warm black + lime (#1C1917 / #A3E635), 40.1 s, Piper anna length-scale 0.85; IG+FB+LI+TikTok 16:00 + YT Short 16:00 + Pinterest video pin 16:10 (Cosmetic Regulations UK & EU). Built 4 Nov ~21:40 PKT.
4 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used.
6 Nov post (18:00 IG+FB+LI) + Pinterest pin 18:05 (CPSR & Safety Assessment): GMP / ISO 22716 in 5 points (Art. 8 + Art. 11(2)(c) Reg 1223/2009, legislation.gov.uk; ISO 22716 designated standard GB — gov.uk notice 1 Jan 2021) — peach + burnt orange (#FFF1E6/#C2410C). Built 5 Nov ~21:40 PKT.
6 Nov ro reel: petrol blue + rose (#0C4A6E / #FDA4AF), 42.7 s, Piper mihai length-scale 0.9; IG+FB+LI+TikTok 15:00 + YT Short 15:00 + Pinterest video pin 15:10 (Cosmetic Regulations UK & EU). Built 5 Nov ~21:40 PKT.
5 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used.
7 Nov post (18:00 IG+FB+LI) + Pinterest 18:05 (Perfume & Fragrance Compliance): EU fragrance allergens 80+ (Reg 2023/1545; 31 Jul 2026 / 31 Jul 2028; HPRA) — pale gold + emerald (#FAF3DC/#047857). Built 7 Nov ~07:50 PKT (catch-up: 6 Nov run had failed).
7 Nov bg reel: royal blue + tangerine (#1E2A78 / #FF8A3D), 40.8 s, Piper dimitar 0.9; IG+FB+LI+TikTok 15:00 + YT Short 15:00 + Pinterest 15:10.
8 Nov post (18:00 IG+FB+LI) + Pinterest 18:05 (CPSR & Safety Assessment): CPSR Part A / Part B (Annex I Reg 1223/2009) — sky + crimson (#E6F1FB/#B91C1C).
8 Nov el reel: charcoal green + peach (#1F2A1F / #FFC9A8), 41.6 s, Piper rapunzelina 0.9; IG+FB+LI+TikTok 15:00 + YT Short 15:00 + Pinterest 15:10. Daily task: 7 and 8 Nov fully done — next is 9 Nov (hr already scheduled; add post + hr Pinterest pin only).
9 Nov post (18:00 IG+FB+LI) + Pinterest 18:05 (Regulatory Updates): EU retinol limits (Reg 2024/996: 0.3% RE face/hand/other, 0.05% RE body lotion, vitamin A warning, 1 Nov 2025 / 1 May 2027 — Obelis, Cosmetics Business) — linen + burgundy (#F7EFE8/#9F1239). hr reel + Short already scheduled; added hr Pinterest video pin 16:10 (Cosmetic Regulations UK & EU). Built 8 Nov ~21:40 PKT.
8 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used. Next: 10 Nov (sl reel + IFRA 52 post).
10 Nov post (18:00 IG+FB+LI) + Pinterest 18:05 (Perfume & Fragrance Compliance): IFRA 52nd Amendment — 48 new dermal sensitisation Standards, 15 revised, furocoumarins in NCS 1 ppm/5 ppm, Notification expected Jan 2027, 11/30 months (ifrafragrance.org EoC letter 31 Aug 2026) — indigo + periwinkle (#16213E/#A5B4FC).
10 Nov sl reel: deep berry + mint (#4A0D35 / #86EFAC), 47.0 s incl. end card, Piper artur 0.9; CTA "sl" added; IG+FB+LI+TikTok 16:00 + YT Short 16:00 + Pinterest 16:10 (Cosmetic Regulations UK & EU). Built 9 Nov ~21:40 PKT.
9 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used. Next: 11 Nov (lt reel 15:00 + UK TPO/4-MBC post).
11 Nov post (18:00 IG+FB+LI) + Pinterest 18:05 (Regulatory Updates): UK bans TPO (gel nails) + 15 CMRs and 4-MBC — 4-MBC 15 Jul 2026 / 14 Jan 2027; CMRs incl. TPO 15 Aug 2026 / 14 Feb 2027; "releases formaldehyde" >0.001% 15 Jul 2026 / 14 Jan 2027 (CTPA 16 Jan 2026) — pale rose + forest green (#FDF0F0/#166534).
11 Nov lt reel: espresso + sky cyan (#241A14 / #67E8F9), 48.5 s incl. end card, Piper ingute 0.9; CTA "lt" added; IG+FB+LI+TikTok 15:00 + YT Short 15:00 + Pinterest 15:10 (Cosmetic Regulations UK & EU). Built 10 Nov ~21:50 PKT.
NOTE: lt_LT-ingute voice config says phoneme_type "lithuanian", which piper-tts 1.8.0 (latest on PyPI) does not support. Workaround: edit piper/lt_LT-ingute-medium.onnx.json to phoneme_type "espeak" (espeak voice lt; all phonemes are in the id map). Speech is intelligible (Whisper check) but may sound less natural. lv/et voices may need the same check. Owner (10 Nov): keep the Piper voice, no custom voiceover needed.
10 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ again not permitted; no blog used. Next: 12 Nov (lv reel 15:00 + stability/challenge testing post).
12 Nov post (18:00 IG+FB+LI) + Pinterest 18:05 (CPSR & Safety Assessment): stability + preservation challenge testing in the CPSR (Decision 2013/674/EU guidelines, legislation.gov.uk) — oat + cobalt (#F3EDE2/#1D4ED8). Built 11 Nov ~21:50 PKT.
12 Nov lv reel: deep moss + orchid (#1A2E05 / #F0ABFC), 47.7 s incl. end card, Piper aivars 0.8; CTA "lv" added; IG+FB+LI+TikTok 15:00 + YT Short 15:00 + Pinterest 15:10 (Cosmetic Regulations UK & EU). lv voice config already phoneme_type espeak (no workaround needed).
11 Nov run: WebFetch of cosmeticsafetypro.com/blogs/ WORKED; unused blogs: Perfume CPSR guide 2026-27, Essential steps in perfume safety assessments, SCPN guide (candidate post topics). Next: 13 Nov (et reel 15:00 + microplastics post).

## Engagement changes (owner approved 7 Nov 2026; from 9 Nov)
- Reels: hook question on screen from frame 0, voice starts within ~0.25 s (lang_reels LEAD 0.25, hr_reel PAD 0.2, no big logo on scene 0); 3.4 s end card "Save this / Follow for UK & EU rules / Free check on WhatsApp" (reels.py built in; lang_reels.py via with_end() + CTA dict — add a CTA entry for every new language).
- Captions: "📌 Save this for your launch · Follow for UK & EU cosmetic rules" line before WhatsApp. firstCommentText = one easy question (reel, Short, image post; never Pinterest). YouTube titles "<topic> | Subscribe for Weekly UK & EU Rules #Shorts" when under 100 chars; description has "🔔 Subscribe for weekly UK & EU cosmetic rules."
- Rebuilt and re-uploaded 7 Nov: 9 Nov hr reel (46.2 s) + Short; 15 Nov rp-r, 16 Nov pif-r, 17 Nov how-long-r reels + Shorts (captions, first comments, YouTube titles updated). Commit 1ad6f3b. Pinterest pins for 9 and 15–17 Nov still to be added by the daily task.
- Owner's part: pin the first-comment question on IG/TikTok/YouTube if possible and reply to comments; engage with 5–10 brand accounts a day.

## Planned image posts 9–14 Nov 2026 (owner approved 8 Nov; 18:00 IG+FB+LI + Pinterest 18:05)
Daily task: use these topics (re-verify every fact first; do not repeat). Reels 9–14 Nov stay the language series (hr, sl, lt, lv, et, no).
- 9 Nov: Retinol in the EU — Reg (EU) 2024/996 limits, new products from 1 Nov 2025, off shelves 1 May 2027 (update; Pinterest board: Regulatory Updates)
- 10 Nov: IFRA 52nd Amendment — what perfumers should prepare before Jan 2027 (update; board: Perfume & Fragrance Compliance). Re-check ifrafragrance.org for Notification date.
- 11 Nov: UK ban on TPO gel nail products and 4-MBC — deadlines (update; board: Regulatory Updates)
- 12 Nov: Stability and challenge testing — what your CPSR needs before launch (board: CPSR & Safety Assessment)
- 13 Nov: EU microplastics restriction timeline, Reg (EU) 2023/2055 (update; board: Regulatory Updates)
- 14 Nov: 6 label items besides INCI — batch number, function, PAO, warnings etc. (board: Cosmetic Labelling Tips)
Dropped: "Importing cosmetics = Responsible Person" post (covered by 15 Nov RP reel).

## Long videos (16:9, YouTube + LinkedIn + Facebook) — built 10/11 Nov 2026 on owner request, NOT yet scheduled
- videos/perfume-brand-compliance-steps.mp4 (202.9 s, aubergine + champagne gold): perfume = cosmetic, IFRA certificate (Cat. 4), allergens 80+ (31 Jul 2026 / 2028), label, candles/diffusers = CLP, 3 mistakes.
- videos/7-mistakes-amazon-etsy-cosmetics.mp4 (179.9 s, graphite + coral): no CPSR, no RP, not notified, INCI list, medicinal claims, banned ingredients, formula change.
- Scripts in tools/video_content.py; build: `python3 tools/video.py <tts_dir> <out.mp4> <key>` (Kokoro bf_emma; tts_dir = kokoro-q8.onnx joined from npm kokoro-q8-shards + voices.bin npz built from npm kokoro-js voices/*.bin).
- Owner wants extra EU-language AUDIO TRACKS for YouTube (one video, multi-language audio), not separate videos. Pending his OK on the English versions.

## Topic plan 15–30 Nov 2026 (owner approved 12 Nov) — RULE: no reel topic may match any post topic or earlier reel/post
No MoCRA/US topic (owner removed it). Re-verify every fact with official sources before use; swap the topic if it does not hold up.
Image posts 18:00 (+ Pinterest 18:05): 13 microplastics · 14 label items besides INCI · 15 Perfume CPSR (blog) · 16 SPF/sun-care claims · 17 banned vs restricted ingredients (Annex II/III) · 18 handmade products still need a CPSR · 19 candles/diffusers = CLP not cosmetics · 20 "free-from"/"hypoallergenic" claims · 21 who can legally sign a safety assessment · 22 perfume safety assessment steps (blog) · 23 "natural" ≠ safe · 24 SCPN step by step (blog) · 25 Northern Ireland: which rules apply · 26 gift sets and multipacks · 27 recalls / Safety Gate · 28 update slot (latest verified news) · 29 importer duties · 30 7-step launch checklist for 2027.
English reels 20:00 (from 18 Nov; 15–17 already scheduled: RP, PIF audit-ready, how long a CPSR): 18 cosmetic or medicine? (VERIFIED: CTPA borderline guide — function, site, composition, presentation; acne/eczema treatment = medicine; sanitisers = biocides) · 19 documents to collect from ingredient suppliers · 20 ⚡ update slot · 21 shades/variants: separate paperwork? · 22 contract manufacturer: what you stay responsible for · 23 ⚡ update slot · 24 label language rules by country (VERIFIED: Art 19(5) — language of content, durability/PAO, precautions, function set by Member State law where sold; INCI list exempt) · 25 products for children: extra safety attention · 26 3 red flags of a weak safety report · 27 ⚡ update slot · 28 OPEN SLOT (MoCRA removed): choose an evergreen topic, verify it, must not match any post/reel · 29 free samples and testers still need an ingredient list (VERIFIED: UK Business Companion — ingredient list applies to samples/testers; nominal content exempt for free samples) · 30 ⚡ update slot.
⚡ update slots: ONLY genuinely new, verified news not already used in a post/reel; otherwise replace with an evergreen tip (so ~2 update reels/week). Do not reuse the rendered news reels (allergens, IFRA 52, retinol, TPO, microplastics, Omnibus) — those topics were posts.
## EU-language reels, 2 per week (from 18 Nov; second round in the big languages) — own topics, different from every post and English reel
18 Nov de (perfume) · 21 Nov fr · 24 Nov es · 27 Nov it · 30 Nov pl (then ro, nl, pt in December). Posted at local midday (CET 16:00 / EET 15:00 PKT) as the usual set: IG+FB+LI+TikTok + YT Short + Pinterest video pin 10 min later (board "Cosmetic Regulations UK & EU"). TikTok max 3/24 h: language reel + English reel = 2/day, fine.
Topics (verify at build): 18 de PERFUME (owner request 12 Nov): decants, travel sprays and miniatures — what changes when you split or refill perfume into smaller bottles (labelling, batch, notification/CPSR responsibility; verify with official sources first; fallback if it can't be verified: IFRA certificate vs safety report — what each covers) · Annex IV colourants moves to a later German slot · 21 fr preservatives (Annex V) · 24 es UV filters (Annex VI) · 27 it CMR substances (Art. 15) · 30 pl open slot (nightly run picks a verified topic that matches nothing else).
Build: new 4-scene script per language in tools/lang_content.py (same structure as the checklist reels, native wording, 38–49 s incl. 3.4 s end card), unique palette (reuse the language's existing PALETTES entry or add one), make sure CTA[<code>] exists, hook question from frame 0, Piper voice via tools/get_piper_voice.sh. Output filename must differ from the checklist reel (do not overwrite reels/lang/<code>-cosmetics-checklist.mp4).
