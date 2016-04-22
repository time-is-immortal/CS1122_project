import pygame
from Bullet import Bullet
import math
from Design import *

class User:

    #constructor
    def __init__(self):
        #ammo
        self.ammo = 9999999
        #health
        self.currentHealth = 10
        self.maxHealth = 10
        #spawn location 
        self.playerX = 300
        self.playerY = 300
        #dimensions
        self.playerWidth = 50
        self.playerHeight = 50
        #movement shift
        self.playerMoveRate = 5
        #last movement
        self.lastMoveIdx = -1
        #current move
        self.CurrentMoveIdx = -1
        #possible movement rates
        self.movements = [(0,-self.playerMoveRate),(0,self.playerMoveRate),(-self.playerMoveRate,0),(self.playerMoveRate,0)]
        self.mouseX = 0
        self.mouseY = 0
        
        self.bulletList = [] #list of bullets on screen, will iterate through to update their positions
        
    #change movement
    #yes moving
    #player moves in direction of key
    def playerMove(self,moveType):
        self.CurrentMoveIdx = moveType
    #no moving
    #in direction you let go
    def playerStop(self):
        self.lastMoveIdx = self.CurrentMoveIdx
        self.CurrentMoveIdx = -1
    #current move
    def locateCurrentMove(self):
        self.CurrentMoveIdx = -1
    #update
    #update player position
    def update(self):
        if(self.CurrentMoveIdx>=0):
            pair = self.movements[self.CurrentMoveIdx]
            #CHECKS THE BORDER BOUNDARIES  
            self.playerX += pair[0]
            if self.playerX > Layout.screen_width-self.playerWidth/2-Layout.borderOffSet:
                self.playerX = Layout.screen_width-self.playerWidth/2-Layout.borderOffSet
            elif self.playerX < self.playerWidth/2+Layout.borderOffSet:
                self.playerX = self.playerWidth/2+Layout.borderOffSet
            self.playerY += pair[1]
            if self.playerY > Layout.screen_height-self.playerHeight/2-Layout.borderOffSet:
                self.playerY = Layout.screen_height-self.playerHeight/2-Layout.borderOffSet
            elif self.playerY < self.playerHeight/2+Layout.topOffSet:
                self.playerY = self.playerHeight/2+Layout.topOffSet
        pos = pygame.mouse.get_pos()
        self.mouseX = pos[0]
        self.mouseY = pos[1]

    def shootBullet(self): #pew pew
        offset = (self.mouseY-self.playerY, self.mouseX-self.playerX) #should calculate angle between player and mouse, unsure if this works
        angle = 135-math.degrees(math.atan2(*offset))
        #angle = 0 #placehlder
        playerBullet = Bullet(self.playerX, self.playerY, angle)
        self.bulletList.append(playerBullet)
        self.ammo -= 1

    def drawUpdate(self, gameDisplay):
        #player display
        moveIdx = self.CurrentMoveIdx
        if moveIdx<0:
            moveIdx = self.lastMoveIdx
        playerForwardImage = GameImages.playerImage[moveIdx]
        gameDisplay.blit(pygame.transform.scale(pygame.image.load(playerForwardImage).convert_alpha(),(self.playerWidth,self.playerHeight)),[self.playerX - self.playerWidth/2,self.playerY - self.playerHeight/2,self.playerWidth,self.playerHeight])
        #health bar
        pygame.draw.rect(gameDisplay,Color.red,[(Layout.screen_width-Layout.healthBarWidth)+Layout.healthBarWidth*(1-self.currentHealth/float(self.maxHealth)),0,Layout.screen_width,Layout.topOffSet])
        
        for index, bullet in enumerate(self.bulletList): #update every bullet on screen
            if bullet.isOffScreen:
                del self.bulletList[index]
            else:
                bullet.drawUpdate(gameDisplay)
            
