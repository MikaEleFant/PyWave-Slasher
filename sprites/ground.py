import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import displaysurface

class Ground(pygame.sprite.Sprite):
  def __init__(self, ground):
    super().__init__()
    self.image = pygame.image.load(ground)
    self.image = pygame.transform.scale(self.image, (732, 350))
    self.rect = pygame.Rect(0, 200, 732, 355)

  def render(self):
    displaysurface.blit(self.image, (0, 0))