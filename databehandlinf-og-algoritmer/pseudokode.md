

Hent inn altall streams
Hvis antall streams er stlrre enn 30 000 000
    Returner antall streams gange 70% (0.7)
Ellers hvis antall streams er stlrre enn 1 400 000:
    Returner antall streams gange 40% (0.4)
Ellers:
    Returner 0


pseudo
SET antall_streams TO READ "hvor mange streams?"
IF antall_streams GREATER THAN 30 000 000
  THEN 


# Oppgave: Skriv algoritmen i vanlig python-kode:
antall_strams = int(input("Hvor mange streams?"))
if antall_streams > 30_000_000:
    print(antall_streams * 0.7)

    test
