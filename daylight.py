import csv
from datetime import date, timedelta
from astral import LocationInfo
from astral.sun import sun

# --- Konfiguration für Winterthur ---
# Koordinaten: 47.49995 N, 8.72413 E
stadt = LocationInfo("Winterthur", "Switzerland", "Europe/Zurich", 47.49995, 8.72413)

# Zeitraum: Jahr 2024 (Schaltjahr)
start_datum = date(2024, 1, 1)
end_datum = date(2024, 12, 31)
delta = timedelta(days=1)

# Dateiname
dateiname = 'tageslaenge_winterthur_2024.csv'

print(f"Berechne Daten für {stadt.name}...")

with open(dateiname, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Header schreiben (optional, falls gewünscht - sonst Zeile löschen)
    writer.writerow(["Datum", "Tageslaenge_Stunden"])
    
    aktuelles_datum = start_datum
    while aktuelles_datum <= end_datum:
        # Sonnenstand berechnen
        s = sun(stadt.observer, date=aktuelles_datum)
        
        # Tageslänge berechnen (Sonnenuntergang - Sonnenaufgang)
        tageslaenge_timedelta = s['sunset'] - s['sunrise']
        
        # In Stunden umrechnen (Sekunden / 3600)
        stunden = tageslaenge_timedelta.total_seconds() / 3600
        
        # Formatierung: Datum YYYY-MM-DD, Stunden mit 6 Nachkommastellen
        writer.writerow([
            aktuelles_datum.strftime("%Y-%m-%d"), 
            f"{stunden:.6f}"
        ])
        
        aktuelles_datum += delta

print(f"Fertig! Die Datei '{dateiname}' wurde erstellt.")