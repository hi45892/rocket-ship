import pygame, sys
from pygame.locals import QUIT
import time 

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("rocket ship")

player.x = 400
player.y = 300

player = pygame.image.load("chr.png")
background = pygame.image.load("bg1.png")

key = [False,False,False,False]
while player.y < 600:
      screen.blit(bg,(0,0))
      screen.blit(player,(player.x,player.y))
      pygame.display.flip()


for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type==pygame.KEYDOWN:
            if event.key ==K_UP:
                 keys[0]=True
            elif event.key==K_LEFT:
                 keys[1]=True
            elif event.key==K_DOWN:
                 keys[2]=True
            elif event.key==K_RIGHT:
                 keys[3]=True

        if event.type==pygame.KEYUP:
            if event.key ==K_UP:
                 keys[0]=False
            elif event.key==K_LEFT:
                 keys[1]=False
            elif event.key==K_DOWN:
                 keys[2]=False
            elif event.key==K_RIGHT:
                 keys[3]=False