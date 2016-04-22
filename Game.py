import pygame
from Player import User
from Design import *
from Monster import AMonster

#will initialize all modules
#have to have it
pygame.init()

#need to make a canvas
#requires a tuple (aka the size of windows)
gameDisplay = pygame.display.set_mode((Layout.screen_width,Layout.screen_height))
pygame.display.set_caption('BestNameEver!')

gameExit = False

#current level
level = 10

#time for frames per sec
clock = pygame.time.Clock()
framesPerSec = 60

#player
player = User()

#list of monsters
monsterList = []

#insert monsters
for i in range(level):
    monsterList.append(AMonster())

#track mouse    
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
        if event.type == pygame.KEYDOWN and player.locateCurrentMove()<0:
            #left or right
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                #player.playerMoveX(MoveConstants.LEFT)
                player.leftTrue()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                #player.playerMoveX(MoveConstants.RIGHT)
                player.rightTrue()
            #up or down
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                #player.playerMoveY(MoveConstants.UP)
                player.upTrue()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                #player.playerMoveY(MoveConstants.DOWN)
                player.downTrue()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.leftFalse()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.rightFalse()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.upFalse()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.downFalse()
            #player should stop moving in given direction
            #player.playerStop()  
        #shoot bullet
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shootBullet(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shootBullet(1)
        

    #check collisions, game logic stuff
    #update graphcs to screen

    #make the color of the screen
    #will always be first
    gameDisplay.fill(Color.white)
    
    #update the player
    player.update()
    player.drawUpdate(gameDisplay)
    
    #update monsters
    for aMonster in monsterList:
        aMonster.checkBulletHitList(player.bulletList)
        if aMonster.update():
            aMonster.drawUpdate(gameDisplay)
        else:
            monsterList.remove(aMonster)
            
    #another way to draw rectangle
    #gameDisplay.fill(red, rect=[200,200,50,50])
    
    pygame.display.update()

    #frames per sec, try to avoid changing this in code, keep it as a const
    clock.tick(framesPerSec) 

#unnitializing pygame
pygame.quit()
#leave python
quit()
