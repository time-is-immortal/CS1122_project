import pygame

class Bullet:
  def __init__(self, x_coord, y_coord):
    self.x_coord = x_coord
    self.y_coord = y_coord
    direction = (0, 0) #placeholder, later we make the direction according to the mouse's aim
    
  def drawUpdate(self):
    self.x_coord += 5
    self.y_coord += 5
