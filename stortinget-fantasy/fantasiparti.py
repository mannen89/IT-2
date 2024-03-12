from politiker import Politiker

class Fantasiparti:
    def __init__(self, navn: str, eier: str) -> None:
        self.navn: str = navn
        self.eier: str = eier
        self.poeng: int = 0
        self.saldo: int = 100_000
        self.partileder: Politiker = None
        self.politikere: list[Politiker] = []


    def __str__(self) -> str:
        #En spesiell metode som bestemmer hbordan print skal se ut
        return f"{self.navn} - {self.eier} - ({self.poeng} poeng, {self.saldo} kr)"
    
    def kjøp_politiker(self, politiker: Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.saldo -= politiker.verdi

    def selg_politiker(self, politiker: Politiker):
        if politiker in self.politikere:
            self

    def vis_parti(self):
        print(f"-- {self.navn} --")
        print(f"Poeng: {self.saldo}")
        print("Melemmer")
        for politiker in self.politikere:
            print(politiker)
            
if __name__ == "__main__":
    print("Tester Fantasiparti-klassen")
    testparti1 = Fantasiparti("Apolitisk Testparti", "Test Testesen")
    testparti2 = Fantasiparti("Politisk Testparti", "Stolt Jensenberg")
    print(testparti1)
    print(testparti2)