import os
import sys
import json
from politiker import Politiker

def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

#1. opsett
with open ("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)


representanter = data["representanter_liste"] # henter ut lista med representanter

# Opretter en liste med politker-objekter (objekter av klasse Politiker):
politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)
    
print("-- Velkommen til stortinget-fantasy --")  

print()
print("Du må stifte et parti for å spille spillet")
print("Hva skal partiet ditt hete?")
partinavn = input(">")
print("hva heter du?")
spillernavn = input(">")
print(f"Gratulerer! Det nye partiet {partinavn} ble stiftet med partilederen {spillernavn}")
input("Trukk enter for å starte spillet")

while True:
    rens_terminal()
    print("-- stortinget-fantasy --")
    print("1: Vis politikeroversikt")
    print("2: Avslutt")
    brukervalg = input("> ")

    if brukervalg == "1":
        print("politikeroversikt")
        for politker in politikere:
            print(politker)
        input("trykk enter for å gå tilbake til hovedmenyen")
    if brukervalg == "2":
        print("avslutter..")
        break
    else:
        print("ugyldig input")
        print("trykk enter for å komme tilbake til hovedmenyen")

print("Takk for nå")