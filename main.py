from einstellung import*
from game_data import Level
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Za World')
        self.clock = pygame.time.Clock()
        
        self.tmx_maps = {0: load_pygame(join('.', 'data', 'tmx', 'first.tmx'))}
        self.current_stage = Level(self.tmx_maps[0])

    def run (self):
        while True:
            t = self.clock.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit

            self.current_stage.run(0.03)
            pygame.display.update()

if __name__== '__main__':        
    game = Game()
    game.run()