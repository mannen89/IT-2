from figur import Figur

class Spiller(Figur):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 10, 150, "white")
        self.poeng = 0

    def flytt_opp(self) -> None:
        self.rect.y -= 5
    
    def flytt_ned(self) -> None:
        self.rect.y += 5

    