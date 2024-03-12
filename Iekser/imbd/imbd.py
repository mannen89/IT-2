import json
 
fil = open("imdb.json", encoding="utf-8")
filmer = json.load(fil)
fil.close()
 
# 1. Hvilken film har høyest karakter?
høyest = filmer[0]
for film in filmer:
    if film["karakter"] > høyest["karakter"]:
        høyest = film
print(f"Filmen med høyest karakter er {høyest['navn']}")
 
# 2. Hva er gjennomsnittskarakteren til filmene på listen?
total_karakter = 0
for film in filmer:
    total_karakter += film['karakter']
snittkarakter = total_karakter / len(filmer)
print(f"Gjennomsnittskarakteren til filmene er {snittkarakter}")
 
# 3. Hva er gjennomsnittskarakteren til de ti første filmene?
filmer_sortert = sorted(filmer, key=lambda film:film['karakter'], reverse=True) # sorterer listen i stigende rekkefølge etter karakter.
ti_første = filmer_sortert[:10] # lager en ny liste som inneholder de ti første filmene
total_karakter_ti_første = 0
for film in ti_første:
    total_karakter_ti_første += film['karakter']
snittkarakter_ti_første = total_karakter_ti_første / len(ti_første)
print(f"Gjennomsnittskarakteren til de ti første filmene er {snittkarakter_ti_første}")
 
# 4. Hvilken regissør har regissert flest filmer på listen?
regissører_antall = {}
for film in filmer:
    for regissør in film['regissører']:
        if regissør in regissører_antall:
            regissører_antall[regissør] += 1
        else:
            regissører_antall[regissør] = 1
            
print(regissører_antall)

regissører_sortert = sorted(regissører_antall.items(), key=lambda regissør: regissør[1], reverse=True)
print(f"Regissøren med flest filmer på listen er {regissører_sortert[0][0]} med {regissører_sortert[0][1]} filmer")
 
# Bonus: Det er faktisk fem regissører med syv filmer på listen.
for i in range(6):
    print(f"{i + 1}: {regissører_sortert[i][0]} - {regissører_sortert[i][1]} filmer")