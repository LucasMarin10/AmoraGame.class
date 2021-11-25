#Importing. . .
import pygame
#The class
class Ship():
    """A class to definy the ship"""
    def __init__(self,screen):
        """The ship"""
        self.screen=screen
        self.si=pygame.image.load("ship.bmp")
        self.sr=self.si.get_rect()
        self.screenr=screen.get_rect()
        self.sr.centerx=self.screenr.centerx
        self.sr.bottom=self.screenr.bottom
    def Pts(self):
        """Drawing the ship"""
        self.screen.blit(self.si,self.sr)
        
