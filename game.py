import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import FPS_CLOCK, FPS, displaysurface, hit_cooldown, enemy_stun_cooldown

from sprites.background import Background
from sprites.ground import Ground
from sprites.player import Player
from sprites.enemy import Slime

pygame.init() 

pygame.display.set_caption("Test Game")

background = Background()
ground = Ground()
player = Player()
slime = Slime()
enemy_group = pygame.sprite.Group()
enemy_group.add(slime)
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
  keys = pygame.key.get_pressed()
  player.gravity_check()

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
          
    if event.type == pygame.MOUSEBUTTONDOWN:
      if player.attacking == False:
          player.attack()
          player.attacking = True
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if player.attacking == False:
          player.attack()
          player.attacking = True

    if event.type == hit_cooldown:
      player.iframe = False
      pygame.time.set_timer(hit_cooldown, 0)

    if event.type == enemy_stun_cooldown:
      slime.stunned = False
      pygame.time.set_timer(enemy_stun_cooldown, 0)

  ground.render()

  background.render()

  if slime.hp != 0:
    slime.render()
  if not slime.stunned:
    slime.move(player.pos)

  player.move()
  player.update()
  player.hit(slime, enemy_group, hit_cooldown)
  slime.hit(player_group, player, enemy_stun_cooldown)
  if player.attacking == True:
    player.attack()
  if player.hp != 0:
    displaysurface.blit(player.image, player.rect)
  
  pygame.display.update()
  FPS_CLOCK.tick(FPS)