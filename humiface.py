
import pygame
import sys


class Gauge():
    def __init__(self, position = (0,0), size=(200,200), bgcolor = (200,200,200)):
        self.posX, self.posY = position
        self.sizeX, self.sizeY = size
        self.bgcolor = bgcolor
        self.color = pygame.color.Color('red')
        self.rect = pygame.Rect(self.posX, self.posY, self.sizeX, self.sizeY)
        self.minVal = 20.0
        self.maxval = 50.0
        self.value = 35.0
        self.unit = '°C'
        
    def update(self):
        pass

    def draw(self, surface):
        # redraw rectangle with bgColor
        pygame.draw.rect(surface, self.bgcolor, self.rect)
        pygame.draw.circle(surface, self.color, (int(self.posX + self.sizeX/2), int(self.posY)), int(self.sizeX/2), int(self.sizeX/4))


SCREEN_SIZE = (800, 480)
SCREEN_RECT = pygame.Rect(0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1])
BGCOLOR = (60, 60, 60)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

RUNNING = True


gauge = Gauge((50,70), (50,30), BGCOLOR)

while RUNNING:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            RUNNING = False
        if evt.type == pygame.KEYDOWN:
            RUNNING = False

    pygame.draw.rect(screen, BGCOLOR, SCREEN_RECT)
    
    gauge.update()
    gauge.draw(screen)    
    
    pygame.display.flip()