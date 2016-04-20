import pygame

class Bullet:
  def __init__(self, x_coord, y_coord): #x and y coords should just be player's coords, since it is shot out of the player
    self.x_coord = x_coord
    self.y_coord = y_coord
    velocity = (5, 5) #placeholder, later we make the direction according to the mouse's aim
    
  def drawUpdate(self, gameDisplay): #moves the bullet according to velocity, then draws it
    if self.x_coord < 800 and self.y_coord < 600: #checks if bullet is off screen
      self.x_coord += velocity[0]
      self.y_coord += velocity[1]
      pygame.draw.circle(gameDisplay, Color.black, [x_coord, y_coord, 10, 10], 3)
    else:
      pass
    
