import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import displaysurface

class SlimeAttack(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/Enemy/Slime/Slime_Attack_Animation.png")
    self.attack_i = 0
    self.current_frame = [192, 192]

  def render(self, player):
    if self.attack_i >= 3000:
      self.attack_i = 0
      self.current_frame = [192, 192]
    if self.attack_i % 1000 == 0:
      self.current_frame[1] += 192
    self.attack_i += 1

    displaysurface.blit(self.image, (player.pos.x, player.pos.y), (self.current_frame[0], self.current_frame[1], 192, 192))