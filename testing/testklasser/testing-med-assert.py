


# Test drever utvukling med assert

## Eksempel en finksjon somt ester om tall er partall
def partall(tall: int):
    if tall % 2 == 0:
        return True
    else:
        return False
    
assert partall(2) == True
assert partall(1) == False
assert partall(-2) == True
assert partall(-1) == False