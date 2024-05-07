from figur import Figur
import random

class Ball(Figur):
    def __init__(self, x: int, y: int, x_fart: int = None, y_fart: int = None) -> None:
        super().__init__(x, y, 10, 10, "white")

        # Hvis x_fart eller y_fart ikke er satt, velg en tilfeldig retning
        if x_fart is None:
            x_fart = 3 if random.randint(0,1) == 1 else -3
        if y_fart is None:
            y_fart = 3 if random.randint(0,1) == 1 else -3
        self.x_fart = x_fart
        self.y_fart = y_fart

    def flytt(self) -> None:
        self.rect.x += self.x_fart
        self.rect.y += self.y_fart

    def snu_x(self) -> None:
        self.x_fart *= -1

    def snu_y(self) -> None:
        self.y_fart *= -1