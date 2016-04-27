import pygame
from Design import *

pygame.mixer.init()

class Pickups(object):
    def __init__(self,x_coord,y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
    
class HealthPickUp(Pickups):
    def __init__(self,x_coord,y_coord):
        super(HealthPickUp,self).__init__(x_coord,y_coord)
        self.imageSurface = pygame.transform.scale(pygame.image.load(GameImages.HEALTHIMAGE).convert_alpha(),(PickupConstants.WIDTH,PickupConstants.HEIGHT))
    def getPickedUp(self,player,healthPackList): #call this when player picks this up
        pygame.mixer.Sound(Sounds.PICKUPSOUND).play()
        player.currentHealth += PickupConstants.HEALTHRESTORE
        if player.currentHealth > PlayerConstants.MAXHEALTH:
            player.currentHealth = PlayerConstants.MAXHEALTH
        healthPackList.remove(self)
    def drawUpdate(self, gameDisplay):
        gameDisplay.blit(self.imageSurface,[self.x_coord - PickupConstants.WIDTH/2,self.y_coord - PickupConstants.HEIGHT/2,PickupConstants.WIDTH,PickupConstants.HEIGHT])  

class AmmoPickUp(Pickups):
    def __init__(self,x_coord,y_coord):
        super(AmmoPickUp,self).__init__(x_coord,y_coord)
        self.imageSurface = pygame.transform.scale(pygame.image.load(GameImages.AMMOIMAGE).convert_alpha(),(PickupConstants.WIDTH,PickupConstants.HEIGHT))
    def getPickedUp(self,player,ammoPackList): #call this when player picks this up
        pygame.mixer.Sound(Sounds.PICKUPSOUND).play()
        player.ammo += PickupConstants.AMMORESTORE
        if player.ammo > PlayerConstants.AMMOLIMIT:
            player.ammo = PlayerConstants.AMMOLIMIT
        ammoPackList.remove(self)
    def drawUpdate(self, gameDisplay):
        gameDisplay.blit(self.imageSurface,[self.x_coord - PickupConstants.WIDTH/2,self.y_coord - PickupConstants.HEIGHT/2,PickupConstants.WIDTH,PickupConstants.HEIGHT])
