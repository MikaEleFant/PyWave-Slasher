import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import displaysurface

class Ground(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/Ground.png")
    self.rect = self.image.get_rect(center = (350, 350))

  def render(self):
    displaysurface.blit(self.image, (self.rect.x, self.rect.y))