import pygame
from Design import Color, Layout
import math
import random


class Bullet:
  def __init__(self, x_coord, y_coord, angle): #x and y coords should just be player's coords, since it is shot out of the player
    self.x_coord = x_coord
    self.y_coord = y_coord
    self.angle = -math.radians(angle - 135) #angle needs to be calculated by the player when it calls shootBullet()
    self.speed = (10*math.cos(self.angle), 10*math.sin(self.angle))
    # self.speed = (1,1)
    self.isOffScreen = False
    
  def drawUpdate(self, gameDisplay): #moves the bullet according to velocity, then draws it
    if self.x_coord < Layout.screen_width and self.y_coord < Layout.screen_height: #checks if bullet is off screen
      self.x_coord += self.speed[0]
      self.y_coord += self.speed[1]
      pygame.draw.circle(gameDisplay, Color.green, [int(round(self.x_coord)), int(round(self.y_coord))], 5, 3)
    else:
      self.isOffScreen = True #this is here so player knows it can be deleted from the player's bulletList
    
