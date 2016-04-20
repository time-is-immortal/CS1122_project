import pygame
from Player import User

#will initialize all modules
#have to have it
pygame.init()

#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grayish = (192,192,192)

#need to make a canvas
#requires a tuple (aka the size of windows)
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('BestNameEver!')

gameExit = False

#time for frames per sec
clock = pygame.time.Clock()
framesPerSec = 60
#player
player = User()


mouseX = 0
mouseY = 0

while not gameExit:
    #they take care of event handling
    #i.e. if arrow key is pressed, space bar is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        #Using Mouse to Move
        if event.type == pygame.MOUSEMOTION:
            (mouseX, mouseY) = pygame.mouse.get_pos()
        
        #Using Keypad to move
        if event.type == pygame.KEYDOWN:
            #left or right
            if event.key == pygame.K_LEFT:
                player.leftTrue()
            if event.key == pygame.K_RIGHT:
                player.rightTrue()
            #up or down
            if event.key == pygame.K_UP:
                player.upTrue()
            if event.key == pygame.K_DOWN:
                player.downTrue()
        if event.type == pygame.KEYUP:
            #player should stop moving
            #in said direction
            if event.key == pygame.K_LEFT:
                player.leftFalse()
            if event.key == pygame.K_RIGHT:
                player.rightFalse()
            if event.key == pygame.K_UP:
                player.upFalse()
            if event.key == pygame.K_DOWN:
                player.downFalse()

    #check collisions, game logic stuff
    #update graphcs to screen

    #make the color of the screen
    #will always be first
    gameDisplay.fill(white)
    #update the player
    player.update()
    player.drawUpdate(gameDisplay)
    #another way to draw rectangle
    #gameDisplay.fill(red, rect=[200,200,50,50])
    
    pygame.display.update()

    #frames per sec, try to avoid changing this in code, keep it as a const
    clock.tick(framesPerSec) 

#unnitializing pygame
pygame.quit()
#leave python
quit()
