while True:
    navn = input("Hva heter du? ")
    splittet_navn = navn.split
    antall_navn = len(splittet_navn)
    if antall_navn < 2:
        print("Ugtyldig input. Input må bestå av minst to navn.")
    else:
        break
fornavn = splittet_navn[0]
første_bokstav_etternavn = splittet_navn[-1][0]
mail = fornavn + første_bokstav_etternavn + "viken.no"