import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
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
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT - GROUND_HEIGHT)
        self.vel_y = 0
        self.is_jump = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if not self.is_jump:
            if keys[pygame.K_SPACE]:
                self.is_jump = True
                self.vel_y = -JUMP_HEIGHT

        if self.is_jump:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            if self.rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
                self.is_jump = False
                self.rect.bottom = SCREEN_HEIGHT - GROUND_HEIGHT

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jump and Run")
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
    screen.fill(WHITE)
    pygame.draw.rect(screen, 'green', (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()