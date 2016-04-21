import pygame
from Bullet import Bullet
import math
from Design import Color,Layout

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
        #movement options, continous, noncontinous, mouse tracking
        self.PlayerXChange = 0
        self.PlayerYChange = 0
        self.pDown = False
        self.pUp = False
        self.pLeft = False
        self.pRight = False
        self.mouseX = 0
        self.mouseY = 0
        
        self.bulletList = [] #list of bullets on screen, will iterate through to update their positions
        
    #change movement
    #yes moving
    #player moves in direction of key
    def leftTrue(self):
        self.pLeft = True
    def rightTrue(self):
        self.pRight = True
    def upTrue(self):
        self.pUp = True
    def downTrue(self):
        self.pDown = True
    #no moving
    #in direction you let go
    def leftFalse(self):
        self.pLeft = False
    def rightFalse(self):
        self.pRight = False
    def upFalse(self):
        self.pUp = False
    def downFalse(self):
        self.pDown = False

    
    #update
    #update player position
    def update(self):
        if self.pLeft == True:
            self.PlayerXChange = -5
        elif self.pRight is True:
            self.PlayerXChange = 5
        else:
            self.PlayerXChange = 0
        if self.pUp is True:
            self.PlayerYChange = -5
        elif self.pDown is True:
            self.PlayerYChange = 5
        else:
            self.PlayerYChange = 0   
        self.playerX += self.PlayerXChange
        if self.playerX > Layout.screen_width-self.playerWidth/2-Layout.borderOffSet:
            self.playerX = Layout.screen_width-self.playerWidth/2-Layout.borderOffSet
        elif self.playerX < self.playerWidth/2+Layout.borderOffSet:
            self.playerX = self.playerWidth/2+Layout.borderOffSet
        self.playerY += self.PlayerYChange
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
        # angle = 0 #placehlder
        playerBullet = Bullet(self.playerX, self.playerY, angle)
        self.bulletList.append(playerBullet)
        self.ammo -= 1

    def drawUpdate(self, gameDisplay):
        #player display
        pygame.draw.rect(gameDisplay,Color.black,[self.playerX - self.playerWidth/2,self.playerY - self.playerHeight/2,self.playerWidth,self.playerHeight])
        #health bar
        pygame.draw.rect(gameDisplay,Color.red,[(Layout.screen_width-Layout.healthBarWidth)+Layout.healthBarWidth*(1-self.currentHealth/float(self.maxHealth)),0,Layout.screen_width,Layout.topOffSet])
        
        for index, bullet in enumerate(self.bulletList): #update every bullet on screen
            if bullet.isOffScreen:
                del self.bulletList[index]
            else:
                bullet.drawUpdate(gameDisplay)
            
