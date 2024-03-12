poeng = int(input("Hvor mange poeng fikk du? "))

if poeng < 50:
    print("Ikke Bestått")
elif poeng <= 69:
    print("Bestått")
elif poeng <= 89:
    print("Godt Bestått")
elif poeng <= 100:
    print("Meget godt bestått")
else:
    print("ikke gyldig poengsum")