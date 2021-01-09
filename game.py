import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from background import Background

pygame.init()  # Begin pygame
 
# Declaring variables to be used through the program
vec = pygame.math.Vector2
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
HEIGHT = 350
WIDTH = 700

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

while True:
  for event in pygame.event.get():
    # Will run when the close window button is clicked    
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
          
    # For events that occur upon clicking the mouse (left click) 
    if event.type == pygame.MOUSEBUTTONDOWN:
      pass

    # Event handling for a range of different key presses    
    if event.type == pygame.KEYDOWN:
      pass   