import pygame
from Bullet import Bullet
import math
from Design import *

class User:

    #constructor
    def __init__(self):
        #ammo
        self.ammo = 10
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
        #player face position
        self.newFace = MoveConstants.UP
        self.currentFace = MoveConstants.UP
        self.bulletList = [] #list of bullets on screen, will iterate through to update their positions
        #font
        self.font = pygame.font.SysFont("comicsansms", 20)
        #represents the image
        self.image = pygame.transform.scale(pygame.image.load(GameImages.playerImage[self.currentFace]).convert_alpha(),(self.playerWidth,self.playerHeight))
        
    #change movement
    #yes moving
    #player moves in direction of key
    def leftTrue(self):
        self.pLeft = True
        self.newFace = MoveConstants.LEFT
    def rightTrue(self):
        self.pRight = True
        self.newFace = MoveConstants.RIGHT
    def upTrue(self):
        self.pUp = True
        self.newFace = MoveConstants.UP
    def downTrue(self):
        self.pDown = True
        self.newFace = MoveConstants.DOWN
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
        #CHECKS THE BORDER BOUNDARIES  
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

    def shootBullet(self, state): #pew pew
        self.currentHealth -=1
        if self.ammo > 0:
            #state is 0 use the mouse
            if state == 0:
                offset = (self.mouseY-self.playerY, self.mouseX-self.playerX) #should calculate angle between player and mouse, unsure if this works
                angle = 135-math.degrees(math.atan2(*offset))
                print(angle)
                #angle = 0 #placeholder
                playerBullet = Bullet(self.playerX, self.playerY, angle)
                
            #state is 1 use space key
            elif state == 1:
                if self.currentFace == MoveConstants.UP:
                    playerBullet = Bullet(self.playerX, self.playerY, -135)
                elif self.currentFace == MoveConstants.DOWN:
                    playerBullet = Bullet(self.playerX, self.playerY, 45)
                elif self.currentFace == MoveConstants.LEFT:
                    playerBullet = Bullet(self.playerX, self.playerY, -45)
                elif self.currentFace == MoveConstants.RIGHT:
                    playerBullet = Bullet(self.playerX, self.playerY, 135)
            self.bulletList.append(playerBullet)
            self.ammo -= 1
            
    def reloadImage(self):
        if self.currentFace != self.newFace:
            self.image = pygame.transform.scale(pygame.image.load(GameImages.playerImage[self.newFace]).convert_alpha(),(self.playerWidth,self.playerHeight))
            self.currentFace = self.newFace
        return self.image    
        
    def drawUpdate(self, gameDisplay):
        #player display
        gameDisplay.blit(self.reloadImage(),[self.playerX - self.playerWidth/2,self.playerY - self.playerHeight/2,self.playerWidth,self.playerHeight])
        #health bar
        pygame.draw.rect(gameDisplay,Color.red,[(Layout.screen_width-Layout.healthBarWidth)+Layout.healthBarWidth*(1-self.currentHealth/float(self.maxHealth)),0,Layout.screen_width,Layout.topOffSet])
        #display ammo
        if self.ammo > 0:
            text = self.font.render("Ammo:" + str(self.ammo), True, Color.black)
        else:   
            text = self.font.render("No Ammo", True, Color.red)
        gameDisplay.blit(text,[Layout.ammoTextPadding,0,0,Layout.topOffSet])
        for index, bullet in enumerate(self.bulletList): #update every bullet on screen
            if bullet.isOffScreen:
                del self.bulletList[index]
            else:
                bullet.drawUpdate(gameDisplay)
            
