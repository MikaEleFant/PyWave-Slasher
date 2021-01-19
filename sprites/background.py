import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import displaysurface

class Background(pygame.sprite.Sprite):
  def __init__(self, background):
    super().__init__()
    self.bgimage = pygame.image.load(background)
    self.bgimage = pygame.transform.scale(self.bgimage, (732, 300))
    self.bgX = 0
    self.bgY = 0

  def render(self):
    displaysurface.blit(self.bgimage, (self.bgX, self.bgY))