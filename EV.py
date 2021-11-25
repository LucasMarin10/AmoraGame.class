#Importing. . .
import pygame
import sys
#The class
class Events():
    """A class for the game events!"""
    def __init__(self):
        """Defining Keys. . ."""
        self.rk=False
        self.lk=False
    def e(self):
        """Quiting and Moving. . ."""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    self.rk=True
                elif event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    self.lk=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    self.rk=False
                elif event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    self.lk=False

