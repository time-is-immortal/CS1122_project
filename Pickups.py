import pygame

class Pickups:
  def __init__(self, x_coord, y_coord):
    self.x_coord = x_coord
    self.y_coord = y_coord
    
class HealthPickUp(Pickups):
  def __init__(self, x_coord, y_coord)
    super().__init__(x_coord, y_coord)
  def gotPickedUp(self, player): #call this when player picks this up
    player.health += 5
    
class AmmoPickUp(Pickups):
  def __init__(self, x_coord, y_coord)
    super().__init__(x_coord, y_coord)
  def gotPickedUp(self, player): #call this when player picks this up
    player.ammo += 5
    
