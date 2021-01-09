import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

vec = pygame.math.Vector2
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
HEIGHT = 350
WIDTH = 700

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))