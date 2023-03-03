import pygame
import random

class Actor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self._rect = pygame.Rect(350,350,25,25)
        self._color = (random.randrange(255),random.randrange(255),random.randrange(255))
        self._rect.x = x
        self._rect.y = y

        # Movimento
        self._changeX = 0
        self._changeY = 0
        self._baseSpeed = 2
    
    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)
    
    def update(self, actors):
        self._rect.x += self._changeX
        self._rect.y += self._changeY
        # lista_colisao = checkcolision(self.rect, tilesexistentes)
    
    def goUp(self):
        self._changeY= -self._baseSpeed
    
    def goDown(self):
        self._changeY = self._baseSpeed
    
    def goRight(self):
        self._changeX = self._baseSpeed

    def goLeft(self):
        self._changeX = -self._baseSpeed
    
    def stopX(self):
        self._changeX = 0
    
    def stopY(self):
        self._changeY = 0