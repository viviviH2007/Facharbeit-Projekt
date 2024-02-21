import pygame
import sys
from settings import*
# Constants

FPS = 60
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
GROUND_HEIGHT = 50
JUMP_HEIGHT = 20
GRAVITY = 1

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_heigth - PLAYER_HEIGHT - GROUND_HEIGHT)
        self.vel_y = 0
        self.is_jump = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
        else:
            self.direction.x = 0

        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
                self.vel_y = -JUMP_HEIGHT

        if self.is_jump:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            if self.rect.bottom >= screen_heigth - GROUND_HEIGHT:
                self.is_jump = False
                self.rect.bottom = screen_heigth - GROUND_HEIGHT

# Initialize Pygame
clock = pygame.time.Clock()

# Create sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()