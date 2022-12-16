import pygame

from static import setup_screen, setup_objects
from object import Object
import random

## GLOBAL
SCISSOR_TYPE = 0
ROCK_TYPE = 1
PAPER_TYPE = 2

## SETUP
# Setup screen and screen information
screen, SCREEN_WIDTH, SCREEN_HEIGHT = setup_screen()

# Setup clock
clock = pygame.time.Clock()

# Spawn all objects
objects = setup_objects(SCREEN_WIDTH, SCREEN_HEIGHT)

## GAME LOOP
run = True
while run:
    
    # Draw bg
    screen.fill((0, 0, 0))

    # Manage timescale
    clock.tick(60)
    
    # Draw objects, deal with movement and collision
    for obj in objects:
        obj.draw(screen)
        obj.move(SCREEN_WIDTH, SCREEN_HEIGHT, objects)
        obj.collision(objects)
    
    # Events
    for event in pygame.event.get():
        # Quit Event
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            run = False
      
    # Update window
    pygame.display.update()
    
pygame.quit()