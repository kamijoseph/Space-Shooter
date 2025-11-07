
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
clock = pygame.time.Clock()
FPS = 120

# player surfaces
x, y = 100, 150
player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1)
player_speed = 300


# stars surface
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

# meteor surface
meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser surface
laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))
 


running = True
while running:
    dt = clock.tick() / 1000
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
    
    # displaying meteor and laser
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # top and bottom wall touch 
    if player_rect.bottom > WINDOW_HEIGHT or player_rect.top < 0:
        player_direction.y *= -1
    
    # right and left wall touch
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction.x *= -1
    
    # moving the player with direction, speed and delta time
    player_rect.center += player_direction * player_speed * dt

    # displaying the player
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()
    

pygame.quit()