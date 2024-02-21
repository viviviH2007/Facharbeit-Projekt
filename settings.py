import pygame,sys
from pytmx.util_pygame import load_pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
screen_heigth = 1000
screen_width = 1600
pygame.init()
screen= pygame.display.set_mode((screen_width,screen_heigth))
tmx_first= load_pygame('./data/tmx/first.tmx')
sprite_group = pygame.sprite.Group()
for layer in tmx_first.visible_layers:
    if hasattr(layer,'data'):
        for x,y,surf in layer.tiles():
            pos = (x * 32,y * 32)
            Tile(pos = pos, surf = surf, groups = sprite_group)

for obj in tmx_first.objects:
    pos = obj.x,obj.y
    Tile(pos = pos, surf = obj.image, groups = sprite_group )


#for obj in tmx_data.objects:
 #   pos = obj.x,obj.y
  #  if obj.image:
   #     Tile(pos = pos, surf = obj.image, groups = sprite_group)
#get layers
#print(tmx_data.layers)# get all layers
#for layer in tmx_data.visible_layers:
  #  print(layer)
#print(tmx_data.layernames)#get all layer names as dict
#print(tmx_data.get_layer_by_name('Kachelebene 1'))# get one layer by name

#for obj in tmx_data.objectgroups:#get object layers
#    print(obj)

#get tiles
#layer = tmx_data.get_layer_by_name('Kachelebene 1')
#for x,y,surf in layer.tiles():# get all the information
#    print(x*32)
#    print(y*32)
#    print(surf)
#get object

while True: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit
    sprite_group.draw(screen)
    pygame.display.update()