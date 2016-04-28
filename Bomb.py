from Design import BombConstants, Layout
import random
import math
import pygame

class HiddenBomb:
    def __init__(self, player):
        self.detonated = False
        # Generate random coorindates, but do not be near the player.
        def _coords():
            return (
                random.randint(Layout.BORDEROFFSET, Layout.SCREEN_WIDTH - Layout.BORDEROFFSET),
                random.randint(Layout.TOPOFFSET, Layout.SCREEN_HEIGHT - Layout.BORDEROFFSET)
            )
        # Dangnabbit, Guido thinks that do..while loops are confusing, now, doesn't he?
        # Well, how is this for confusing?
        self.x, self.y = _coords()
        while self.distanceToPlayer(player) < BombConstants.TRIGGERRADIUS:
            self.x, self.y = _coords()
        print("Bomb coordinates:", self.x, self.y)
    
    def distanceToPlayer(self, player):
        # Pythagorean Theorem
        return math.sqrt(math.pow(player.playerY - self.y, 2) + math.pow(player.playerX - self.x, 2))
    
    def distanceToMonster(self, monster):
        # Pythagorean Theorem
        return math.sqrt(math.pow(monster.monsterY - self.y, 2) + math.pow(monster.monsterX - self.x, 2))
    
    def detonate(self, explosionAnimationList):
        self.detonated = True
        print("BOOM!") # TODO: Get an actual WAV file
        explosionAnimationList.append(ExplosionAnimation(self.x, self.y, BombConstants.EXPLOSION, BombConstants.EXPLOSION_SIZE, BombConstants.EXPLOSION_REGISTRATION, BombConstants.EXPLOSION_FPS))
          
    def checkCollisionsWithMonster(self, monster, explosionAnimationList):
        if self.detonated:
            return False
        if self.distanceToMonster(monster) < BombConstants.TRIGGERRADIUS:
            self.detonate(explosionAnimationList)
            return True
        return False
    
    def checkCollisionsWithPlayer(self, player, explosionAnimationList):
        if self.detonated:
            return False
        if self.distanceToPlayer(player) < BombConstants.TRIGGERRADIUS:
            self.detonate(explosionAnimationList)
            return True
        return False
        
class ExplosionAnimation:
    def __init__(self, x, y, frames, dimensions, registration, fps):
        self.x = x - registration[0]
        self.y = y - registration[1]
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.frames = frames
        self.fps = fps
        self.globalframe = 0
        self.animframe = 0
        self.image = None
        self.reloadImage(0)
    
    def reloadImage(self, globalFPS):
        if self.globalframe >= globalFPS / self.fps or self.image is None:
            self.globalframe = 0
            self.animframe += 1
            self.image = pygame.transform.scale(pygame.image.load(self.frames[min(self.animframe, len(self.frames) - 1)]).convert_alpha(), (self.width, self.height))
        return self.image
    
    def drawUpdate(self, gameDisplay, globalFPS):
        if self.animframe < len(self.frames):
            gameDisplay.blit(self.reloadImage(globalFPS), [self.x, self.y, self.width, self.height])
            self.globalframe += 1
            return True
        return False