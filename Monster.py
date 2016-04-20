import pygame
import random
from Design import Color,Layout

class AMonster:

    #constructor
    def __init__(self):
        #health
        self.health = 1
        #random spawn location
        #does not test if spwaning on player*************
        self.monsterX = random.randint(Layout.borderOffSet,Layout.screen_width-Layout.borderOffSet)
        self.monsterY = random.randint(Layout.borderOffSet,Layout.screen_height-Layout.borderOffSet)
        #dimensions
        self.monsterWidth = 50
        self.monsterHeight = 50
        #movement frequency
        self.delayTimer = 15
        self.delay = 0
        #movement shift
        monsterMove = 20
        #possible movements
        self.movements = ['up','down','left','right']
        self.values = {'up':(0,-monsterMove),'down':(0,monsterMove),'left':(-monsterMove,0),'right':(monsterMove,0)}
        
    #update monster position
    def update(self):
        if self.delay == 10:
            #random movement
            pair = self.values[self.movements[random.randint(0,len(self.movements)-1)]]		
            self.monsterX += pair[0]
            if self.monsterX > Layout.screen_width-self.monsterWidth/2-Layout.borderOffSet:
                self.monsterX = Layout.screen_width-self.monsterWidth/2-Layout.borderOffSet
            elif self.monsterX < self.monsterWidth/2+Layout.borderOffSet:
                self.monsterX = self.monsterWidth/2+Layout.borderOffSet
            self.monsterY += pair[1]
            if self.monsterY > Layout.screen_height-self.monsterHeight/2-Layout.borderOffSet:
                self.monsterY = Layout.screen_height-self.monsterHeight/2-Layout.borderOffSet
            elif self.monsterY < max(self.monsterHeight/2,Layout.topOffSet):
                self.monsterY = max(self.monsterHeight/2,Layout.topOffSet)
        self.delay += 1
        #reset delay
        if self.delay > self.delayTimer:
           self.delay = 0 
        
    def drawUpdate(self, gameDisplay):
        pygame.draw.rect(gameDisplay,Color.red,[self.monsterX - self.monsterWidth/2,self.monsterY - self.monsterHeight/2,self.monsterWidth,self.monsterHeight])	
