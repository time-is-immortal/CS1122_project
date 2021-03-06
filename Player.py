import pygame
import math
import random
from Design import *
from Bullet import Bullet

pygame.mixer.init()

class User:
    #constructor
    def __init__(self):
        #ammo
        self.ammo = PlayerConstants.AMMOLIMIT
        #health
        self.currentHealth = PlayerConstants.MAXHEALTH
        #bombs
        self.bombBeepHz = 0
        self.bombBeepDelay = 0
        self.bombDistanceSum = 0
        self.beepSounds = []
        for path in BombConstants.BEEP_SOUNDS:
            self.beepSounds.append(pygame.mixer.Sound(path))
        #spawn location 
        self.playerX = 300
        self.playerY = 300
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
        #represents the image
        self.image = pygame.transform.scale(pygame.image.load(GameImages.PLAYERIMAGE[self.currentFace]).convert_alpha(),(PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT))
        self.killCount = 0
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
    def update(self,healthPackList,ammoPackList,hiddenBombList,explosionAnimationList):
        self.checkDirection()
        #checks contact
        for healthPack in healthPackList:
            if CHECKRECT(self.playerX,self.playerY,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT,healthPack.x_coord,healthPack.y_coord,PickupConstants.WIDTH,PickupConstants.HEIGHT):
                healthPack.getPickedUp(self,healthPackList)
        #checks contact        
        for ammoPack in ammoPackList:
            if CHECKRECT(self.playerX,self.playerY,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT,ammoPack.x_coord,ammoPack.y_coord,PickupConstants.WIDTH,PickupConstants.HEIGHT):
                ammoPack.getPickedUp(self,ammoPackList)       
        #checks contact with bomb
        self.bombDistanceSum = 0
        for bomb in hiddenBombList:
            if not bomb.detonated:
                self.bombDistanceSum += bomb.distanceToPlayer(self)
                if bomb.checkCollisionsWithPlayer(self, explosionAnimationList):
                    self.explode()
        self.bombBeepHz = (1 - self.bombDistanceSum / BombConstants.BEEPRADIUS) * BombConstants.BEEPHERTZMAX if self.bombDistanceSum > 0 else 0
        if self.pLeft == True:
            self.PlayerXChange = -PlayerConstants.MOVE
        elif self.pRight is True:
            self.PlayerXChange = PlayerConstants.MOVE
        else:
            self.PlayerXChange = 0
        if self.pUp is True:
            self.PlayerYChange = -PlayerConstants.MOVE
        elif self.pDown is True:
            self.PlayerYChange = PlayerConstants.MOVE
        else:
            self.PlayerYChange = 0 
        #CHECKS THE BORDER BOUNDARIES  
        self.playerX += self.PlayerXChange
        if self.playerX > Layout.SCREEN_WIDTH-PlayerConstants.PLAYERWIDTH/2-Layout.BORDEROFFSET:
            self.playerX = Layout.SCREEN_WIDTH-PlayerConstants.PLAYERWIDTH/2-Layout.BORDEROFFSET
        elif self.playerX < PlayerConstants.PLAYERWIDTH/2+Layout.BORDEROFFSET:
            self.playerX = PlayerConstants.PLAYERWIDTH/2+Layout.BORDEROFFSET
        self.playerY += self.PlayerYChange
        if self.playerY > Layout.SCREEN_HEIGHT-PlayerConstants.PLAYERHEIGHT/2-Layout.BORDEROFFSET:
            self.playerY = Layout.SCREEN_HEIGHT-PlayerConstants.PLAYERHEIGHT/2-Layout.BORDEROFFSET
        elif self.playerY < PlayerConstants.PLAYERHEIGHT/2+Layout.TOPOFFSET:
            self.playerY = PlayerConstants.PLAYERHEIGHT/2+Layout.TOPOFFSET
        pos = pygame.mouse.get_pos()
        self.mouseX = pos[0]
        self.mouseY = pos[1]

    def shootBullet(self, state): #pew pew
        if self.ammo > 0:
            #state is 0 use the mouse
            if state == 0:
                offset = (self.mouseY-self.playerY, self.mouseX-self.playerX) #should calculate angle between player and mouse, unsure if this works
                angle = 135-math.degrees(math.atan2(*offset))
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
                elif self.currentFace == MoveConstants.UPRIGHT:
                    playerBullet = Bullet(self.playerX, self.playerY, 180)
                elif self.currentFace == MoveConstants.UPLEFT:
                    playerBullet = Bullet(self.playerX, self.playerY, -90)
                elif self.currentFace == MoveConstants.DOWNRIGHT:
                    playerBullet = Bullet(self.playerX, self.playerY, 90)
                elif self.currentFace == MoveConstants.DOWNLEFT:
                    playerBullet = Bullet(self.playerX, self.playerY, 0)
            pygame.mixer.Sound(Sounds.SHOOTSOUND).play()
            self.bulletList.append(playerBullet)
            self.ammo -= 1
            
    def loseHealth(self,num):
        pygame.mixer.Sound(Sounds.HITSOUND).play()
        self.currentHealth -= num
        if self.currentHealth < 0:
            self.currentHealth = 0
    
    def explode(self):
        # The player got blown up by a bomb.
        self.loseHealth(3)
    
##    def checkDiagonal(self):
##        if (self.pRight == True and self.pUp == True):
##            self.newFace = MoveConstants.UPRIGHT
##        elif (self.pRight == True and self.pDown == True):
##            self.newFace = MoveConstants.DOWNRIGHT
##        elif (self.pLeft == True and self.pUp == True):
##            self.newFace = MoveConstants.UPLEFT
##        elif (self.pLeft == True and self.pDown == True):
##            self.newFace = MoveConstants.DOWNLEFT

    def checkDirection(self):
        #caridinals
        if (self.pLeft == True):
            self.newFace = MoveConstants.LEFT
        elif (self.pRight == True):
            self.newFace = MoveConstants.RIGHT
        elif (self.pUp == True):
            self.newFace = MoveConstants.UP
        elif (self.pDown == True):
            self.newFace = MoveConstants.DOWN
        #diagonals
        if (self.pRight == True and self.pUp == True):
            self.newFace = MoveConstants.UPRIGHT
        elif (self.pRight == True and self.pDown == True):
            self.newFace = MoveConstants.DOWNRIGHT
        elif (self.pLeft == True and self.pUp == True):
            self.newFace = MoveConstants.UPLEFT
        elif (self.pLeft == True and self.pDown == True):
            self.newFace = MoveConstants.DOWNLEFT
    
    def reloadImage(self):
        if self.currentFace != self.newFace:
            self.image = pygame.transform.scale(pygame.image.load(GameImages.PLAYERIMAGE[self.newFace]).convert_alpha(),(PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT))
            self.currentFace = self.newFace
        return self.image    
        
    def drawUpdate(self, gameDisplay, framesPerSec):
        #player display
        gameDisplay.blit(self.reloadImage(),[self.playerX - PlayerConstants.PLAYERWIDTH/2,self.playerY - PlayerConstants.PLAYERHEIGHT/2,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT])
        #health bar
        pygame.draw.rect(gameDisplay,Color.RED,[(Layout.SCREEN_WIDTH-Layout.HEALTHBARWIDTH)+Layout.HEALTHBARWIDTH*(1-self.currentHealth/float(PlayerConstants.MAXHEALTH)),0,Layout.SCREEN_WIDTH,Layout.TOPOFFSET-1])
        if self.currentHealth <= 0:
            return True
        for index, bullet in enumerate(self.bulletList): #update every bullet on screen
            if bullet.isOffScreen:
                del self.bulletList[index]
            else:
                bullet.drawUpdate(gameDisplay)
        #play sound for bomb beep
        if self.bombBeepHz >= BombConstants.BEEPHERTZMIN:
            if self.bombBeepDelay >= framesPerSec / self.bombBeepHz:
                self.bombBeepDelay = 0
                # Play a sound
                #ping = BombConstants.BEEP_SOUNDS[int(min(self.bombDistanceSum / BombConstants.BEEPRADIUS * len(BombConstants.BEEP_SOUNDS), len(BombConstants.BEEP_SOUNDS) - 1))]
                #print(ping)
                #pygame.mixer.Sound(ping).play()
                self.beepSounds[int(min(self.bombDistanceSum / BombConstants.BEEPRADIUS * len(BombConstants.BEEP_SOUNDS), len(BombConstants.BEEP_SOUNDS) - 1))].play()
            else:
                self.bombBeepDelay += 1
        return False   
