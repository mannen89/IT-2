import json
with open("stortinget.json", encoding="utf-8") as fil:
    data = json.load(fil)
 
politikere = data["representanter_liste"]

 
# 1. Lag en for-løkke som printer navn og tilhørnde parti på alle politikerne
for politiker in politikere:
    print(f"{politiker['fornavn']} {politiker['etternavn']}: {politiker['parti']['navn']}")



# 2. Lag en ordbok som teller antall representanter hvert parti har
antall = {}
for politiker in politikere:
    parti = politiker['parti']['navn']
    if parti not in antall:
        antall[parti] = 1
    else:
        antall[parti] += 1
print(antall)

antall_liste = list(antall.items())
antall_sortert = sorted(antall_liste, key=lambda parti:parti[1])
parti_flest = antall_sortert[-1]
print(f"Partiet med flest politikeret på tinget er {parti_flest[0]} med {parti_flest[1]} representanter")

import matplotlib.pyplot as plt  
parti_liste = list(antall.keys())
antall_liste = list(antall.values())
plt.bar(parti_liste, antall_liste)
plt.xticks(rotation=90)
plt.show()

total = 0
for parti in antall:
    total += antall[parti]
snitt = total / len(antall)
print(f"hvert parti har i snitt {snitt} representanter")