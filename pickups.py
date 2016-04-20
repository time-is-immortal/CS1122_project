import pygame
import random

class Pickup:
  def __init__(self):
    self.location_x = random.randint(0, 700) 
    self.location_y = random.randint(0,500) #need screen size
  
