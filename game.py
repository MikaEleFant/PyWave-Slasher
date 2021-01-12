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

while True:
  keys = pygame.key.get_pressed()
  player.gravity_check(ground_group)

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
          
    if event.type == pygame.MOUSEBUTTONDOWN:
      if player.attacking == False:
          player.attack()
          player.attacking = True
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_w:
        player.jump(ground_group)
      if event.key == pygame.K_SPACE:
        if player.attacking == False:
          player.attack()
          player.attacking = True

  background.render()

  ground.render()

  player.move()
  player.update()
  if player.attacking == True:
    player.attack()
  displaysurface.blit(player.image, player.rect)
  
  pygame.display.update()
  FPS_CLOCK.tick(FPS)