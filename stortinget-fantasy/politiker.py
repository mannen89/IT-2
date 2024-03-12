class Politiker:
    def __init__(self, politiker_ordbok: dict) -> None:
        self.fornavn: str = politiker_ordbok["fornavn"]
        self.etternavn: str = politiker_ordbok["etternavn"]
        self.kjønn: str = "kvinne" if politiker_ordbok["kjoenn"] == 1 else "mann"
        self.fylke: str = politiker_ordbok["fylke"]["navn"]
        self.parti: str = politiker_ordbok["parti"]["navn"]
        self.komiteer = [komite["navn"] for komite in politiker_ordbok["komiteer_liste"]]
        self.ukepoeng: list[int] = []
        self.verdi: int = 1000
 
    def __str__(self) -> str:
        return f"{self.etternavn}, {self.etternavn} ({self.parti})"
    
    def gi_ukepoeng(self, poeng: int) -> None:
        self.ukepoeng.append(poeng)

    