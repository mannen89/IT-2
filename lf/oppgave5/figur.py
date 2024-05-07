import pygame

class Figur:
    def __init__(self, x: int, y: int, bredde: int, hoyde: int, farge = str) -> None:
        self.surface = pygame.Surface((bredde, hoyde))
        self.rect = self.surface.get_rect()

        self.rect.center = (x, y)
        self.surface.fill(farge)
    
    def tegn(self, surface: pygame.Surface) -> None:
        surface.blit(self.surface, self.rect) 

