import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()