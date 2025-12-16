# Importing the modules
import random
import pygame

class Button():
    def __init__(self,x,y,pos,width,height):
        self.x = x
        self.y = y
        self.pos = pos
        self.height = height
        self.width = width

    def Button_clicked(self, pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
    

class Start_RPS():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.screen = pygame.display.set_caption("RPS Brawl")