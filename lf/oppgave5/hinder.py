from figur import Figur

class Hinder(Figur):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 50, 50, "red")
