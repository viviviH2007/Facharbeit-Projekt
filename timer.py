from pygame.time import get_ticks

class Timer:
    def __init__(self, duration, func = None, repeat = False):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False
        self.repeat = repeat

    def activate(self):
        self.active = True # start timer
        self.start_time = get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat:
            self.activate()

    def update(self): # will run and check all the time
        current_time = get_ticks()
        if current_time - self.start_time >= self.duration: # function till the duration cap
            if self.func and self.start_time !=0:
                self.func()
            self.deactivate()
