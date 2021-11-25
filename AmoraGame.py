#Importing. . . -_-
import pygame
import sys
from GS import Gs
from SS import Ship
from EV import Events
#Preparating to start
pygame.init()
sc=Gs()
screen=pygame.display.set_mode((sc.screenw,sc.screenh))
sh=Ship(screen)
pygame.display.set_caption("This is a game")
Ev=Events()
#The Game
while True:
    Ev.e()
    if Ev.rk and sh.sr.right<sc.screenw:
        sh.sr.centerx+=2
    if Ev.lk and sh.sr.left>0:
        sh.sr.centerx-=2
    #TheImage
    screen.fill(sc.screencl)
    sh.Pts()
    pygame.display.flip()

