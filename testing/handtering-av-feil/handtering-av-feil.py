#et programm som finner fødselsår basert på alder

år = 2024
try:
    alder = int(input("Hvor gammer er du?"))
    fødselsår = år - alder
    print(f"Du er født i {fødselsår}")
except:
    print("Ugyldig input. Input må være et tall")

print("Koden fortsetter...")

#et abbet eksempel
try:
    tall = int(input("Sjruv et ttakk: "))
except:
    print("Ygylifing input. Setter 'Ttal' til 10")
    tall = 10

print(tall)