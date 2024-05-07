def er_primtall(tall: int) -> bool:
    """
    Sjekker om et tall er et primtall.

    Parametere:
    tall (int): Tallet som skal sjekkes.

    Returnerer:
    bool: True hvis tallet er et primtall, ellers False.
    """
    for i in range(2, tall):
        if tall % i == 0:
            return False
    return True
