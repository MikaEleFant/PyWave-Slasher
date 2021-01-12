import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
import random

from config import vec, WIDTH, displaysurface

class Slime(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/Enemy/Slime.png")
    self.image = pygame.transform.scale(self.image, (75, 40))
    self.rect = self.image.get_rect()
    self.pos = vec(0, 0)
    self.vel = vec(0, 0)
    self.direction = random.randint(0, 1)

    self.vel.x = random.randint(2, 6) / 4

    if self.direction == 0:
      self.pos.x = 0
      self.pos.y = 260
    if self.direction == 1:
      self.pos.x = 700
      self.pos.y = 260

  def move(self):
    if self.pos.x >= (WIDTH - 60):
      self.direction = 1
    elif self.pos.x <= 0:
      self.direction = 0

    if self.direction == 0:
      self.pos.x += self.vel.x
    if self.direction == 1:
      self.pos.x -= self.vel.x

    self.rect.center = self.pos

  def render(self):
    displaysurface.blit(self.image, (self.pos.x, self.pos.y))