import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

ACC = 0.15
FRIC = -0.05
FPS = 120
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
HEIGHT = 350
WIDTH = 700

hit_cooldown = pygame.USEREVENT + 1
enemy_stun_cooldown = pygame.USEREVENT + 1

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
vec = pygame.math.Vector2
