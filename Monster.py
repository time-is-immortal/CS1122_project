import pygame
import random
import thread
import time
from Design import *
from Pickups import *

class AMonster:
    #constructor
    def __init__(self,monsterList,player,monsterLevel):
        self.monsterLevel = monsterLevel
        #health
        self.maxHealth = self.currentHealth = MonsterConstants.MONSTERSTATS[monsterLevel][0]
        #dimensions
        self.monsterWidth = MonsterConstants.MONSTERSTATS[monsterLevel][1]
        self.monsterHeight = MonsterConstants.MONSTERSTATS[monsterLevel][2]
        #movement frequency
        self.delayTimer = MonsterConstants.MONSTERSTATS[monsterLevel][3]
        #spawn deplay
        self.delay = MonsterConstants.SPAWNDELAY*(monsterLevel+1)
        #movement shift
        self.monsterMoveRate = MonsterConstants.MONSTERSTATS[monsterLevel][4]
        #possible movement rates
        self.movements = [(0,-self.monsterWidth/self.monsterMoveRate),(0,self.monsterWidth/self.monsterMoveRate),(-self.monsterHeight/self.monsterMoveRate,0),(self.monsterHeight/self.monsterMoveRate,0),(0,0)]
        #is alive
        self.state = True
        #random spawn location
        #does not spawn on other monsters or the player
        self.monsterX = random.randint(self.monsterWidth/2+Layout.BORDEROFFSET,Layout.SCREEN_WIDTH-Layout.BORDEROFFSET-self.monsterWidth/2)
        self.monsterY = random.randint(self.monsterHeight/2+Layout.TOPOFFSET,Layout.SCREEN_HEIGHT-Layout.BORDEROFFSET-self.monsterHeight/2)
        #checks to reload spawn location 
        i = 0
        while i < len(monsterList):
            if CHECKRECT(self.monsterX,self.monsterY,self.monsterWidth,self.monsterHeight,player.playerX,player.playerY,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT) or CHECKRECT(monsterList[i].monsterX,monsterList[i].monsterY,monsterList[i].monsterWidth,monsterList[i].monsterHeight,self.monsterX,self.monsterY,self.monsterWidth,self.monsterHeight):
                i = -1
                self.monsterX = random.randint(self.monsterWidth/2+Layout.BORDEROFFSET,Layout.SCREEN_WIDTH-Layout.BORDEROFFSET-self.monsterWidth/2)
                self.monsterY = random.randint(self.monsterHeight/2+Layout.TOPOFFSET,Layout.SCREEN_HEIGHT-Layout.BORDEROFFSET-self.monsterHeight/2)
            i+=1
        #represents the image
        self.imageSurface = pygame.transform.scale(pygame.image.load(GameImages.MONSTERIMAGE).convert_alpha(),(self.monsterWidth,self.monsterHeight))
    
    #show monster player contact
    def flash_Monster(self,monsterList):
        self.currentHealth = 0
        self.state = False
        time.sleep(.25)
        monsterList.remove(self)   
        
    #update monster position
    def update(self,monsterList,player,gameDisplay,healthPackList,ammoPackList):
        if not self.state:
            return True
        if self.currentHealth <= 0:
            # The monster is dead.
            monsterList.remove(self)
            player.killCount+=1
            spawnRate = random.random()
            if spawnRate < PickupConstants.RATESPAWN*(self.monsterLevel+1):
                healthPackList.append(HealthPickUp(self.monsterX,self.monsterY))
            elif spawnRate > 1-PickupConstants.RATESPAWN*(self.monsterLevel+1):
                ammoPackList.append(AmmoPickUp(self.monsterX,self.monsterY))
            return False
        if self.delay == self.delayTimer:
            #random movement
            pair = self.movements[self.locatePlayer(player)]
            #checks if movement chosen is not colliding with another monster
            i = 0
            while i < len(monsterList):
                if monsterList[i] is not self and CHECKRECT(monsterList[i].monsterX,monsterList[i].monsterY,monsterList[i].monsterWidth,monsterList[i].monsterHeight,self.monsterX+pair[0],self.monsterY+pair[1],self.monsterWidth,self.monsterHeight):
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
        if CHECKRECT(self.monsterX,self.monsterY,self.monsterWidth,self.monsterHeight,player.playerX,player.playerY,PlayerConstants.PLAYERWIDTH,PlayerConstants.PLAYERHEIGHT): 
            # The monster is dead.
            player.loseHealth(self.currentHealth)
            player.killCount+=1
            try:
                thread.start_new_thread(self.flash_Monster,(monsterList,))
            except:
                print "Error: unable to start "
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
        pygame.draw.rect(gameDisplay,Color.RED if self.currentHealth/float(self.maxHealth) > .5 else Color.DARKRED if self.currentHealth/float(self.maxHealth) > .25 else Color.GRAYISH,[(self.monsterX - self.monsterWidth/2)+self.monsterWidth*(1-(self.currentHealth/float(self.maxHealth))),self.monsterY - self.monsterHeight/2,self.monsterWidth*(self.currentHealth/float(self.maxHealth)),2])
        
    def gotHitByBullet(self):
        self.currentHealth -= 1
        if self.currentHealth < 0:
            self.currentHealth = 0
        
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
    
    def locatePlayer(self,player):
        w = self.monsterX - player.playerX
        h = self.monsterY - player.playerY
        if abs(w) < 2*PlayerConstants.PLAYERWIDTH or abs(h) < 2*PlayerConstants.PLAYERHEIGHT:
            if abs(w) > abs(h):
                if w <=0:
                    return MoveConstants.RIGHT
                return MoveConstants.LEFT
            if h <=0:
                return MoveConstants.DOWN
            return MoveConstants.UP
        if(w<0 and h<0):
            return MoveConstants.RIGHT if random.randint(0,1) == 1 else MoveConstants.DOWN
        if(w>0 and h>0):
            return MoveConstants.LEFT if random.randint(0,1) == 1 else MoveConstants.UP    
        if(w>0 and h<0):
            return MoveConstants.LEFT if random.randint(0,1) == 1 else MoveConstants.DOWN
        if(w<0 and h>0):
            return MoveConstants.RIGHT if random.randint(0,1) == 1 else MoveConstants.UP
            
        