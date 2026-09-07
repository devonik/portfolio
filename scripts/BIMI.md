# BIMI & DMARC — devnik.dev

Status prüfen: `./scripts/bimi_status.sh devnik.dev`
SVG prüfen:    `python3 ./scripts/bimi_check.py public/logo-bimi.svg`

> Nicht mit `dig` prüfen. Dieser Anschluss fängt Port 53 ab und beantwortet jede
> Anfrage aus einem eigenen Resolver — auch `dig @1.2.3.4` liefert eine Antwort.
> `bimi_status.sh` fragt deshalb über DNS-over-HTTPS ab.

## Entscheidung: ohne Zertifikat

Ohne VMC/CMC zeigt nur Yahoo das Logo. Gmail verlangt VMC oder CMC, Apple Mail
zwingend VMC, Outlook unterstützt BIMI nicht (Stand 08/2026). CMC kostet
650–1400 USD/Jahr, VMC 750–1500 USD plus eingetragene Marke. Für Solo-Betrieb mit
geringem Volumen nicht wirtschaftlich. Nachrüsten = `a=`-Tag im BIMI-Record.
Falls doch: CMC, nicht VMC — die 12-Monats-Nutzungspflicht ist erfüllt
(devnik.dev ist seit 27.03.2024 in der Wayback Machine).

## Phase 0 — abgeschlossen 23.08.2026

- [x] `logo-bimi.svg` gebaut, validiert, deployed
- [x] `default._bimi` gesetzt: `v=BIMI1; l=https://devnik.dev/logo-bimi.svg; a=;`
- [x] `_dmarc` gesetzt: `v=DMARC1; p=none; rua=mailto:re+b4utbfeydgm@dmarc.postmarkapp.com; adkim=r; aspf=r`
- [x] Port25-Bericht vom 23.08.2026: `SPF pass`, `DKIM pass`, `iprev pass`.
      **Beide Mechanismen ausgerichtet** — `smtp.mailfrom=…@devnik.dev` und
      `header.d=devnik.dev`. Auch strenge Ausrichtung würde bestehen.
      Schlüssel 2048 Bit, `a=rsa-sha256`, `c=relaxed/relaxed`.

Doppelte Ausrichtung heißt: Weiterleitungen brechen zwar SPF, DKIM überlebt sie
aber. Die Verschärfung ist damit risikoarm abgesichert.

## Phase 1 — Beobachtung

Wöchentlicher Postmark-Digest (erster Bericht um den 30.08.). Zwei Kriterien,
beide müssen erfüllt sein:

- Keine unerklärten Versandquellen (alles außer Namecheap Private Email prüfen —
  legitim? dann in SPF/DKIM aufnehmen. Fremd? dann ist die Verschärfung richtig)
- 100 % DMARC-Pass für das eigene Volumen über zwei aufeinanderfolgende Wochen

Besonders achten auf: sendet die Portfolio-Seite selbst Mails (Kontaktformular)?
Der Port25-Test deckte nur den Weg über `smtp.privateemail.com` ab. Jede andere
Quelle taucht erst in den Reports auf.

### Stand 07.09.2026 — devnik.dev

- Digest 1 (24.–31.08.): 4 Mails, **100 % ausgerichtet**, ausschließlich
  Namecheap-IPs (104.207.68.48, 198.54.127.67, 63.250.43.113, 63.250.43.122)
- Digest 2 (31.08.–07.09.): erwartet am 07.09. gegen 23:20 MESZ, zum Zeitpunkt
  dieser Notiz noch nicht eingegangen

Zusätzlich am 01.09. unabhängig vom Digest geprüft:

- **Blog-App (EC2)** → authentifiziert (`ESMTPA`) über den privateemail-SMTP.
  Kopfzeilen beim Empfänger: `dkim=pass header.d=devnik.dev`, `spf=pass`,
  `Return-Path: <niklas.grieger@devnik.dev>` — beide Mechanismen ausgerichtet.
- **Gmail „Senden als"** → `mail.privateemail.com`, Port 587 TLS. Kein Versand
  über Google-IPs, also kein Alignment-Bruch.
- **Portfolio-Seite** → sendet nichts. Nur `mailto:`-Links in
  `app/app.config.ts:30` und `content/index.yml:180`, keine Mail-Bibliothek in
  `package.json`, keine SMTP-Credentials. Die offene Frage oben ist damit
  beantwortet.
- **Absender-Audit** über ~10 Wochen Postausgang: ausschließlich direkte
  1:1-Korrespondenz an Kunden und Recruiter. Keine Mailinglisten, kein
  Drittanbieter, der als `devnik.dev` sendet.

## Phase 2 — Rampe

### devnik.dev — am 01.09.2026 in einem Schritt auf pct=100

Abweichung vom ursprünglichen Plan. Statt der Stufen 25 → 50 → 100 wurde am
01.09. direkt gesetzt:

    v=DMARC1; p=quarantine; pct=100; rua=mailto:re+b4utbfeydgm@dmarc.postmarkapp.com; adkim=r; aspf=r

Zweck der Rampe war, unbekannte Versandquellen schrittweise aufzudecken. Diese
Frage war zu dem Zeitpunkt bereits anders und vollständiger beantwortet: durch
den Port25-Bericht vom 23.08. (doppelte Ausrichtung, auch strikt bestehend) und
den Absender-Audit aus Phase 1. Ein Rückschritt auf `pct=25` hätte den Schutz
gesenkt und BIMI um einen Monat verzögert, ohne eine neue Erkenntnis zu liefern.

Die BIMI-Voraussetzung ist damit **seit 01.09. erfüllt** statt ab 05.10.
Verifiziert über `bimi_status.sh` (DoH): `p=quarantine bei pct=100 — OK`.

Offen: `p=reject` (Termin 22.09.). Für BIMI nicht nötig, siehe Phase 4.

### kinderleicht-hannover.de — Rampe steht noch aus

Unverändert dreistufig, weil hier noch **kein** Versandweg per Testmail
verifiziert ist. Nach jedem Schritt eine Woche warten, Digest prüfen, Testmail
an Gmail (Nachricht → Original anzeigen → SPF/DKIM/DMARC müssen alle PASS sein):

| Datum (frühestens) | Wert                   | Kontrolle                    |
|--------------------|------------------------|------------------------------|
| 21.09.2026         | `p=quarantine; pct=25` | Testmail im Gmail-Posteingang|
| 28.09.2026         | `pct=50`               | Digest ohne neue Fehlschläge |
| 05.10.2026         | `pct=100`              | `bimi_status.sh` meldet OK   |

Bei einem FAIL sofort eine Stufe zurück.

Kein `sp=` setzen — Subdomains erben dann die Hauptpolicy. `sp=none` würde den
Schutz für Subdomains wieder aufheben.

## Phase 3 — BIMI-Verifikation

Für devnik.dev seit 01.09. durchführbar (siehe Phase 2), nicht erst ab Oktober.

1. `./scripts/bimi_status.sh devnik.dev` — alles grün
2. Gegenprüfung: mxtoolbox.com/bimi.aspx
3. Testmail an eine Yahoo-Adresse (einziger Client ohne Zertifikat)

Yahoo verlangt zusätzlich Absenderreputation. Bei geringem Volumen kann das
Logo Wochen brauchen oder ausbleiben — das ist dann kein Konfigurationsfehler.

## Phase 4 — laufend

- Monatlich Postmark-Digest überfliegen
- Logo-URL überwachen: `curl -sf https://devnik.dev/logo-bimi.svg >/dev/null || alert`
  (ein Redeploy ohne die Datei macht BIMI still kaputt)
- Nach Phase 2 `p=reject` erwägen (strengerer Spoofing-Schutz, für BIMI nicht nötig)

## kinderleicht-hannover.de

Todo/Fortschritt zusätzlich als GitHub-Issue geführt:
https://github.com/devonik/kinderleicht-hannover/issues/46


DNS liegt bei Vercel (Team `devonik`), Records also per CLI statt über ein Panel.

**Zwei Versandwege, beide DKIM-signiert — beide müssen DMARC bestehen, bevor
verschärft werden darf:**

| Selector                  | Größe    | Wofür                          |
|---------------------------|----------|--------------------------------|
| `spacemail._domainkey`    | 2048 Bit | Charlys Postfach `info@`       |
| `resend._domainkey`       | 1024 Bit | Transaktionsmails der App      |

Bricht einer davon, fallen entweder Charlys persönliche Mails oder die
Buchungsbestätigungen weg. Vor der Rampe deshalb ZWEI Nachweise nötig:
- Mail aus Charlys Postfach an `check-auth@verifier.port25.com`
- Ein Resend-Versand, geprüft über die Kopfzeilen beim Empfänger

Status: `./scripts/bimi_status.sh kinderleicht-hannover.de spacemail`
(bzw. `… resend` für den zweiten Weg)

> Korrigiert am 07.09.2026: Der Selector heißt `spacemail`, nicht `privateemail`.
> Namecheap hat Private Email zu Spacemail umbenannt, der SPF-Include zeigt
> konsistent auf `spf.spacemail.com`. Der alte Name lieferte ein „kein
> DKIM-Record"-FEHL, obwohl der 2048-Bit-Schlüssel publiziert ist.

### rua gesetzt am 23.08.2026

    v=DMARC1; p=none; rua=mailto:re+bx4ip70wlgw@dmarc.postmarkapp.com; adkim=r; aspf=r

Record-ID `rec_4bf447795fab44196673348f`. Beobachtungsphase läuft seit 23.08.
Die `rua`-Adresse war hier bis 07.09. falsch dokumentiert (`re+cikepvwzjgt@`);
live steht und stand `re+bx4ip70wlgw@`. Vermutlich beim Neuanlegen entstanden —
Vercel DNS kennt kein Update.
parallel zu devnik.dev. Postmark generiert `pct=100` und `sp=none` mit — beides
entfernt: 100 ist der Default und stört bei der Rampe, `sp=none` würde später den
Schutz für Subdomains aushebeln.

Vercel DNS kennt kein Update — erst `vercel dns rm <id>`, dann `vercel dns add`.
Dabei sicherstellen, dass am Ende genau EIN `_dmarc`-Record existiert: mehrere
DMARC-Records lassen Empfänger die Domain behandeln, als gäbe es gar keinen.

### ⚠️ Vor der Rampe: beide Wege verifizieren (Termin 14.09.)

Für devnik.dev ist die Verschärfung abgesichert, für kinderleicht ist noch kein
Weg geprüft. Nötig sind zwei Nachweise:

1. **Postfach** — Mail von `info@kinderleicht-hannover.de` an
   `check-auth@verifier.port25.com`. Erwartung: `header.d=kinderleicht-hannover.de`
   mit Selector `spacemail` (nicht `privateemail`, siehe oben)
2. **Resend** — echten Versand auslösen, beim Empfänger die Kopfzeilen prüfen.
   Der Return-Path läuft über `send.kinderleicht-hannover.de` (Amazon SES), SPF
   ist dort also anders ausgerichtet als beim Postfach — DKIM muss tragen.

### BIMI für kinderleicht — Record steht seit 23.08.2026

    v=BIMI1; l=https://www.kinderleicht-hannover.de/assets/logo-bimi.svg; a=;

Record-ID `rec_155f91e9dfd13f2b67b35abf`. Logo unter
`public/assets/logo-bimi.svg`, deployed am 23.08.2026 (Commit `83b7c60`,
direkt auf `main`). URL liefert HTTP 200 mit `image/svg+xml`, ausgelieferter
Inhalt byte-identisch mit der Quelle, Profilprüfung bestanden.

Wirksam wird der Record erst mit `pct=100` am 05.10.

Zwei Fallen, die hier fast zugeschlagen hätten:

1. **Die Maintenance-Sperre.** `proxy.ts` leitet alles außer der Allowlist auf die
   Startseite um — ein Mailprovider bekäme HTML statt SVG. Der Matcher nimmt
   `assets` aber aus, deshalb liegt das Logo unter `public/assets/` und nicht im
   `public/`-Wurzelverzeichnis. Verifiziert an `/assets/about.webp` → HTTP 200.
2. **Apex → www.** `kinderleicht-hannover.de` antwortet mit 308 auf
   `www.kinderleicht-hannover.de`. Der Record zeigt deshalb direkt auf www.

Gestaltung: Aquarellton `#D6DECF` und die Petrolfarben stammen aus einer
Pixelanalyse von `public/logo.svg` (JPEG im SVG-Mantel, für BIMI selbst
unbrauchbar). Schriftzug, Claim und Flugspur sind bewusst weggelassen — bei
32 px unlesbar bzw. unter der Sichtbarkeitsschwelle. Der Flieger ist auf 82 %
skaliert, weil die Flügelspitze sonst am Kreisbeschnitt streift.
