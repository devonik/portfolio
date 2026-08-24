#!/usr/bin/env bash
# BIMI/DMARC readiness check for one domain.
# Usage: ./bimi_status.sh devnik.dev [dkim-selector]
set -uo pipefail

DOMAIN="${1:?Usage: $0 <domain> [dkim-selector]}"
SELECTOR="${2:-default}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# This connection hijacks port 53 and answers every query from its own resolver,
# even when an explicit "@server" is given, so local lookups cannot be trusted.
# Query over DNS-over-HTTPS instead, which is unaffected.
txt() {
  curl -s --max-time 15 -H 'accept: application/dns-json' \
    "https://dns.google/resolve?name=$1&type=TXT" \
  | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
for a in d.get('Answer', []):
    if a.get('type') == 16:
        print(a['data'].strip('\"'))
"
}

ok()   { printf '  \033[32m OK \033[0m %s\n' "$1"; }
bad()  { printf '  \033[31mFEHL\033[0m %s\n' "$1"; }
warn() { printf '  \033[33mWARN\033[0m %s\n' "$1"; }
info() { printf '       %s\n' "$1"; }

printf '\n\033[1m=== %s ===\033[0m\n' "$DOMAIN"

# --- SPF ---
echo; echo "SPF"
spf=$(txt "$DOMAIN" | grep '^v=spf1' | head -1)
[ -n "$spf" ] && ok "$spf" || bad "kein SPF-Record"

# --- DKIM ---
echo; echo "DKIM (Selector: $SELECTOR)"
dkim=$(txt "${SELECTOR}._domainkey.${DOMAIN}" | head -1)
if [ -n "$dkim" ]; then
  ok "Schluessel publiziert ($(echo -n "$dkim" | wc -c | tr -d ' ') Zeichen)"
  info "Signierung nur per Testmail an check-auth@verifier.port25.com pruefbar"
else
  bad "kein DKIM-Record fuer Selector '$SELECTOR'"
fi

# --- DMARC ---
echo; echo "DMARC"
dmarc=$(txt "_dmarc.${DOMAIN}" | grep '^v=DMARC1' | head -1)
if [ -z "$dmarc" ]; then
  bad "kein DMARC-Record - BIMI unmoeglich"
else
  info "$dmarc"
  policy=$(echo "$dmarc" | grep -oE 'p=[a-z]+' | head -1 | cut -d= -f2)
  pct=$(echo "$dmarc" | grep -oE 'pct=[0-9]+' | head -1 | cut -d= -f2)
  pct=${pct:-100}
  case "$policy" in
    reject|quarantine)
      if [ "$pct" -eq 100 ]; then ok "p=$policy bei pct=$pct - BIMI-Voraussetzung erfuellt"
      else warn "p=$policy, aber pct=$pct - BIMI verlangt pct=100"; fi ;;
    none) warn "p=none - Beobachtungsmodus, BIMI noch nicht moeglich" ;;
    *)    bad "Policy nicht lesbar" ;;
  esac
  rua=$(echo "$dmarc" | grep -oE 'rua=[^;]+' | head -1 | cut -d= -f2- | xargs)
  if [ -z "$rua" ]; then
    warn "kein rua= - keine Reports, Beobachtungsphase sammelt nichts"
  elif echo "$rua" | grep -qE '^mailto:[^[:space:]@,;:]+@[^[:space:]@,;:]+\.[a-zA-Z]{2,}(,mailto:[^[:space:]@,;:]+@[^[:space:]@,;:]+\.[a-zA-Z]{2,})*$'; then
    ok "Reporting an $rua"
  else
    bad "rua ist unbrauchbar: '$rua' - erwartet mailto:adresse@domain, es kommen keine Reports"
  fi
  echo "$dmarc" | grep -q ';;' && warn "doppeltes Semikolon im Record - leeres Tag"
  sp=$(echo "$dmarc" | grep -oE 'sp=[a-z]+' | head -1 | cut -d= -f2)
  [ "${sp:-}" = "none" ] && warn "sp=none hebt die Wirkung fuer Subdomains auf"
fi

# --- BIMI ---
echo; echo "BIMI"
bimi=$(txt "default._bimi.${DOMAIN}" | grep '^v=BIMI1' | head -1)
if [ -z "$bimi" ]; then
  warn "kein BIMI-Record unter default._bimi"
else
  info "$bimi"
  url=$(echo "$bimi" | grep -oE 'l=[^;]+' | head -1 | cut -d= -f2- | xargs)
  if [ -z "$url" ]; then
    bad "kein l= (Logo-URL) im Record"
  else
    read -r code ctype eff < <(curl -sIL -o /dev/null \
      -w '%{http_code} %{content_type} %{url_effective}' --max-time 15 "$url")
    [ "$code" = "200" ] && ok "HTTP 200: $url" || bad "HTTP $code fuer $url"
    case "$ctype" in
      image/svg+xml*) ok "Content-Type: $ctype" ;;
      *)              bad "Content-Type ist '$ctype', erwartet image/svg+xml" ;;
    esac
    [ "$eff" != "$url" ] && warn "Weiterleitung nach $eff - besser direkt ausliefern"
    case "$url" in https://*) ok "HTTPS" ;; *) bad "keine HTTPS-URL" ;; esac

    if [ -x "$(command -v python3)" ] && [ -f "$HERE/bimi_check.py" ]; then
      tmp=$(mktemp /tmp/bimi.XXXXXX.svg)
      if curl -sL --max-time 15 -o "$tmp" "$url"; then
        echo; echo "SVG-Profilpruefung"
        python3 "$HERE/bimi_check.py" "$tmp" | tail -n +2
      fi
      rm -f "$tmp"
    fi
  fi
fi
echo
