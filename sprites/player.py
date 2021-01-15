import pygame
from pygame.locals import *
import sys
import random
from tkinter import filedialog
from tkinter import *

from config import vec, ACC, FRIC, WIDTH

run_animation_R = [
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite2_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite3_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite4_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite5_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite6_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png")
  ]
run_animation_L = [
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite2_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite3_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite4_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite5_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite6_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_L.png")
  ]
attack_animation_R = [
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack_R.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack2_R.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack3_R.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack4_R.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack5_R.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack5_R.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png")
]
attack_animation_L = [
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_L.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack_L.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack2_L.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack3_L.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack4_L.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack5_L.png"),
    pygame.image.load("assets/Player_Attack_Animations/Player_Attack5_L.png"),
    pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_L.png")
]

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("assets/Player_Movement_Animations/Player_Sprite_R.png")
    self.rect = self.image.get_rect()

    self.vx = 0
    self.pos = vec((340, 240))
    self.vel = vec(0, 0)
    self.acc = vec(0, 0)
    self.direction = "RIGHT"
    self.move_frame = 0
    self.attacking = False
    self.attack_frame = 0
    self.hp = 100
    self.iframe = False

  def move(self):
    self.acc = vec(0, 0)

    if abs(self.vel.x) > 0.15:
      self.running = True
    else:
      self.running = False

    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_a]:
      self.acc.x = -ACC
    elif pressed_keys[K_d]:
      self.acc.x = ACC
    if pressed_keys[K_w]:
      self.acc.y = -ACC
    elif pressed_keys[K_s]:
      self.acc.y = ACC

    self.acc.x += self.vel.x * FRIC
    self.acc.y += self.vel.y * FRIC
    self.vel += self.acc
    self.pos += self.vel + self.acc / 2

    if self.pos.x > WIDTH:
      self.pos.x = 0
    if self.pos.x < 0:
      self.pos.x = WIDTH

    self.rect.midbottom = self.pos

  def gravity_check(self):
    if self.pos.y >= 355:
      self.pos.y = 354
      self.vel.y = 0
    if self.pos.y <= 175:
      self.pos.y = 175
      self.vel.y = 0

  def update(self):
    if self.move_frame > 6:
      self.move_frame = 0
      return
    
    if self.running == True:
      if self.vel.x > 0:
        self.image = run_animation_R[round(self.move_frame)]
        self.direction = "RIGHT"
      elif self.vel.x < 0:
        self.image = run_animation_L[round(self.move_frame)]
        self.direction = "LEFT"
      self.move_frame += 0.25

    if abs(self.vel.x) < 0.1 and self.move_frame != 0:
      self.move_frame = 0
      if self.direction == "RIGHT":
        self.image = run_animation_R[self.move_frame]
      elif self.direction == "LEFT":
        self.image = run_animation_L[self.move_frame]
  
  def attack(self):
    if self.attack_frame > 7:
      self.attack_frame = 0
      self.attacking = False

    if self.direction == "RIGHT":
      self.image = attack_animation_R[round(self.attack_frame)]
    elif self.direction == "LEFT":
      self.attack_correction_L()
      self.image = attack_animation_L[round(self.attack_frame)]
    self.attack_frame += 0.25

  def attack_correction_L(self):
    if self.attack_frame == 1.25:
      self.pos.x -= 20
    if self.attack_frame == 6.5:
      self.pos.x += 20

  def hit(self, enemy, enemy_group, hit_cooldown):
    hits = pygame.sprite.spritecollide(self, enemy_group, False)

    if enemy.stunned == False:
      if hits and not self.attacking:
        if self.iframe == False:
          self.iframe = True
          self.hp -= 5
          pygame.time.set_timer(hit_cooldown, 1000)
    print(self.hp)

  def dead(self):
    if self.hp == 0:
      pass
    # death animation
    # show end game screen