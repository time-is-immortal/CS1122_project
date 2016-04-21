import pygame

class Pickups:
  def __init__(self, x_coord, y_coord):
    self.x_coord = x_coord
    self.y_coord = y_coord
    pickedUp = false
    
class HealthPickUp(Pickups):
  def __init__(self, x_coord, y_coord)
    super().__init__(x_coord, y_coord)
  def getPickedUp(self, player): #call this when player picks this up
    player.currentHealth += 5
    pickedUp = True
  def drawUpdate(self, gameDisplay):
    if not PickedUp:
      pass #placeholder
    
class AmmoPickUp(Pickups):
  def __init__(self, x_coord, y_coord)
    super().__init__(x_coord, y_coord)
  def getPickedUp(self, player): #call this when player picks this up
    player.ammo += 5
    pickedUp = True
  def drawUpdate(self, gameDisplay):
    if not PickedUp:
      pass #placeholder
    
