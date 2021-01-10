import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import FPS_CLOCK, FPS, displaysurface

from sprites.background import Background
from sprites.ground import Ground
from sprites.player import Player

pygame.init() 

pygame.display.set_caption("Test Game")

background = Background()
ground = Ground()
player = Player()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

def gravity_check(entity):
  hits = pygame.sprite.spritecollide(entity, ground_group, False)
  if entity.vel.y > 0:
    if hits:
      lowest = hits[0]
      if entity.pos.y < lowest.rect.bottom:
        entity.pos.y = lowest.rect.top + 1
        entity.vel.y = 0
        entity.jumping = False

while True:
  gravity_check(player)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
          
    if event.type == pygame.MOUSEBUTTONDOWN:
      pass
    
    if event.type == pygame.KEYDOWN:
      pass

  background.render()
  ground.render()
  player.move()
  displaysurface.blit(player.image, player.rect)
  
  pygame.display.update()
  FPS_CLOCK.tick(FPS)