
# pygame space shooter game
import pygame
from os.path import join
from random import randint

# initialise
pygame.init()

# window/display_surface
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter Game")

# player surfaces
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
x, y = 100, 150

# stars surface
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]



running = True
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill("black")

    # displaying the stars surface
    for position in star_positions:
        display_surface.blit(
            star_surf,
            position
        )

    # displaying the player surface
    x += 0.5
    display_surface.blit(player_surf, (x, y))

    
    pygame.display.update()
    


pygame.quit()