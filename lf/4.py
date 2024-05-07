import json
import math

with open("sykkelturer.json", encoding="utf-8") as file:
    data = json.load(file)

## Oppgave 1
### I denne oppgaven lager jeg en ordbok som teller antall turer fra hver stasjon,
### og sorterer denne ordboken med funksjonen sorted()

start_antall = {}

for tur in data:
    start = tur["start_station_name"]
    if start not in start_antall:
        start_antall[start] = 1
    else:
        start_antall[start] += 1

start_sortert = sorted(start_antall.items(), key=lambda stasjon: stasjon[1], reverse=True)
print(start_sortert[:5])

print()
print(" -- Mest populære starter -- ")
for i in range(5):
    print(f"{i + 1}: {start_sortert[i][0]}: {start_sortert[i][1]}")


## Oppgave 2
### "Trikset" i denne oppgaven er å gjøre om fra string til int før sortering
### Her lager jeg en ny liste med riktig format, og sorterer denne

turer_med_riktig_tid = []

for tur in data:
    tur["tid"] = int(tur["duration"])
    turer_med_riktig_tid.append(tur)

turer_sortert_tid = sorted(turer_med_riktig_tid, key=lambda tur: tur["tid"], reverse=True)

print()
print(" -- De tre lengste turene (tid) -- ")
for i in range(3):
    print(f"{i + 1}: {turer_sortert_tid[i]["start_station_name"]} -> {turer_sortert_tid[i]["end_station_name"]}: {turer_sortert_tid[i]["tid"]}s")

## Oppgave 3
### Her bruker jeg Pythagoras' setning for å regne ut distansen mellom to punkter,
### og lager en liste med ordbøker som inneholder distansen og stasjonavn

turer_distanse = []

for tur in data:
    start_pos = (float(tur["start_station_latitude"]), float(tur["start_station_longitude"]))
    slutt_pos = (float(tur["end_station_latitude"]), float(tur["end_station_longitude"]))
    distanse_x = slutt_pos[0] - start_pos[0]
    distanse_y = slutt_pos[1] - start_pos[1]
    distanse = math.sqrt(distanse_x ** 2 + distanse_y ** 2)
    
    turer_distanse.append({
        "distanse": distanse,
        "start": tur["start_station_name"],
        "slutt": tur["end_station_name"]
    })

sortert_distanse = sorted(turer_distanse, key=lambda tur:tur["distanse"], reverse=True)
print()
print("-- De tre lngste turene (distanse) --")
for i in range(3):
    print(f"{i + 1}: {sortert_distanse[i]["start"]} -> {sortert_distanse[i]["slutt"]}")
