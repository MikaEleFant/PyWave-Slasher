import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import vec

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

  def move(self):
    if abs(self.vel.x) > 0.3:
      self.running = True
    else:
      self.running = False
  
  def update(self):
    pass
  
  def attack(self):
    pass

  def jump(self):
    pass