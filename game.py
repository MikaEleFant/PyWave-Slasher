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
from sprites.enemies.slime import Slime
from sprites.attacks.slime_attack import SlimeAttack
from stage import stages

pygame.init() 

pygame.display.set_caption("Test Game")
stage = stages[0]

background = Background(stage["background"])
ground = Ground(stage["ground"])
player = Player()
slime = Slime()
slime_atk = SlimeAttack()
enemy_group = pygame.sprite.Group()
enemy_group.add(slime)
player_group = pygame.sprite.Group()
player_group.add(player)

hits = pygame.sprite.spritecollide(player, enemy_group, False)

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

  if player.hp != 0:
    displaysurface.blit(player.image, player.rect)
    player.move()
    player.update()
    if hits:
      # slime_atk.render(player)
      player.hit(slime, hit_cooldown)
  else:
    player.kill()
  
  if slime.hp != 0:
    slime.render()
    slime.hit(player_group, player, enemy_stun_cooldown)
  else:
    slime.kill()

  if player.attacking == True:
    player.attack()

  if not slime.stunned:
    slime.move(player.pos)

  # displaysurface.blit(player.image, player.rect)
  # slime_atk.render(player)
  
  pygame.display.update()
  FPS_CLOCK.tick(FPS)