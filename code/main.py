
# pygame space shooter game
import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300

        # laser cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # moving left, up, down and righht
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        # normalizing direction
        self.direction = self.direction.normalize() if self.direction else self.direction

        # moving player with input
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print("fire laser")
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, star_surf):
        super().__init__(groups)
        self.image = star_surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

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
star_surf = pygame.image.load(join("images", "star.png")).convert_alpha()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

# meteor surface
meteor_surf = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser surface
laser_surf = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))
 
# custom events: meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

running = True
while running:
    # delta time (dt)
    dt = clock.tick() / 1000

    # event loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        # if event.type == meteor_event:
        #     print("create meteor................")

    all_sprites.update(dt)

    # drawing the game
    display_surface.fill("black")
    all_sprites.draw(display_surface)
    pygame.display.update()
    

pygame.quit()