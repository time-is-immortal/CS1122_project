import pygame
import random
from Design import *

class AMonster:

    #constructor
    def __init__(self,monsterList,player):
        #health
        self.currentHealth = 3
        self.maxHealth = 3
        #dimensions
        self.monsterWidth = 50
        self.monsterHeight = 50
        #movement frequency
        self.delayTimer = random.randint(5,15)
        self.delay = 0
        #movement shift
        self.monsterMoveRate = 20
        #possible movement rates
        self.movements = [(0,-self.monsterMoveRate),(0,self.monsterMoveRate),(-self.monsterMoveRate,0),(self.monsterMoveRate,0)]
        
        #random spawn location
        #does not spawn on other monsters nor the player
        self.monsterX = random.randint(self.monsterWidth/2+Layout.BORDEROFFSET,Layout.SCREEN_WIDTH-Layout.BORDEROFFSET-self.monsterWidth/2)
        self.monsterY = random.randint(self.monsterHeight/2+Layout.TOPOFFSET,Layout.SCREEN_HEIGHT-Layout.BORDEROFFSET-self.monsterHeight/2)
        #checks to reload spawn location 
        i = 0
        while i < len(monsterList):
            if self.checkMonsterRect(player.playerX,player.playerY,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT) or monsterList[i].checkMonsterRect(self.monsterX,self.monsterY,self.monsterWidth,self.monsterHeight):
                i = -1
                self.monsterX = random.randint(self.monsterWidth/2+Layout.BORDEROFFSET,Layout.SCREEN_WIDTH-Layout.BORDEROFFSET-self.monsterWidth/2)
                self.monsterY = random.randint(self.monsterHeight/2+Layout.TOPOFFSET,Layout.SCREEN_HEIGHT-Layout.BORDEROFFSET-self.monsterHeight/2)
            i+=1
        #represents the image
        self.imageSurface = pygame.transform.scale(pygame.image.load(GameImages.MONSTERIMAGE).convert_alpha(),(self.monsterWidth,self.monsterHeight))
        
    #update monster position
    def update(self,monsterList,player):
        if self.currentHealth <= 0:
            # The monster is dead.
            monsterList.remove(self)
            return False
        if self.delay == self.delayTimer:
            #random movement
            pair = self.movements[random.randint(0,len(self.movements)-1)]
            #checks if movement chosen is not colliding with another monster
            i = 0
            while i < len(monsterList):
                if monsterList[i] is not self and monsterList[i].checkMonsterRect(self.monsterX+pair[0],self.monsterY+pair[1],self.monsterWidth,self.monsterHeight):
                    i = -1
                    pair = self.movements[random.randint(0,len(self.movements)-1)]
                i+=1
            #CHECKS THE BORDER BOUNDARIES 
            self.monsterX += pair[0]
            if self.monsterX > Layout.SCREEN_WIDTH-self.monsterWidth/2-Layout.BORDEROFFSET:
                self.monsterX = Layout.SCREEN_WIDTH-self.monsterWidth/2-Layout.BORDEROFFSET
            elif self.monsterX < self.monsterWidth/2+Layout.BORDEROFFSET:
                self.monsterX = self.monsterWidth/2+Layout.BORDEROFFSET
            self.monsterY += pair[1]
            if self.monsterY > Layout.SCREEN_HEIGHT-self.monsterHeight/2-Layout.BORDEROFFSET:
                self.monsterY = Layout.SCREEN_HEIGHT-self.monsterHeight/2-Layout.BORDEROFFSET
            elif self.monsterY < self.monsterHeight/2+Layout.TOPOFFSET:
                self.monsterY = self.monsterHeight/2+Layout.TOPOFFSET
        #checks if collides with player
        if self.checkMonsterRect(player.playerX,player.playerY,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT): 
            # The monster is dead.
            player.loseHealth(self.currentHealth)
            monsterList.remove(self)
            return False
        self.delay += 1
        #resets delay
        if self.delay > self.delayTimer:
           self.delay = 0 
        return True
        
    def drawUpdate(self, gameDisplay):
        #monster display
        gameDisplay.blit(self.imageSurface,[self.monsterX - self.monsterWidth/2,self.monsterY - self.monsterHeight/2,self.monsterWidth,self.monsterHeight])
        #health bar
        pygame.draw.rect(gameDisplay,Color.RED if self.currentHealth/self.maxHealth > .5 else Color.DARKRED if self.currentHealth/self.currentHealth > .25 else Color.GRAYISH,[(self.monsterX - self.monsterWidth/2)+self.monsterWidth*(1-(self.currentHealth/float(self.maxHealth))),self.monsterY - self.monsterHeight/2,self.monsterWidth*(self.currentHealth/float(self.maxHealth)),2])
        
    def gotHitByBullet(self):
        self.currentHealth -= 1
        
    def checkBulletHit(self, bullet):
        # Checks whether this monster was hit by a bullet
        if abs(bullet.x_coord - self.monsterX) <= self.monsterWidth / 2 and abs(bullet.y_coord - self.monsterY) <= self.monsterHeight / 2:
            # The bullet hit the monster!
            self.gotHitByBullet()
            bullet.remove()
            return True
        return False
       
    def checkBulletHitList(self, bulletList):
        for bullet in bulletList:
            if self.checkBulletHit(bullet):
                break
    
    #collision between two rectangles 
    def checkMonsterRect(self,otherX,otherY,otherWidth,otherHeight):
        if abs(otherX - self.monsterX) <= self.monsterWidth/2 + otherWidth/2 and abs(otherY - self.monsterY) <= self.monsterHeight/2 + otherHeight/2:
            return True
        return False