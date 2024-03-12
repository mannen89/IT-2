# Et program som fortsetter helt til brueker har skrevet riktig input

år = 2024

while True:
    try:
        alder = int(input("Hvor gammel blir du i år? "))
        break
    except:
        print("Ugyldig input. Input må være et tall")

fødselsår = år - alder
print(F"Du er født i {fødselsår}")

# tips til 3.14
navn = "Noah Storm Nordli"
splittet_navn = navn.split(" ")
antall_navn = len(splittet_navn)     