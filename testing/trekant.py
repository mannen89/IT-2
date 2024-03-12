class Trekant:
    def __init__(self, grunnlinje: int, høyde: int) -> None:
        self.grunnlinje: int = grunnlinje
        self.høyde: int = høyde

    def areal(self):
        return (self.grunnlinje * self.høyde) / 2


if __name__ == "__main__":
    print("Testing")

    min_trektant = Trekant(10, 10)
    print(min_trektant.areal())