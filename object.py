import pygame
import random
import math
import os

SCISSOR_TYPE = 0
ROCK_TYPE = 1
PAPER_TYPE = 2

class Object():
    def __init__(self, x, y, type):
        self.rect = pygame.Rect((x, y, 50, 50))
        self.type = type
        self.xmove = 1
        self.ymove = 1
        self.speed = 4
        self.chase = 200
        base_path = os.path.dirname(__file__)
        # scissor = pygame.image.load(os.path.join(base_path, 'images/scissor.jpg'))
        # rock = pygame.image.load(os.path.join(base_path, 'images/rock.jpg'))
        # paper = pygame.image.load(os.path.join(base_path, 'images/paper.jpg'))
        scissor = pygame.image.load('images/scissor.jpg')
        rock = pygame.image.load('images/rock.jpg')
        paper = pygame.image.load('images/paper.jpg')
        self.images = [scissor, rock, paper]
        
    def draw(self, surface):
        image = self.images[self.type]
        image = pygame.transform.scale(image, (50, 50))
        surface.blit(image, self.rect)

    def move(self, screen_x, screen_y, objects):
        distances = []
        points = []
        if self.type == SCISSOR_TYPE:
            for obj in objects:
                if obj.type == PAPER_TYPE:
                    a = [self.rect.left, self.rect.top]
                    b = [obj.rect.left, obj.rect.top]
                    distances.append(math.dist(a,b))
                    points.append(b) 
        if self.type == ROCK_TYPE:
            for obj in objects:
                if obj.type == SCISSOR_TYPE:
                    a = [self.rect.left, self.rect.top]
                    b = [obj.rect.left, obj.rect.top]
                    distances.append(math.dist(a,b))
                    points.append(b)  
        if self.type == PAPER_TYPE:
            for obj in objects:
                if obj.type == ROCK_TYPE:
                    a = [self.rect.left, self.rect.top]
                    b = [obj.rect.left, obj.rect.top]
                    if math.dist(a,b) != 0:
                        distances.append(math.dist(a,b))
                        points.append(b)
        if len(distances):
            shortest = min(distances)  
            point = points[distances.index(shortest)]       
            if random.randint(1,10) > 3:
                x_move = point[0] - self.rect.left
                x_move = x_move / self.chase
                y_move = point[1] - self.rect.top
                y_move = y_move / self.chase
                self.rect.left += x_move * 1
                self.rect.top += y_move * 1
        self.xmove = random.randint(-1, 1)
        self.ymove = random.randint(-1, 1)
        if (self.rect.left <= 0):
            self.xmove = 1
        if (self.rect.right >= screen_x):
            self.xmove = -1
        if (self.rect.top <= 0):
            self.ymove = 1
        elif (self.rect.bottom >= screen_y):
            self.ymove = -1
        self.rect.x += self.xmove * self.speed
        self.rect.y += self.ymove * self.speed

    def collision(self, objects):
        for obj in objects:
            collision = pygame.Rect.colliderect(self.rect, obj.rect)
            if collision:
                self.collide(obj)
                
    def collide(self, obj):
        if self.type == SCISSOR_TYPE and obj.type == PAPER_TYPE:
            obj.type = SCISSOR_TYPE
        if self.type == ROCK_TYPE and obj.type == SCISSOR_TYPE:
            obj.type = ROCK_TYPE
        if self.type == PAPER_TYPE and obj.type == ROCK_TYPE:
            obj.type = PAPER_TYPE
            