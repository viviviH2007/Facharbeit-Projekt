import pygame, sys
from settings import* #der Code von der Datei Setting wird hier auch verwendet
from overworld import Overworld

class Game:
    def __init__(self):
        self.max_level=3
        self.overworld = Overworld(0,self.max_level,screen)
        
    def run(self):
        self.overworld.run()

pygame.init()
screen=pygame.display.set_mode((10,10))
clock=pygame.time.Clock()
game=Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()
    
    pygame.display.update()
    clock.tick(60)