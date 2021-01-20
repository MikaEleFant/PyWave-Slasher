import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
import random

from config import vec, WIDTH, displaysurface

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.pos = vec(0, 0)
    self.vel = vec(0, 0)
    self.direction = random.randint(0, 1)
    self.hp = 20
    self.stunned = False

    if self.direction == 0:
      self.pos.x = 0
      self.pos.y = 260
    if self.direction == 1:
      self.pos.x = 700
      self.pos.y = 260

  def move(self, player_pos):
    if player_pos[0] > self.pos.x:
      self.pos.x += self.vel.x
    elif player_pos[0] < self.pos.x:
      self.pos.x -= self.vel.x

    if player_pos[1] > self.pos.y:
      self.pos.y += self.vel.y
    elif player_pos[1] < self.pos.y:
      self.pos.y -= self.vel.y

    self.rect.center = self.pos

  def render(self):
    displaysurface.blit(self.image, (self.pos.x, self.pos.y))

  def hit(self, player_group, player, enemy_stun_cooldown):
    hits = pygame.sprite.spritecollide(self, player_group, False)

    if hits and player.attacking:
      if self.stunned == False:
        if player.direction == "RIGHT" and player.pos.x < self.pos.x:
          self.hp -= 10
          self.stunned = True
          pygame.time.set_timer(enemy_stun_cooldown, player.normal_attack_frames * 100)
        elif player.direction == "LEFT" and player.pos.x > self.pos.x:
          self.hp -= 10
          self.stunned = True
          pygame.time.set_timer(enemy_stun_cooldown, player.normal_attack_frames * 100)
          
    if self.stunned == True:
      displaysurface.blit(player.attack_image, (self.pos.x, self.pos.y), (192, 192))