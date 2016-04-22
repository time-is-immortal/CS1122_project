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
   tempMonster = AMonster(monsterList)
   monsterList.append(tempMonster)

mouseX = 0
mouseY = 0

#shoot mode TOGGLE with key R
shoot = False

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
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.leftTrue()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.rightTrue()
            #up or down
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.upTrue()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.downTrue()
            if event.key == pygame.K_r:
                shoot = not shoot
        #shoot bullet via mouse
        if event.type == pygame.MOUSEBUTTONDOWN and shoot == True:
            player.shootBullet(0)
        #shoot bullet via spacebar
        elif event.type == pygame.KEYDOWN and shoot == False:
            if event.key == pygame.K_SPACE:
                player.shootBullet(1)
        if event.type == pygame.KEYUP:
            #player should stop moving
            #in said direction
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.leftFalse()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.rightFalse()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.upFalse()
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.downFalse()

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
