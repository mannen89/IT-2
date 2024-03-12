import json
 
fil = open("imdb.json", encoding="utf-8")
filmer = json.load(fil)
fil.close()
 
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