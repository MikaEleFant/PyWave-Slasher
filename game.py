import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import FPS_CLOCK, FPS
from sprites.background import Background
from sprites.ground import Ground

pygame.init() 

pygame.display.set_caption("Test Game")

background = Background()
ground = Ground()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
          
    if event.type == pygame.MOUSEBUTTONDOWN:
      pass
    
    if event.type == pygame.KEYDOWN:
      pass   

  background.render()
  ground.render()
  
  pygame.display.update()
  FPS_CLOCK.tick(FPS)