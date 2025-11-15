
# pygame space shooter game
import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    
    def update(self):
        print("ship is being updated........")

# initialise
pygame.init()


# window/display_surface
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter Game")
clock = pygame.time.Clock()
FPS = 120
x, y = 100, 150


all_sprites = pygame.sprite.Group()
player = Player(all_sprites)

# player surfaces
# player_surf = pygame.image.load(join("images", "player.png")).convert_alpha()
# player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# player_direction = pygame.math.Vector2(0, 0)
# player_speed = 300


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
    # delta time (dt)
    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        
    # user inputs
    # keys = pygame.key.get_pressed()
    # # moving left and righht
    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # # moving up and down
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    # # handling diagonal inconsistent speed
    # player_direction = player_direction.normalize() if player_direction else player_direction

    # # moving player with input
    # player_rect.center += player_direction * player_speed * dt

    all_sprites.update()

    # draw the game
    display_surface.fill("black")

    # displaying the stars surface
    for position in star_positions:
        display_surface.blit(
            star_surf,
            position
        )
    
    # displaying ship, meteor and laser
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    # display_surface.blit(player_surf, player_rect)
    all_sprites.draw(display_surface)

    pygame.display.update()
    

pygame.quit()