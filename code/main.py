
# pygame space shooter game
import pygame
from os.path import join

# initialise
pygame.init()

# window/display_surface
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter Game")
running = True

# plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 100

# image surfaces
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("darkgray")
    x += 0.5
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()
    


pygame.quit()