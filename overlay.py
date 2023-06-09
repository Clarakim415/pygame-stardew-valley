import pygame as pg
from settings import *

class Overlay:
    def __init__(self, player):
        
        # general setup
        self.display_surface = pg.display.get_surface()
        self.player = player
        
        # imports
        overlay_path = 'graphics/overlay/'
        self.tools_surf = {tool: pg.image.load(overlay_path+tool+'.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pg.image.load(overlay_path+seed+'.png').convert_alpha() for seed in player.seeds}
        
    def display(self):
        
        # tools 
        tool_surf = self.tools_surf[self.player.selected_tool] 
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf, tool_rect)
        
        # seeds
        seed_surf = self.seeds_surf[self.player.selected_seed] 
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surface.blit(seed_surf, seed_rect)
        