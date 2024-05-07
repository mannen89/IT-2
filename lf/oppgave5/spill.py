import pygame
import random
from spiller import Spiller
from hinder import Hinder
from ball import Ball
 
# Oppsett av pygame
pygame.init()
BREDDE = 600 # bredde på vinduet
HOYDE = 600  # høyde på vinduet
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
kjorer = True
font = pygame.font.SysFont("Arial", 50)
 
# OPPSETT AV SPILL HER:
spiller1 = Spiller(25, HOYDE / 2)
spiller2 = Spiller(BREDDE - 25, HOYDE / 2)

# Plaserer ballen litt over midten i y-retning, for å unngå at den 
# treffer hinderet i midten
baller = [Ball(BREDDE / 2, 200)]

# 100 + i * 200 gir 100, 300 og 500:
hindere = []
for i in range(3):
    hindere.append(Hinder(BREDDE / 2, 100 + i * 200))

# må ha en variabel for å holde styr på tiden siden forrige nye ball ble laget,
# slik at vi ikke lager nye baller for ofte
tid_siden_forrige_nye_ball = 0


while kjorer:
    # fyll skjermen med en farge for å fjerne alt fra forrige frame
    vindu.fill("black")
    
    # Hendelser
    for hendelse in pygame.event.get():
        # pygame.QUIT hendelsen skjer når brukeren klikke på X for å lukke vinduet
        if hendelse.type == pygame.QUIT:
            kjorer = False
 
 
    # Input fra tastatur:
    taster = pygame.key.get_pressed()
    if taster[pygame.K_UP]:
        spiller1.flytt_opp()
    if taster[pygame.K_DOWN]:
        spiller1.flytt_ned()
    if taster[pygame.K_w]:
        spiller2.flytt_opp()
    if taster[pygame.K_s]:
        spiller2.flytt_ned()
 
    # Oppdater spill her:
    for ball in baller:
        ball.flytt()

        if ball.rect.y < 0 or ball.rect.y > HOYDE:
            ball.snu_y()

        if ball.rect.colliderect(spiller1.rect) or ball.rect.colliderect(spiller2.rect):
            if tid_siden_forrige_nye_ball > 60:
                # Fikk en bug her, hvor nye baller kunne bli sittende fast i spilleren.
                # Løsningen ble å sette x-posisjonen til nye baller litt til siden for 
                # spilleren, x-posisjonen er derfor satt til ball.rect.x - (ball.x_fart * 2),
                # som gjør at spilleren ikke treffer ballen igjen med en gang. 
                # Se på dette som et eksperttips -- løsninger med bugs godkjennes også.
                baller.append(Ball(ball.rect.x - (ball.x_fart * 2), ball.rect.y, -ball.x_fart, -ball.y_fart))
                tid_siden_forrige_nye_ball = 0
            ball.snu_x()

        if ball.rect.x < 0 or ball.rect.x > BREDDE:
            baller.remove(ball)
            if len(baller) == 0:
                baller.append(Ball(BREDDE / 2, 200))
            if ball.rect.x < 0:
                spiller1.poeng += 1
            else:
                spiller2.poeng += 1

        for hinder in hindere:
            if ball.rect.colliderect(hinder.rect):
                ball.snu_x()
    
    tid_siden_forrige_nye_ball += 1

    # Tegn på skjermen her:
    spiller1.tegn(vindu)
    spiller2.tegn(vindu)
    for ball in baller:
        ball.tegn(vindu)
    for hinder in hindere:
        hinder.tegn(vindu)

    poeng_spiller_1 = font.render(str(spiller1.poeng), True, "white")
    vindu.blit(poeng_spiller_1, (25, 25))
    poeng_spiller_2 = font.render(str(spiller2.poeng), True, "white")
    vindu.blit(poeng_spiller_2, (BREDDE - 50, 25))
 
 
    # flip() oppdater vinduet med alle endringer
    pygame.display.flip()
 
    # klokke.tick(60) begrenser spillet til 60 FPS (frames per second)
    klokke.tick(60) 
 
pygame.quit()