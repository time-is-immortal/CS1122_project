import pygame
import random
from Design import *
from Monster import AMonster
from Player import User
from Pickups import *
from Bomb import HiddenBomb
import time
import sys
 
#will initialize all modules
#have to have it
pygame.init()

#need to make a canvas
#requires a tuple (aka the size of windows)
gameDisplay = pygame.display.set_mode((Layout.SCREEN_WIDTH,Layout.SCREEN_HEIGHT))
pygame.display.set_caption('BestNameEver!')

gameExit = False
tutorial = True
startText = True

#current level
level = 0

#time for frames per sec
clock = pygame.time.Clock()
framesPerSec = 60

#player
player = User()

#list of monsters
monsterList = []

#list of health packs
healthPackList = []

#list of ammo packs
ammoPackList = []

#list of hidden bombs
hiddenBombList = []
explosionAnimationList = []

#display level
font = pygame.font.Font("static/KOMTITP_.ttf", 16)

#spawn monsters
def spawnMonsters():
    if tutorial == True:
        monsterList.append(AMonster(monsterList,player,1))
    else:
        #insert monsters
        value = level
        for i in reversed(range(len(MonsterConstants.MONSTERLEVEL))):
            for j in range(int(value/MonsterConstants.MONSTERLEVEL[i])):
                monsterList.append(AMonster(monsterList,player,i))
            value %= MonsterConstants.MONSTERLEVEL[i]
        ammoPackList.append(AmmoPickUp(random.randint(PickupConstants.WIDTH/2+Layout.BORDEROFFSET,Layout.SCREEN_WIDTH-Layout.BORDEROFFSET-PickupConstants.WIDTH/2),random.randint(PickupConstants.HEIGHT/2+Layout.TOPOFFSET,Layout.SCREEN_HEIGHT-Layout.BORDEROFFSET-PickupConstants.HEIGHT/2)))

#create hidden bombs
def createHiddenBombs(howmany):
    del hiddenBombList[:]
    for i in range(0, howmany):
        hiddenBombList.append(HiddenBomb(player))

#mouse
mouseX = 0
mouseY = 0

#shoot mode TOGGLE with key R
shoot = True

#hide cursor
pygame.mouse.set_visible(False)

#cursor image
cursorImage = pygame.transform.scale(pygame.image.load(GameImages.CURSORIMAGE).convert_alpha(),(Layout.MOUSEDIMENSIONS,Layout.MOUSEDIMENSIONS))
#background image
backGroundImage = pygame.transform.scale(pygame.image.load(GameImages.BACKGROUNDIMAGE).convert_alpha(),(Layout.SCREEN_WIDTH,Layout.SCREEN_HEIGHT))

def playerRules():
    pygame.draw.rect(gameDisplay, Color.GREY, [80, 80, 410, 180]) 
    gameDisplay.blit(font.render(" Avoid the monsters! ",True, Color.ANTIQUEWHITE,Color.GREY),[100,100,100,Layout.TOPOFFSET]) 
    gameDisplay.blit(font.render(" Use AWSD or ARROW Keys to move ",True, Color.ANTIQUEWHITE,Color.GREY),[100,130,100,Layout.TOPOFFSET]) 
    gameDisplay.blit(font.render(" Shoot via Left Click or SPACE ",True, Color.ANTIQUEWHITE,Color.GREY),[100,160,100,Layout.TOPOFFSET]) 
    gameDisplay.blit(font.render(" Toggle between shooting option via R ",True, Color.ANTIQUEWHITE,Color.GREY),[100,190,100,Layout.TOPOFFSET])
    gameDisplay.blit(font.render(" Press Z to continue ",True, Color.ANTIQUEWHITE,Color.GREY),[100,220,100,Layout.TOPOFFSET])
          
        
while not gameExit:
    
    #make monster(s)
    #no monsters left
    if len(monsterList) == 0:
        if not tutorial:
            level+=1
            if level >= BombConstants.MINLEVEL:
                createHiddenBombs(1) # Just one bomb for now
        spawnMonsters()
        
    #core game logic
    #always need to be checked
    #they take care of event handling
    #i.e. if arrow key is pressed, space bar is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        
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
            #start tutorial
            if event.key == pygame.K_z:
                startText = False
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


    #make the color of the screen
    #will always be first
    gameDisplay.blit(backGroundImage,[0,0,Layout.SCREEN_WIDTH,Layout.SCREEN_HEIGHT])
   
    #trapped in tutorial
    #with non moving monsterList
    #kill monster to play game
    if startText: 
        playerRules()        
    
    else:
        #display current level
        if player.ammo > 0:
           text = font.render(" Level:"+str(level)+" Ammo:"+str(player.ammo)+" ",True,Color.ANTIQUEWHITE,Color.GREY)
        else:   
            text = font.render(" Level:"+str(level)+" No Ammo"+" ",True,Color.RED,Color.GREY)
        gameDisplay.blit(text,[10,0,0,Layout.TOPOFFSET]) 
        
        if tutorial:
            pygame.draw.rect(gameDisplay, Color.GREY, [80, 30, 420, 220]) 
            text = font.render(" Kill monster to start game! ",True,Color.RED,Color.GREY)
            text2 = font.render("Beware of the hidden bombs.", True, Color.RED, Color.GREY)
            text3 = font.render("If you hear a beeping sound,", True, Color.RED, Color.GREY)
            text4 = font.render("go back the other way!", True, Color.RED, Color.GREY)
            text5 = font.render ("Tip: Monsters sometimes drop", True, Color.ANTIQUEWHITE, Color.Grey)
            text6 = font.render("ammo and health packs!", True, Color.ANTIQUEWHITE, Color.Grey)
            gameDisplay.blit(text,[100,50,0,Layout.TOPOFFSET])
            gameDisplay.blit(text2, [100, 80, 0, Layout.TOPOFFSET])
            gameDisplay.blit(text3, [100, 110, 0, Layout.TOPOFFSET])
            gameDisplay.blit(text4, [100, 140, 0, Layout.TOPOFFSET])
            gameDisplay.blit(text5, [100, 170, 0, Layout.TOPOFFSET])
            gameDisplay.blit(text6, [100, 200, 0, Layout.TOPOFFSET])
        #update graphics to screen

        #update monsters
        for aMonster in monsterList:
            aMonster.checkBulletHitList(player.bulletList)
            if aMonster.update(monsterList,player,gameDisplay,healthPackList,ammoPackList,hiddenBombList,explosionAnimationList, tutorial):
                aMonster.drawUpdate(gameDisplay)
            elif tutorial == True:
                tutorial = False
                player.currentHealth = PlayerConstants.MAXHEALTH
                player.ammo = PlayerConstants.AMMOLIMIT
        
        #update heealth packs
        for healthPack in healthPackList:
            healthPack.drawUpdate(gameDisplay)
        
        #update ammo packs
        for ammoPack in ammoPackList:
            ammoPack.drawUpdate(gameDisplay)
        
        #update the player
        player.update(healthPackList,ammoPackList,hiddenBombList,explosionAnimationList)
        if player.drawUpdate(gameDisplay, framesPerSec):
            gameDisplay.blit(font.render(" _________GG WP_________ ",True, Color.ANTIQUEWHITE,Color.GREY),[100,100,100,Layout.TOPOFFSET]) 
            gameDisplay.blit(font.render(" Level: " + str(level),True, Color.ANTIQUEWHITE,Color.GREY),[100,150,100,Layout.TOPOFFSET]) 
            gameDisplay.blit(font.render(" Monsters killed : " + str(player.killCount),True, Color.ANTIQUEWHITE,Color.GREY),[100,200,100,Layout.TOPOFFSET])
            gameDisplay.blit(font.render(" Press SPACE to continue ",True, Color.ANTIQUEWHITE,Color.GREY),[100,250,100,Layout.TOPOFFSET])
            gameDisplay.blit(font.render(" Press ENTER to quit ",True, Color.ANTIQUEWHITE,Color.GREY),[100,300,100,Layout.TOPOFFSET])
            pygame.display.update()  
            while(not tutorial):              
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        tutorial = True
                        startText = True
                        level = 0
                        player = User()
                        del monsterList[:]
                        del healthPackList[:]
                        del ammoPackList[:]
                        del hiddenBombList[:]
                        del explosionAnimationList[:]
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        pygame.quit()
                        sys.exit("Thanks for playing")      
        #play explosion animations
        for anim in explosionAnimationList:
            anim.drawUpdate(gameDisplay, framesPerSec)
        
        
        #Using Mouse to Move
        (mouseX, mouseY) = pygame.mouse.get_pos()
        gameDisplay.blit(cursorImage,[mouseX-Layout.MOUSEDIMENSIONS/2,mouseY-Layout.MOUSEDIMENSIONS/2,Layout.MOUSEDIMENSIONS,Layout.MOUSEDIMENSIONS])
  


    pygame.display.update()

    #frames per sec, try to avoid changing this in code, keep it as a const
    clock.tick(framesPerSec) 

# unnitializing pygame
pygame.quit()
# leave python
quit()
