from Design import BombConstants, Layout
import random
import math

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
    
    def detonate(self):
        self.detonated = True
        print("BOOM!") # TODO: Get an actual WAV file
    
    def checkCollisionsWithMonster(self, monster):
        if self.detonated:
            return False
        if self.distanceToMonster(monster) < BombConstants.TRIGGERRADIUS:
            self.detonate()
            return True
        return False
    
    def checkCollisionsWithPlayer(self, player):
        if self.detonated:
            return False
        if self.distanceToPlayer(player) < BombConstants.TRIGGERRADIUS:
            self.detonate()
            return True
        return False
