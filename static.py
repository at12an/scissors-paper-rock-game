import pygame
import random
from object import Object


## Initialise game window
def setup_screen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_info = pygame.display.Info()
    w = screen_info.current_w
    h = screen_info.current_h
    pygame.display.set_caption('Scissors Paper Rock!')
    pygame.display.flip()
    return screen, w, h

def setup_objects(w,h):
    objects = []
    for x in range(0,20):
        for y in range(0,3):
            obj = Object(random.randrange(0, w), random.randrange(0, h), y)
            objects.append(obj)
    return objects

    
