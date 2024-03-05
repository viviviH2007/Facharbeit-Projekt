from pygame.sprite import Group
from einstellung import*
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((40,63))
        self.image.fill('blue')

        # rects
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

        #movement
        self.direction = vector()
        self.speed = 300
        self.gravity = 600
        self.jump = False
        self.jump_height = 2.5


        # collision
        self.collision_sprites = collision_sprites
        self.on_surface = {'floor': False, 'left': False, 'right': False}

        # timer
        self.timers = { # list
            'wall jump': Timer(200),
            'jump window': Timer(300)
        }
        

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0,0)
        if not self.timers['wall jump'].active:# if timer active, no left or right input is active
            if keys[pygame.K_d]:
                input_vector.x +=2
            if keys[pygame.K_a]:
                input_vector.x -=2
            self.direction.x = input_vector.normalize().x if input_vector else input_vector.x # normalize only x

        if keys[pygame.K_SPACE]:
            self.jump = True
            


    def move(self, dt):
        # horizontal
        self.rect.x += self.direction.x * self.speed / 60
        self.collision('horizontal')

        #vertical
        if not self.on_surface['floor'] and any ((self.on_surface['left'], self.on_surface['right'])) and not self.timers['jump window'].active:
            self.direction.y = 0
            self.rect.y += self.gravity / 180
        else:
            self.direction.y += self.gravity / 60 / 120      # gravity
            self.rect.y += self.direction.y * self.speed / 60
            self.direction.y += self.gravity / 60 / 120
            
        if self.jump:
            if self.on_surface['floor']:
                self.direction.y = -self.jump_height
                self.timers['jump window'].activate()
            elif any((self.on_surface['left'], self.on_surface['right'])) and not self.timers['jump window'].active: # once the player is on the wall
                self.timers['wall jump'].activate() 
                self.direction.y = -self.jump_height
                self.direction.x = 1 if self.on_surface['left'] else -1
            self.jump = False

        self.collision('vertical')

    def check_contact(self):
        floor_rect = pygame.Rect(self.rect.bottomleft,(self.rect.width,2))
        right_rect = pygame.Rect(self.rect.topright + vector(0, self.rect.height / 4),(2, self.rect.height / 2)) # for wall jumps
        left_rect = pygame.Rect(self.rect.topleft + vector(-2, self.rect.height/4), (2,self.rect.height / 2))
        collide_rects = [sprite.rect for sprite in self.collision_sprites]

        #collisions
        self.on_surface['floor'] = True if floor_rect.collidelist(collide_rects) >=0 else False
        self.on_surface['right'] = True if right_rect.collidelist(collide_rects) >= 0 else False
        self.on_surface['left'] = True if left_rect.collidelist(collide_rects) >= 0 else False



    def collision(self, axis):
        for sprite in self.collision_sprites: # static rec
            if sprite.rect.colliderect(self.rect): # moving rec
                if axis == 'horizontal':
                    # left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right: # problem with the position and moveside of the player
                        self.rect.left = sprite.rect.right

                    # right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left: 
                        self.rect.right = sprite.rect.left

                else: # vertical # top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom: 
                        self.rect.top = sprite.rect.bottom
                        # bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top: 
                        self.rect.bottom = sprite.rect.top
                    self.direction.y = 0

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()



    def update(self, t):
        self.old_rect = self.rect.copy()
        self.update_timers()
        self.input()
        self.move(t)
        self.check_contact()