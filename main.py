import pygame as pg
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
        pg.display.set_caption('pydew-valley') # set window name
        self.clock = pg.time.Clock() 
        self.level = Level()
        
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit(  )
                    sys.exit()
            
            dt = self.clock.tick()/1000
            self.level.run(dt)
            pg.display.update() # Update portions of the screen
            
if __name__ == '__main__': # check if we are in the main file
    game = Game()
    game.run()