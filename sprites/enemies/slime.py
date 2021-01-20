import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import displaysurface
from ..enemy import Enemy

class Slime(Enemy):
  def __init__(self):
    super(Slime, self).__init__()
    self.image = pygame.image.load("assets/Enemy/Slime/Slime.png")
    self.image = pygame.transform.scale(self.image, (75, 40))
    self.rect = self.image.get_rect()
    self.attack_frames = 3

    self.vel.x, self.vel.y = random.randint(2, 6) / 2, random.randint(2, 6) / 2

  def move(self, player_pos):
    corrected_pos_x = self.pos.x + 40
    corrected_pos_y = self.pos.y + 40

    if player_pos[0] > corrected_pos_x:
      self.pos.x += self.vel.x
    elif player_pos[0] < corrected_pos_x:
      self.pos.x -= self.vel.x

    if player_pos[1] > corrected_pos_y:
      self.pos.y += self.vel.y
    elif player_pos[1] < corrected_pos_y:
      self.pos.y -= self.vel.y

    self.rect.center = self.pos

  def hit(self, player_group, player, enemy_stun_cooldown):
    hits = pygame.sprite.spritecollide(self, player_group, False)

    if hits and player.attacking:
      if self.stunned == False:
        if player.direction == "RIGHT" and player.pos.x < self.pos.x:
          self.hp -= 10
          self.stunned = True
          pygame.time.set_timer(enemy_stun_cooldown, 1000)
        elif player.direction == "LEFT" and player.pos.x + 20 > self.pos.x:
          self.hp -= 10
          self.stunned = True
          pygame.time.set_timer(enemy_stun_cooldown, 1000)
        