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
        self.lastMoveIdxX = -1
        self.lastMoveIdxY = -1
        #current move in X
        self.CurrentMoveIdx = -1
        self.CurrentMoveIdxX = -1
	#current move in Y
        self.CurrentMoveIdxY = -1
        #possible movement rates
        self.movements = [(0,-self.playerMoveRate),(0,self.playerMoveRate),(-self.playerMoveRate,0),(self.playerMoveRate,0)]
	self.moveIdx = 0
        self.mouseX = 0
        self.mouseY = 0
        
        self.pDown = False
        self.pUp = False
        self.pLeft = False
        self.pRight = False
        #0 = up, 1 = right, 2 = down, 3 = left
	self.currentFace = 0	
        self.bulletList = [] #list of bullets on screen, will iterate through to update their positions
        
    #change movement
    #yes moving
    #player moves in direction of key
    def playerMoveX(self,moveType):
        self.CurrentMoveIdxX = moveType
    #no moving
    #in direction you let go
    def playerStopX(self):
        self.lastMoveIdxX = self.CurrentMoveIdxX
        self.CurrentMoveIdxX = -1
    
    def playerMoveY(self,moveType):
        self.CurrentMoveIdxY = moveType
    #no moving
    #in direction you let go
    def playerStopY(self):
        self.lastMoveIdxY = self.CurrentMoveIdxY
        self.CurrentMoveIdxY = -1
    #current move
    def locateCurrentMove(self):
        self.CurrentMoveIdx = -1
        #return self.CurrentMoveIdx
    
	#player moves in direction of key
    def leftTrue(self):
        self.pLeft = True
        self.pRight = False
        self.playerMoveX(MoveConstants.LEFT)
        self.currentFace = 3
    def rightTrue(self):
        self.pRight = True
        self.pLeft = False
        self.playerMoveX(MoveConstants.RIGHT)
        self.currentFace = 2
    def upTrue(self):
        self.pUp = True
        self.pDown = False
        self.playerMoveY(MoveConstants.UP)
        self.currentFace = 0
    def downTrue(self):
        self.pDown = True
        self.pUp = False
        self.playerMoveY(MoveConstants.DOWN)
        self.currentFace = 1
    #no moving
    #in direction you let go
    def leftFalse(self):
        self.pLeft = False
        self.playerStopX()
    def rightFalse(self):
        self.pRight = False
        self.playerStopX()
    def upFalse(self):
        self.pUp = False
        self.playerStopY()
    def downFalse(self):
        self.pDown = False
        self.playerStopY()
	
	
	
	
	#update
    #update player position
    def update(self):
	if(self.CurrentMoveIdxX>=0):
            pair = self.movements[self.CurrentMoveIdxX]
            #CHECKS THE BORDER BOUNDARIES  
            self.playerX += pair[0]
            if self.playerX > Layout.screen_width-self.playerWidth/2-Layout.borderOffSet:
                self.playerX = Layout.screen_width-self.playerWidth/2-Layout.borderOffSet
            elif self.playerX < self.playerWidth/2+Layout.borderOffSet:
                self.playerX = self.playerWidth/2+Layout.borderOffSet
        if(self.CurrentMoveIdxY>=0):
            pair = self.movements[self.CurrentMoveIdxY]
            self.playerY += pair[1]
			#CHECKS THE BORDER BOUNDARIES 
            if self.playerY > Layout.screen_height-self.playerHeight/2-Layout.borderOffSet:
                self.playerY = Layout.screen_height-self.playerHeight/2-Layout.borderOffSet
            elif self.playerY < self.playerHeight/2+Layout.topOffSet:
                self.playerY = self.playerHeight/2+Layout.topOffSet
        pos = pygame.mouse.get_pos()
        self.mouseX = pos[0]
        self.mouseY = pos[1]

    def shootBullet(self, state): #pew pew
        #state is 0 use the mouse
        if state == 0:
            offset = (self.mouseY-self.playerY, self.mouseX-self.playerX) #should calculate angle between player and mouse, unsure if this works
            angle = 135-math.degrees(math.atan2(*offset))
            print(angle)
            #angle = 0 #placehlder
            playerBullet = Bullet(self.playerX, self.playerY, angle)
            self.bulletList.append(playerBullet)
            self.ammo -= 1
        #state is 1 use space key
        elif state == 1:
            #Up is 224 degrees
            #right is 133
            #down is 42
            #left is 314
            if self.currentFace == 0:
                playerBullet = Bullet(self.playerX, self.playerY, 224)
                self.bulletList.append(playerBullet)
                self.ammo -= 1
                
    def drawUpdate(self, gameDisplay):
        #player display
	if self.pLeft == True or self.pRight == True:
            self.moveIdx = self.CurrentMoveIdxX
	elif self.pUp == True or self.pDown == True:
            self.moveIdx = self.CurrentMoveIdxY
        if self.moveIdx<0:
            self.moveIdx = self.lastMoveIdx
        playerForwardImage = GameImages.playerImage[self.moveIdx]
        gameDisplay.blit(pygame.transform.scale(pygame.image.load(playerForwardImage).convert_alpha(),(self.playerWidth,self.playerHeight)),[self.playerX - self.playerWidth/2,self.playerY - self.playerHeight/2,self.playerWidth,self.playerHeight])
        #health bar
        pygame.draw.rect(gameDisplay,Color.red,[(Layout.screen_width-Layout.healthBarWidth)+Layout.healthBarWidth*(1-self.currentHealth/float(self.maxHealth)),0,Layout.screen_width,Layout.topOffSet])
        
        for index, bullet in enumerate(self.bulletList): #update every bullet on screen
            if bullet.isOffScreen:
                del self.bulletList[index]
            else:
                bullet.drawUpdate(gameDisplay)
            
