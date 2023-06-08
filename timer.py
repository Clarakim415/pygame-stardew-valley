import pygame as pg

class Timer:
    def __init__(self, duration, func=None):
        self.duration = duration
        self.func = func
        self.start_time = 0
        self.active = False
        
    def activate(self):
        self.active = True
        self.start_time = pg.time.get_ticks() 
        
    def deactivate(self):
        self.active = False
        self.start_time = 0
        
    def update(self):
        current_time = pg.time.get_ticks()
        
        if current_time - self.start_time >= self.duration:
            self.deactivate()