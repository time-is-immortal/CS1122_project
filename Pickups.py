import pygame
import random

class Pickup:
  def __init__(self, x_ coord, y_coord):
    #stores its location coords when pickup is spawned
    self.x_coord = x_coord
    self.y_coord = y_coord

class Health_Pickup(Pickup): #call this when player picks this up
  super().__init__()
  
  def gotPickedUp(self, player):
    player.health += 5
    
class Ammo_Pickup(Pickup): #call this when player picks this up
  super().__init__()
  
  def gotPickedUp(self, player):
    player.ammo += 50
  
