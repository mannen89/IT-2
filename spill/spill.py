import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spill")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

score = 0
score_okning = 1

font = pygame.font.Font(None, 36)

# Player properties
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10
player_vel = 1

# Platform properties
platform_width, platform_height = 200, 20
platform_x, platform_y = WIDTH // 2 - platform_width // 2, HEIGHT - platform_height - 50


# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(WHITE)  # Fill the screen with white color first

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_vel
    if keys[pygame.K_RIGHT]:
        player_x += player_vel
    if keys[pygame.K_UP]:
        player_y -= player_vel
    if keys[pygame.K_DOWN]:
        player_y += player_vel

    pygame.draw.rect(win, BLUE, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.rect(win, BLUE, (player_x, player_y, player_width, player_height))

    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    win.blit(score_text, (10, 10))  # Then blit the score text

    pygame.display.update()

pygame.quit()
