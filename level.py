import pygame as pg
from settings import *
from player import Player

class Level:
    def __init__(self):
        # allows the level to draw straight on the main display
        # get display surface
        self.display_surface = pg.display.get_surface()
        
        # sprite groups
        self.all_sprites = pg.sprite.Group()
        self.setup() 
        
    def setup(self):
        self.player = Player((640,340), self.all_sprites)
    
    def run(self,dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)