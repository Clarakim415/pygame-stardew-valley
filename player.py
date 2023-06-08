import pygame as pg
from settings import *
from support import *
from timer import Timer

class Player(pg.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group) # the object will be in the group when the class instance is made
        
        self.import_assets()
        self.status = 'down'
        self.frame_index = 0
        
        # general setup 
        self.image = self.animations[self.status][self.frame_index]
        #self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)
        
        # movement attributes
        self.direction = pg.math.Vector2(x=0,y=0) # (Left&Right direction, Up&Down direction)
        self.pos = pg.math.Vector2(self.rect.center)
        self.speed = 200
        
        # timers
        self.timers = {
            'tool_use': Timer(350,self.use_tool)
        }
        
        #tools
        self.selected_tool = 'axe'
        
    def use_tool(self):
        print(self.selected_tool)
    
    def import_assets(self):
        self.animations = {'up':[],'down':[],'left':[],'right':[],
                           'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                           'right_hoe':[], 'left_hoe':[], 'up_hoe':[], 'down_hoe':[],
                           'right_axe':[], 'left_axe':[], 'up_axe':[], 'down_axe':[],
                           'right_water':[], 'left_water':[], 'up_water':[], 'down_water':[]
                           }
        
        for animation in self.animations.keys():
            path = 'graphics/character/' + animation
            self.animations[animation] = import_folder(path)
    
    def animate(self,dt):
        self.frame_index += 4*dt 
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
         
        self.image = self.animations[self.status][int(self.frame_index)]
    
    def input(self):
        keys = pg.key.get_pressed()
        
        # direction
        if keys[pg.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pg.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
            
        if keys[pg.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pg.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0
            
        # tool use    
        if keys[pg.K_SPACE]:
            self.timers['tool_use'].activate()
            
            
            
    def get_status(self):
        # if the player is not moving, add idle to the status
        if self.direction.magnitude() == 0: # not moving
            self.status = self.status.split('_')[0] + '_idle'   
            
        # tool use
        if self.timers['tool_use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool 
          
    def update_timers(self): 
        for timer in self.timers.values():
            timer.update()  
          
    def move(self,dt):
        
        # normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize() # in order to make equal speed (normalizing vector)
        
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
            
    def update(self,dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)