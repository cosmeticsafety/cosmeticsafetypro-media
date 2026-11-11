# -*- coding: utf-8 -*-
"""Per-language reel scripts (35–45 s, voiced). Each scene:
(kicker, title_html, big(bool: logo card), [(narration, bullet_or_None), ...])
tts: ("kokoro", voice, espeak_lang) or ("espeak", espeak_voice)
"""
WA = "WhatsApp +44 7868 737497"
SITE = "cosmeticsafetypro.com"

LANGS = {
 "fr": {
  "name": "French", "flag": "FR", "tts": ("kokoro", "ff_siwis", "fr-fr"),
  "scenes": [
   ("Conformité UE &amp; Royaume-Uni", "Vous vendez des <em>cosmétiques</em> en Europe&nbsp;?", True, [
     ("Vous vendez des soins, des parfums ou des autobronzants en Europe ? Voici votre liste de contrôle.", None)]),
   ("Union européenne", "Ce qu'il vous <em>faut</em> dans l'UE", False, [
     ("Dans l'Union européenne, chaque produit a besoin de :", None),
     ("une personne responsable établie dans l'UE,", "Personne responsable UE"),
     ("un rapport sur la sécurité, signé par un évaluateur qualifié,", "Rapport de sécurité (CPSR)"),
     ("un dossier d'information sur le produit,", "Dossier d'information (PIF)"),
     ("et une notification sur le portail européen avant la mise en vente.", "Notification CPNP")]),
   ("Royaume-Uni", "Vous vendez en <em>Grande-Bretagne</em>&nbsp;?", False, [
     ("Pour la Grande-Bretagne, il vous faut aussi une personne responsable au Royaume-Uni", "Personne responsable UK"),
     ("et une notification britannique.", "Notification SCPN"),
     ("Et attention aux allergènes des parfums, au rétinol et au facteur de protection solaire.", "Allergènes · rétinol · FPS")]),
   ("Cosmetic Safety Pro", "Analyse <em>gratuite</em> de votre formule", True, [
     ("Nous nous occupons de tout. Envoyez-nous votre formule pour une analyse gratuite sur WhatsApp,", WA),
     ("ou rendez-vous sur notre site.", SITE)]),
  ]},
 "de": {
  "name": "German", "flag": "DE", "tts": ("piper", "de_DE-thorsten-high"),
  "scenes": [
   ("EU- &amp; UK-Konformität", "Sie verkaufen <em>Kosmetik</em> in Europa?", True, [
     ("Sie verkaufen Hautpflege, Parfüm oder Selbstbräuner in Europa? Hier ist Ihre Checkliste.", None)]),
   ("Europäische Union", "Das brauchen Sie in der <em>EU</em>", False, [
     ("In der Europäischen Union braucht jedes Produkt:", None),
     ("eine verantwortliche Person mit Sitz in der EU,", "Verantwortliche Person EU"),
     ("einen Sicherheitsbericht, unterzeichnet von einem qualifizierten Sicherheitsbewerter,", "Sicherheitsbericht (CPSR)"),
     ("eine Produktinformationsdatei,", "Produktinformationsdatei (PIF)"),
     ("und eine Notifizierung im EU-Portal vor dem Verkauf.", "CPNP-Notifizierung")]),
   ("Großbritannien", "Sie verkaufen in <em>Großbritannien</em>?", False, [
     ("Für Großbritannien brauchen Sie zusätzlich eine verantwortliche Person im Vereinigten Königreich", "Verantwortliche Person UK"),
     ("und eine britische Notifizierung.", "SCPN-Notifizierung"),
     ("Und achten Sie auf Duftstoff-Allergene, Retinol und den Lichtschutzfaktor.", "Allergene · Retinol · LSF")]),
   ("Cosmetic Safety Pro", "<em>Kostenlose</em> Rezepturprüfung", True, [
     ("Wir kümmern uns um alles. Senden Sie uns Ihre Rezeptur für eine kostenlose Prüfung per WhatsApp,", WA),
     ("oder besuchen Sie unsere Website.", SITE)]),
  ]},
 "it": {
  "name": "Italian", "flag": "IT", "tts": ("kokoro", "if_sara", "it"),
  "scenes": [
   ("Conformità UE e Regno Unito", "Vendete <em>cosmetici</em> in Europa?", True, [
     ("Vendete prodotti per la pelle, profumi o autoabbronzanti in Europa? Ecco la vostra lista di controllo.", None)]),
   ("Unione europea", "Cosa serve nell'<em>UE</em>", False, [
     ("Nell'Unione europea, ogni prodotto ha bisogno di:", None),
     ("una persona responsabile con sede nell'UE,", "Persona responsabile UE"),
     ("una relazione sulla sicurezza, firmata da un valutatore qualificato,", "Relazione sulla sicurezza (CPSR)"),
     ("un fascicolo informativo sul prodotto,", "Fascicolo informativo (PIF)"),
     ("e una notifica sul portale europeo prima della vendita.", "Notifica CPNP")]),
   ("Regno Unito", "Vendete in <em>Gran Bretagna</em>?", False, [
     ("Per la Gran Bretagna serve anche una persona responsabile nel Regno Unito", "Persona responsabile UK"),
     ("e una notifica britannica.", "Notifica SCPN"),
     ("E attenzione agli allergeni dei profumi, al retinolo e al fattore di protezione solare.", "Allergeni · retinolo · SPF")]),
   ("Cosmetic Safety Pro", "Analisi <em>gratuita</em> della formula", True, [
     ("Pensiamo a tutto noi. Inviateci la vostra formula per un'analisi gratuita su WhatsApp,", WA),
     ("oppure visitate il nostro sito.", SITE)]),
  ]},
 "es": {
  "name": "Spanish", "flag": "ES", "tts": ("kokoro", "ef_dora", "es"),
  "scenes": [
   ("Cumplimiento UE y Reino Unido", "¿Vende <em>cosméticos</em> en Europa?", True, [
     ("¿Vende cuidado de la piel, perfumes o autobronceadores en Europa? Esta es su lista de control.", None)]),
   ("Unión Europea", "Lo que necesita en la <em>UE</em>", False, [
     ("En la Unión Europea, cada producto necesita:", None),
     ("una persona responsable establecida en la UE,", "Persona responsable UE"),
     ("un informe de seguridad, firmado por un evaluador cualificado,", "Informe de seguridad (CPSR)"),
     ("un expediente de información del producto,", "Expediente de información (PIF)"),
     ("y una notificación en el portal europeo antes de la venta.", "Notificación CPNP")]),
   ("Reino Unido", "¿Vende en <em>Gran Bretaña</em>?", False, [
     ("Para Gran Bretaña también necesita una persona responsable en el Reino Unido", "Persona responsable UK"),
     ("y una notificación británica.", "Notificación SCPN"),
     ("Y cuidado con los alérgenos de perfumes, el retinol y el factor de protección solar.", "Alérgenos · retinol · FPS")]),
   ("Cosmetic Safety Pro", "Revisión <em>gratuita</em> de su fórmula", True, [
     ("Nosotros nos encargamos de todo. Envíenos su fórmula para una revisión gratuita por WhatsApp,", WA),
     ("o visite nuestra web.", SITE)]),
  ]},
 "nl": {
  "name": "Dutch", "flag": "NL", "tts": ("piper", "nl_BE-nathalie-medium"),
  "scenes": [
   ("EU- &amp; VK-naleving", "Verkoopt u <em>cosmetica</em> in Europa?", True, [
     ("Verkoopt u huidverzorging, parfum of zelfbruiners in Europa? Dit is uw checklist.", None)]),
   ("Europese Unie", "Wat u nodig hebt in de <em>EU</em>", False, [
     ("In de Europese Unie heeft elk product nodig:", None),
     ("een verantwoordelijke persoon in de EU,", "Verantwoordelijke persoon EU"),
     ("een veiligheidsrapport, ondertekend door een gekwalificeerde veiligheidsbeoordelaar,", "Veiligheidsrapport (CPSR)"),
     ("een productinformatiedossier,", "Productinformatiedossier (PIF)"),
     ("en een notificatie op het Europese portaal vóór de verkoop.", "CPNP-notificatie")]),
   ("Verenigd Koninkrijk", "Verkoopt u in <em>Groot-Brittannië</em>?", False, [
     ("Voor Groot-Brittannië hebt u ook een verantwoordelijke persoon in het Verenigd Koninkrijk nodig", "Verantwoordelijke persoon VK"),
     ("en een Britse notificatie.", "SCPN-notificatie"),
     ("En let op allergenen in parfum, retinol en de zonbeschermingsfactor.", "Allergenen · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Gratis</em> formulecheck", True, [
     ("Wij regelen alles. Stuur ons uw formule voor een gratis check via WhatsApp,", WA),
     ("of bezoek onze website.", SITE)]),
  ]},
 "pt": {
  "name": "Portuguese", "flag": "PT", "tts": ("kokoro", "pf_dora", "pt"),
  "scenes": [
   ("Conformidade UE e Reino Unido", "Vende <em>cosméticos</em> na Europa?", True, [
     ("Vende cuidados de pele, perfumes ou autobronzeadores na Europa? Esta é a sua lista de verificação.", None)]),
   ("União Europeia", "O que precisa na <em>UE</em>", False, [
     ("Na União Europeia, cada produto precisa de:", None),
     ("uma pessoa responsável estabelecida na UE,", "Pessoa responsável UE"),
     ("um relatório de segurança, assinado por um avaliador qualificado,", "Relatório de segurança (CPSR)"),
     ("um ficheiro de informações do produto,", "Ficheiro de informações (PIF)"),
     ("e uma notificação no portal europeu antes da venda.", "Notificação CPNP")]),
   ("Reino Unido", "Vende na <em>Grã-Bretanha</em>?", False, [
     ("Para a Grã-Bretanha, precisa também de uma pessoa responsável no Reino Unido", "Pessoa responsável UK"),
     ("e de uma notificação britânica.", "Notificação SCPN"),
     ("E atenção aos alergénios dos perfumes, ao retinol e ao fator de proteção solar.", "Alergénios · retinol · FPS")]),
   ("Cosmetic Safety Pro", "Análise <em>gratuita</em> da sua fórmula", True, [
     ("Nós tratamos de tudo. Envie-nos a sua fórmula para uma análise gratuita pelo WhatsApp,", WA),
     ("ou visite o nosso site.", SITE)]),
  ]},
 "pl": {
  "name": "Polish", "flag": "PL", "tts": ("piper", "pl_PL-gosia-medium"),
  "scenes": [
   ("Zgodność UE i Wielka Brytania", "Sprzedajesz <em>kosmetyki</em> w Europie?", True, [
     ("Sprzedajesz kosmetyki, perfumy lub samoopalacze w Europie? Oto Twoja lista kontrolna.", None)]),
   ("Unia Europejska", "Czego potrzebujesz w <em>UE</em>", False, [
     ("W Unii Europejskiej każdy produkt potrzebuje:", None),
     ("osoby odpowiedzialnej z siedzibą w UE,", "Osoba odpowiedzialna UE"),
     ("raportu bezpieczeństwa, podpisanego przez wykwalifikowanego oceniającego,", "Raport bezpieczeństwa (CPSR)"),
     ("dokumentacji informacyjnej produktu,", "Dokumentacja produktu (PIF)"),
     ("oraz zgłoszenia w europejskim portalu przed sprzedażą.", "Zgłoszenie CPNP")]),
   ("Wielka Brytania", "Sprzedajesz w <em>Wielkiej Brytanii</em>?", False, [
     ("W Wielkiej Brytanii potrzebujesz też osoby odpowiedzialnej w Zjednoczonym Królestwie", "Osoba odpowiedzialna UK"),
     ("i brytyjskiego zgłoszenia.", "Zgłoszenie SCPN"),
     ("Uważaj też na alergeny zapachowe, retinol i filtr przeciwsłoneczny.", "Alergeny · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Bezpłatna</em> analiza receptury", True, [
     ("Zajmiemy się wszystkim. Wyślij nam recepturę do bezpłatnej analizy przez WhatsApp,", WA),
     ("lub odwiedź naszą stronę.", SITE)]),
  ]},
 "sv": {
  "name": "Swedish", "flag": "SE", "tts": ("piper", "sv_SE-alma-medium"),
  "scenes": [
   ("EU och Storbritannien", "Säljer du <em>kosmetika</em> i Europa?", True, [
     ("Säljer du kosmetika, parfym eller brun utan sol i Europa? Här är din checklista.", None)]),
   ("Europeiska unionen", "Det här behöver du i <em>EU</em>", False, [
     ("I EU behöver varje produkt:", None),
     ("en ansvarig person i EU,", "Ansvarig person i EU"),
     ("en säkerhetsrapport, signerad av en behörig bedömare,", "Säkerhetsrapport (CPSR)"),
     ("en produktinformationsfil,", "Produktinformationsfil (PIF)"),
     ("och en anmälan i den europeiska portalen innan försäljning.", "CPNP-anmälan")]),
   ("Storbritannien", "Säljer du i <em>Storbritannien</em>?", False, [
     ("I Storbritannien behöver du dessutom en ansvarig person i Storbritannien", "Ansvarig person i UK"),
     ("och en brittisk anmälan.", "SCPN-anmälan"),
     ("Var också uppmärksam på doftallergener, retinol och solskydd.", "Allergener · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Kostnadsfri</em> granskning av receptet", True, [
     ("Vi tar hand om allt. Skicka ditt recept för en kostnadsfri granskning via WhatsApp,", WA),
     ("eller besök vår webbplats.", SITE)]),
  ]},
 "da": {
  "name": "Danish", "flag": "DK", "tts": ("piper", "da_DK-talesyntese-medium"),
  "scenes": [
   ("EU og Storbritannien", "Sælger du <em>kosmetik</em> i Europa?", True, [
     ("Sælger du hudpleje, parfume eller selvbruner i Europa? Her er din tjekliste.", None)]),
   ("Den Europæiske Union", "Det skal du have i <em>EU</em>", False, [
     ("I EU skal hvert produkt have:", None),
     ("en ansvarlig person med base i EU,", "Ansvarlig person i EU"),
     ("en sikkerhedsrapport, underskrevet af en kvalificeret vurderingsekspert,", "Sikkerhedsrapport (CPSR)"),
     ("en produktinformationsfil,", "Produktinformationsfil (PIF)"),
     ("og en anmeldelse i den europæiske portal, før salget starter.", "CPNP-anmeldelse")]),
   ("Storbritannien", "Sælger du i <em>Storbritannien</em>?", False, [
     ("I Storbritannien skal du desuden have en ansvarlig person i Storbritannien", "Ansvarlig person i UK"),
     ("og en britisk anmeldelse.", "SCPN-anmeldelse"),
     ("Hold også øje med duftallergener, retinol og solbeskyttelse.", "Allergener · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Gratis</em> gennemgang af din formel", True, [
     ("Vi klarer det hele. Send os din formel til en gratis gennemgang via WhatsApp,", WA),
     ("eller besøg vores hjemmeside.", SITE)]),
  ]},
 "fi": {
  "name": "Finnish", "flag": "FI", "tts": ("piper", "fi_FI-harri-medium", 0.83),
  "scenes": [
   ("EU- ja UK-vaatimukset", "Myytkö <em>kosmetiikkaa</em> Euroopassa?", True, [
     ("Myytkö ihonhoitotuotteita, hajusteita tai itseruskettavia tuotteita Euroopassa? Tässä on tarkistuslistasi.", None)]),
   ("Euroopan unioni", "Mitä tarvitset <em>EU:ssa</em>", False, [
     ("Euroopan unionissa jokainen tuote tarvitsee:", None),
     ("EU:hun sijoittautuneen vastuuhenkilön,", "Vastuuhenkilö EU"),
     ("pätevän arvioijan allekirjoittaman turvallisuusraportin,", "Turvallisuusraportti (CPSR)"),
     ("tuotetietoasiakirjan,", "Tuotetietoasiakirja (PIF)"),
     ("ja ilmoituksen EU:n portaaliin ennen myyntiä.", "CPNP-ilmoitus")]),
   ("Iso-Britannia", "Myytkö <em>Isossa-Britanniassa</em>?", False, [
     ("Isoon-Britanniaan tarvitset lisäksi vastuuhenkilön Yhdistyneessä kuningaskunnassa", "Vastuuhenkilö UK"),
     ("ja brittiläisen ilmoituksen.", "SCPN-ilmoitus"),
     ("Huomioi myös hajusteallergeenit, retinoli ja aurinkosuojakerroin.", "Allergeenit · retinoli · SPF")]),
   ("Cosmetic Safety Pro", "<em>Maksuton</em> reseptin tarkistus", True, [
     ("Hoidamme kaiken puolestasi. Lähetä reseptisi maksuttomaan tarkistukseen WhatsAppilla,", WA),
     ("tai käy verkkosivuillamme.", SITE)]),
  ]},
 "cs": {
  "name": "Czech", "flag": "CZ", "tts": ("piper", "cs_CZ-jirka-medium", 0.74),
  "scenes": [
   ("EU a Spojené království", "Prodáváte <em>kosmetiku</em> v Evropě?", True, [
     ("Prodáváte kosmetiku nebo parfémy v Evropě? Tady je váš kontrolní seznam.", None)]),
   ("Evropská unie", "Co potřebujete v <em>EU</em>", False, [
     ("V Evropské unii potřebuje každý výrobek:", None),
     ("odpovědnou osobu se sídlem v EU,", "Odpovědná osoba v EU"),
     ("zprávu o bezpečnosti, podepsanou kvalifikovaným hodnotitelem,", "Zpráva o bezpečnosti (CPSR)"),
     ("informační dokumentaci o výrobku,", "Informační dokumentace (PIF)"),
     ("a oznámení na evropském portálu ještě před zahájením prodeje.", "Oznámení CPNP")]),
   ("Spojené království", "Prodáváte i ve <em>Velké Británii</em>?", False, [
     ("Ve Velké Británii navíc potřebujete britskou odpovědnou osobu", "Odpovědná osoba v UK"),
     ("a britské oznámení.", "Oznámení SCPN"),
     ("Pozor také na alergeny ve vůních, retinol a ochranu před sluncem.", "Alergeny · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Bezplatná</em> kontrola vaší receptury", True, [
     ("Pošlete nám recepturu na bezplatnou kontrolu přes WhatsApp,", WA),
     ("nebo navštivte náš web.", SITE)]),
  ]},
 "sk": {
  "name": "Slovak", "flag": "SK", "tts": ("piper", "sk_SK-lili-medium", 0.8),
  "scenes": [
   ("EÚ a Spojené kráľovstvo", "Predávate <em>kozmetiku</em> v Európe?", True, [
     ("Predávate kozmetiku alebo parfumy v Európe? Tu je váš kontrolný zoznam.", None)]),
   ("Európska únia", "Čo potrebujete v <em>EÚ</em>", False, [
     ("V Európskej únii potrebuje každý výrobok:", None),
     ("zodpovednú osobu so sídlom v EÚ,", "Zodpovedná osoba v EÚ"),
     ("správu o bezpečnosti, podpísanú kvalifikovaným posudzovateľom,", "Správa o bezpečnosti (CPSR)"),
     ("informačnú dokumentáciu o výrobku,", "Informačná dokumentácia (PIF)"),
     ("a oznámenie na európskom portáli ešte pred začatím predaja.", "Oznámenie CPNP")]),
   ("Spojené kráľovstvo", "Predávate aj vo <em>Veľkej Británii</em>?", False, [
     ("Vo Veľkej Británii navyše potrebujete britskú zodpovednú osobu", "Zodpovedná osoba v UK"),
     ("a britské oznámenie.", "Oznámenie SCPN"),
     ("Pozor aj na alergény vo vôňach, retinol a ochranu pred slnkom.", "Alergény · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Bezplatná</em> kontrola vašej receptúry", True, [
     ("Pošlite nám receptúru na bezplatnú kontrolu cez WhatsApp,", WA),
     ("alebo navštívte náš web.", SITE)]),
  ]},
 "hu": {
  "name": "Hungarian", "flag": "HU", "tts": ("piper", "hu_HU-anna-medium", 0.85),
  "scenes": [
   ("EU és Egyesült Királyság", "Kozmetikumot <em>árul</em> Európában?", True, [
     ("Kozmetikumot vagy parfümöt árul Európában? Itt az ellenőrzőlistája.", None)]),
   ("Európai Unió", "Ami kell az <em>EU-ban</em>", False, [
     ("Az Európai Unióban minden terméknek kell:", None),
     ("egy EU-ban székhellyel rendelkező felelős személy,", "Felelős személy az EU-ban"),
     ("egy biztonsági értékelés, amelyet képesített értékelő ír alá,", "Biztonsági jelentés (CPSR)"),
     ("egy termékinformációs dokumentáció,", "Termékinformációs dosszié (PIF)"),
     ("és bejelentés az európai portálon még a forgalmazás előtt.", "CPNP bejelentés")]),
   ("Egyesült Királyság", "Nagy-Britanniában <em>is</em> árul?", False, [
     ("Nagy-Britanniában ezen felül brit felelős személy kell", "Felelős személy az UK-ban"),
     ("és brit bejelentés.", "SCPN bejelentés")
     ,("Figyeljen az illatanyag-allergénekre, a retinolra és a fényvédelemre is.", "Allergének · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Ingyenes</em> receptúra-ellenőrzés", True, [
     ("Küldje el receptúráját ingyenes ellenőrzésre WhatsAppon,", WA),
     ("vagy látogasson el weboldalunkra.", SITE)]),
  ]},
 "ro": {
  "name": "Romanian", "flag": "RO", "tts": ("piper", "ro_RO-mihai-medium", 0.9),
  "scenes": [
   ("Conformitate UE și Marea Britanie", "Vindeți <em>cosmetice</em> în Europa?", True, [
     ("Vindeți cosmetice sau parfumuri în Europa? Iată lista dumneavoastră de verificare.", None)]),
   ("Uniunea Europeană", "Ce vă trebuie în <em>UE</em>", False, [
     ("În Uniunea Europeană, fiecare produs are nevoie de:", None),
     ("o persoană responsabilă cu sediul în UE,", "Persoană responsabilă în UE"),
     ("un raport de siguranță semnat de un evaluator calificat,", "Raport de siguranță (CPSR)"),
     ("un dosar cu informații despre produs,", "Dosarul produsului (PIF)"),
     ("și notificarea pe portalul european înainte de vânzare.", "Notificare CPNP")]),
   ("Marea Britanie", "Vindeți și în <em>Marea Britanie</em>?", False, [
     ("Pentru Marea Britanie aveți nevoie și de o persoană responsabilă britanică", "Persoană responsabilă în UK"),
     ("și de notificarea britanică.", "Notificare SCPN"),
     ("Atenție și la alergenii din parfumuri, la retinol și la protecția solară.", "Alergeni · retinol · SPF")]),
   ("Cosmetic Safety Pro", "Verificare <em>gratuită</em> a formulei", True, [
     ("Trimiteți-ne formula pentru o verificare gratuită pe WhatsApp", WA),
     ("sau vizitați site-ul nostru.", SITE)]),
  ]},
 "hr": {
  "name": "Croatian", "flag": "HR", "tts": ("file", "reels/lang/hr-voice-ttsmaker.mp3"),
  "scenes": [
   ("Usklađenost EU i UK", "Prodajete <em>kozmetiku</em> u Europi?", True, [
     ("Prodajete kozmetiku, parfeme ili samopotamnjivače u Europi? Evo vašeg popisa za provjeru.", None)]),
   ("Europska unija", "Što vam treba u <em>EU</em>", False, [
     ("U Europskoj uniji svaki proizvod treba:", None),
     ("odgovornu osobu sa sjedištem u EU,", "Odgovorna osoba EU"),
     ("izvješće o sigurnosti koje potpisuje kvalificirani procjenitelj,", "Izvješće o sigurnosti (CPSR)"),
     ("dokumentaciju s informacijama o proizvodu,", "Dokumentacija proizvoda (PIF)"),
     ("i prijavu na europskom portalu prije prodaje.", "Prijava CPNP")]),
   ("Velika Britanija", "Prodajete u <em>Velikoj Britaniji</em>?", False, [
     ("Za Veliku Britaniju trebate i odgovornu osobu u Ujedinjenom Kraljevstvu", "Odgovorna osoba UK"),
     ("i britansku prijavu.", "Prijava SCPN"),
     ("I pazite na alergene u mirisima, retinol i zaštitni faktor.", "Alergeni · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Besplatna</em> provjera formulacije", True, [
     ("Mi se brinemo o svemu. Pošaljite nam svoju formulaciju na besplatnu provjeru putem WhatsAppa", WA),
     ("ili posjetite našu web stranicu.", SITE)]),
  ]},
 "bg": {
  "name": "Bulgarian", "flag": "BG", "tts": ("piper", "bg_BG-dimitar-medium", 0.9),
  "scenes": [
   ("ЕС и Обединеното кралство", "Продавате ли <em>козметика</em> в Европа?", True, [
     ("Продавате козметика, парфюми или автотан в Европа? Ето вашия списък за проверка.", None)]),
   ("Европейският съюз", "Какво ви трябва в <em>ЕС</em>", False, [
     ("В ЕС всеки продукт се нуждае от:", None),
     ("отговорно лице, установено в ЕС,", "Отговорно лице в ЕС"),
     ("доклад за безопасност, подписан от квалифициран оценител,", "Доклад за безопасност (CPSR)"),
     ("досие на продукта,", "Досие на продукта (PIF)"),
     ("и нотификация в европейския портал преди продажбата.", "Нотификация CPNP")]),
   ("Обединено кралство", "Продавате ли във <em>Великобритания</em>?", False, [
     ("За Великобритания ви трябва и отговорно лице във Великобритания", "Отговорно лице в UK"),
     ("и британска нотификация.", "Нотификация SCPN"),
     ("Внимавайте и с алергените в парфюмите, ретинола и слънцезащитния фактор.", "Алергени · ретинол · SPF")]),
   ("Cosmetic Safety Pro", "<em>Безплатен</em> преглед на формулата", True, [
     ("Ние се грижим за всичко. Изпратете формулата си за безплатен преглед през WhatsApp,", WA),
     ("или посетете нашия уебсайт.", SITE)]),
  ]},
 "el": {
  "name": "Greek", "flag": "GR", "tts": ("piper", "el_GR-rapunzelina-medium", 0.9),
  "scenes": [
   ("ΕΕ και Ηνωμένο Βασίλειο", "Πουλάτε <em>καλλυντικά</em> στην Ευρώπη;", True, [
     ("Πουλάτε καλλυντικά, αρώματα ή αυτομαυριστικά στην Ευρώπη; Ορίστε η λίστα ελέγχου σας.", None)]),
   ("Ευρωπαϊκή Ένωση", "Τι χρειάζεστε στην <em>ΕΕ</em>", False, [
     ("Στην ΕΕ κάθε προϊόν χρειάζεται:", None),
     ("ένα Υπεύθυνο Πρόσωπο εγκατεστημένο στην ΕΕ,", "Υπεύθυνο Πρόσωπο ΕΕ"),
     ("έκθεση ασφάλειας, υπογεγραμμένη από πιστοποιημένο αξιολογητή,", "Έκθεση ασφάλειας (CPSR)"),
     ("φάκελο πληροφοριών προϊόντος,", "Φάκελος προϊόντος (PIF)"),
     ("και κοινοποίηση στην ευρωπαϊκή πύλη πριν από την πώληση.", "Κοινοποίηση CPNP")]),
   ("Ηνωμένο Βασίλειο", "Πουλάτε στο <em>Ηνωμένο Βασίλειο</em>;", False, [
     ("Για το Ηνωμένο Βασίλειο χρειάζεστε επιπλέον Υπεύθυνο Πρόσωπο στη Βρετανία", "Υπεύθυνο Πρόσωπο UK"),
     ("και βρετανική κοινοποίηση.", "Κοινοποίηση SCPN"),
     ("Προσέξτε επίσης τα αλλεργιογόνα αρωμάτων, τη ρετινόλη και τον δείκτη αντηλιακού.", "Αλλεργιογόνα · ρετινόλη · SPF")]),
   ("Cosmetic Safety Pro", "<em>Δωρεάν</em> έλεγχος της σύνθεσής σας", True, [
     ("Αναλαμβάνουμε τα πάντα. Στείλτε μας τη σύνθεσή σας για δωρεάν έλεγχο στο WhatsApp,", WA),
     ("ή επισκεφθείτε την ιστοσελίδα μας.", SITE)]),
  ]},
 "sl": {
  "name": "Slovenian", "flag": "SI", "tts": ("piper", "sl_SI-artur-medium", 0.9),
  "scenes": [
   ("EU in Združeno kraljestvo", "Prodajate <em>kozmetiko</em> v Evropi?", True, [
     ("Prodajate kozmetiko ali parfume v Evropi? Brez teh štirih stvari izdelka ne smete prodajati.", None)]),
   ("Evropska unija", "Kaj potrebujete v <em>EU</em>", False, [
     ("V EU vsak izdelek potrebuje:", None),
     ("odgovorno osebo s sedežem v EU,", "Odgovorna oseba v EU"),
     ("poročilo o varnosti, ki ga podpiše usposobljen ocenjevalec,", "Poročilo o varnosti (CPSR)"),
     ("dokumentacijo z informacijami o izdelku,", "Dokumentacija izdelka (PIF)"),
     ("in priglasitev na evropskem portalu pred prodajo.", "Priglasitev CPNP")]),
   ("Združeno kraljestvo", "Prodajate v <em>Veliki Britaniji</em>?", False, [
     ("Za Veliko Britanijo potrebujete še odgovorno osebo v Združenem kraljestvu", "Odgovorna oseba v UK"),
     ("in britansko priglasitev.", "Priglasitev SCPN"),
     ("Bodite pozorni tudi na alergene v dišavah, retinol in zaščitni faktor.", "Alergeni · retinol · SPF")]),
   ("Cosmetic Safety Pro", "<em>Brezplačen</em> pregled formulacije", True, [
     ("Za vse poskrbimo mi. Pošljite nam svojo formulacijo v brezplačen pregled prek WhatsAppa", WA),
     ("ali obiščite našo spletno stran.", SITE)]),
  ]},
 "lt": {
  "name": "Lithuanian", "flag": "LT", "tts": ("piper", "lt_LT-ingute-medium", 0.9),
  "scenes": [
   ("ES ir Jungtinė Karalystė", "Parduodate <em>kosmetiką</em> Europoje?", True, [
     ("Parduodate kosmetiką ar kvepalus Europoje? Be šių keturių dalykų savo produkto parduoti negalite.", None)]),
   ("Europos Sąjunga", "Ko reikia <em>ES</em>", False, [
     ("Europos Sąjungoje kiekvienam produktui reikia:", None),
     ("atsakingojo asmens, įsisteigusio ES,", "Atsakingasis asmuo ES"),
     ("saugos ataskaitos, kurią pasirašo kvalifikuotas vertintojas,", "Saugos ataskaita (CPSR)"),
     ("produkto informacinės bylos,", "Produkto informacinė byla (PIF)"),
     ("ir pranešimo Europos portale prieš pradedant prekybą.", "Pranešimas CPNP")]),
   ("Jungtinė Karalystė", "Parduodate <em>Didžiojoje Britanijoje</em>?", False, [
     ("Didžiajai Britanijai dar reikia atsakingojo asmens Jungtinėje Karalystėje", "Atsakingasis asmuo JK"),
     ("ir britiško pranešimo.", "Pranešimas SCPN"),
     ("Atkreipkite dėmesį ir į kvapiųjų medžiagų alergenus, retinolį ir apsaugos nuo saulės faktorių.", "Alergenai · retinolis · SPF")]),
   ("Cosmetic Safety Pro", "<em>Nemokama</em> formulės peržiūra", True, [
     ("Viskuo pasirūpinsime mes. Atsiųskite savo formulę nemokamai peržiūrai per WhatsApp", WA),
     ("arba apsilankykite mūsų svetainėje.", SITE)]),
  ]},
 "lv": {
  "name": "Latvian", "flag": "LV", "tts": ("piper", "lv_LV-aivars-medium", 0.8),
  "scenes": [
   ("ES un Lielbritānija", "Pārdodat <em>kosmētiku</em> Eiropā?", True, [
     ("Pārdodat kosmētiku vai smaržas Eiropā? Bez šīm četrām lietām savu produktu pārdot nedrīkstat.", None)]),
   ("Eiropas Savienība", "Kas nepieciešams <em>ES</em>", False, [
     ("Eiropas Savienībā katram produktam ir nepieciešama:", None),
     ("atbildīgā persona, kas reģistrēta ES,", "Atbildīgā persona ES"),
     ("drošuma ziņojums, ko parakstījis kvalificēts vērtētājs,", "Drošuma ziņojums (CPSR)"),
     ("produkta informācijas dokumentācija,", "Produkta dokumentācija (PIF)"),
     ("un paziņojums Eiropas portālā pirms pārdošanas.", "CPNP paziņojums")]),
   ("Apvienotā Karaliste", "Pārdodat <em>Lielbritānijā</em>?", False, [
     ("Lielbritānijai papildus nepieciešama atbildīgā persona Apvienotajā Karalistē", "Atbildīgā persona AK"),
     ("un britu paziņojums.", "SCPN paziņojums"),
     ("Pievērsiet uzmanību arī smaržvielu alergēniem, retinolam un saules aizsardzības faktoram.", "Alergēni · retinols · SPF")]),
   ("Cosmetic Safety Pro", "<em>Bezmaksas</em> receptūras pārbaude", True, [
     ("Mēs parūpēsimies par visu. Atsūtiet savu receptūru bezmaksas pārbaudei WhatsApp", WA),
     ("vai apmeklējiet mūsu tīmekļa vietni.", SITE)]),
  ]},
}
