def er_primtall(tall):
    for i in range(1, tall):
        if tall % i == 0:
            return True
        else:
            return False
        
print(er_primtall(17))

#koden funker men funksjonenn er_primtall er feil siden for alle verdier for tall så returnerer den True