import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import vec, ACC, FRIC, WIDTH

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png")
    self.rect = self.image.get_rect()

    self.vx = 0
    self.pos = vec((340, 240))
    self.vel = vec(0, 0)
    self.acc = vec(0, 0)
    self.direction = "RIGHT"
    self.jumping = False

  def move(self):
    self.acc = vec(0, 0.5)

    if abs(self.vel.x) > 0.3:
      self.running = True
    else:
      self.running = False

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_LEFT]:
      self.acc.x = -ACC
    if pressed_keys[K_RIGHT]:
      self.acc.x = ACC

    self.acc.x += self.vel.x * FRIC
    self.vel += self.acc
    self.pos += self.vel + self.acc / 2

    if self.vel.x > 0:
      self.image  = pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png")
    if self.vel.x < 0:
      self.image = pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_L.png")

    if self.pos.x > WIDTH:
      self.pos.x = 0
    if self.pos.x < 0:
      self.pos.x = WIDTH

    self.rect.midbottom = self.pos
  
  def update(self):
    pass
  
  def attack(self):
    pass

  def jump(self):
    pass