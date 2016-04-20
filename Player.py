import pygame

#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grayish = (192,192,192)

class User:

    playerX = 300
    playerY = 300
    playerWidth = 50
    playerHeight = 50
    PlayerXChange = 0
    PlayerYChange = 0
    pDown = False
    pUp = False
    pLeft = False
    pRight = False
    mouseX = 0
    mouseY = 0

    #constructor
    #idk what to write
    
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
        self.playerY += self.PlayerYChange

    def drawUpdate(self, gameDisplay):
        pygame.draw.rect(gameDisplay, black, [self.playerX,self.playerY,self.playerWidth,self.playerHeight])
