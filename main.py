import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Spiel")
clock = pygame.time.Clock()

test_surface = pygame.image.load("")

while True: #Auf dieser Schleife aufgebaut
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()       
    screen.blit(test_surface,(0,0)) # Nullpunkt ist Oben Links
    # alle Elemente
    
    pygame.display.update()
    clock.tick(60) # Begrenzung der Frame-Rate für die Geschwindigkeit des Spiels 
