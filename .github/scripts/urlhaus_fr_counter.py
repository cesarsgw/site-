#!/usr/bin/env python3
"""Compte les URL de malware actives hébergées en France (abuse.ch URLhaus).
Écrit cyber-counter.json lu par site/threat-counter.js."""
import csv, io, json, os, sys, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone

FEED = os.environ.get("URLHAUS_FEED", "https://urlhaus.abuse.ch/feeds/country/FR/")
OUT = sys.argv[1] if len(sys.argv) > 1 else "cyber-counter.json"
COLS = ["dateadded", "url", "url_status", "threat", "host", "ip", "asn", "country"]


def write(data):
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def fail(err):
    write({"ok": False, "error": err, "updatedAt": datetime.now(timezone.utc).isoformat()})
    print("ERREUR:", err)
    sys.exit(0)  # le JSON d'erreur est publié, le site affiche « indisponible »


key = os.environ.get("URLHAUS_AUTH_KEY", "").strip()
if not key:
    fail("cle_absente")

req = urllib.request.Request(FEED, headers={"Auth-Key": key, "User-Agent": "mgc-threat-counter"})
try:
    raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
except urllib.error.HTTPError as e:
    fail("http_%d" % e.code)
except Exception:
    fail("reseau")

print("--- apercu flux (5 premieres lignes) ---")
_l = raw.splitlines()
print("\n".join([x for x in _l if x.startswith("#")][-6:] + [x for x in _l if not x.startswith("#")][:4])[:2500])
rows = [r for r in csv.reader(io.StringIO("\n".join(l for l in raw.splitlines() if l and not l.startswith("#")))) if r]
if not rows:
    fail("flux_vide")
if not rows or len(rows[0]) < 3:
    fail("format_inattendu")

statuses = {r[2].strip().lower() for r in rows if len(r) > 2}
print("statuts vus:", sorted(statuses)[:10], "| lignes:", len(rows))
if not statuses & {"online", "offline"}:
    fail("format_inattendu")

now = datetime.now(timezone.utc)
online = added24h = 0
for r in rows:
    d = dict(zip(COLS, r))
    if d.get("url_status", "").strip().lower() != "online":
        continue
    online += 1
    try:
        t = datetime.strptime(d["dateadded"].strip(), "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        if now - t <= timedelta(hours=24):
            added24h += 1
    except Exception:
        pass

write({"ok": True, "value": online, "added24h": added24h, "realtime": False,
       "source": "abuse.ch URLhaus", "updatedAt": now.isoformat()})
print("online FR =", online, "| +24h =", added24h)
