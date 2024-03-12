import os
import sys
import json

with open ("pokemon.json", "r", encoding="utf-8") as fil:
    alle_pokemon = json.load(fil)

def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

while True:
    rens_terminal
    print("1. Se pokemonoversikt")
    print("2. Se treneroversikt")
    print("3. Lag trener")
    print("4. Avslutt")
    brukervalg = input(">")
    if brukervalg == "1":
        print("-- Pokemonoversikt --")
        for pokemenn in alle_pokemon:
            print(pokemenn)
    input("Trykk enter for å gå tilbake til hovedmenyen")


