import pygame as pg
from os import walk

def import_folder(path):
    surface_list = []
    
    for __,__, img_files in walk(path): # walk returns ( root(folder name),dirs,files ) as tuple
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pg.image.load(full_path).convert_alpha() 
            surface_list.append(image_surf)
            
            
    return surface_list 