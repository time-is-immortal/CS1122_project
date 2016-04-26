
#define colors    
class Color:
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    DARKRED = (128,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    GRAYISH = (192,192,192)
    ANTIQUEWHITE = (250,235,215)
   
#define borders
class Layout:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BORDEROFFSET = 5
    TOPOFFSET = 25
    HEALTHBARWIDTH = SCREEN_WIDTH/2
    AMMOTEXTPADDING = 10
    MOUSEDIMENSIONS = 30

#define game images
class GameImages:
    PLAYERIMAGE = ["static/player-up.png","static/player-down.png","static/player-left.png","static/player-right.png"]
    MONSTERIMAGE = "static/virus.png"
    HEALTHIMAGE = "static/pickup_Health.png"
    AMMOIMAGE = "static/pickup_Ammo.png"

class Sounds:
    SHOOTSOUNT = "audio/shootSound.wav"

#constants for movements
class MoveConstants:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    
class PlayerConstants:
    AMMOLIMIT = 999
    MAXHEALTH = 20
    PLAYERWIDTH = 50
    PLAYERHEIGHT = 50
    MOVE = 5
    
class MonsterConstants:
    MONSTERLEVEL = [.25,3,5,10,20]
    #health,width,height,delay timer,move rate
    MONSTERSTATS = [(2,50,50,7,4),(4,100,100,7,7),(10,250,250,15,3),(6,25,25,3,2),(10,300,300,50,2)]
    SPAWNDELAY = -30
    
class PickupConstants:
    HEIGHT = 20
    WIDTH = 20
    RATESPAWN = .1
    RATERESTORE = 10
    
#collision between two rectangles 
def CHECKRECT(X,Y,Width,Height,otherX,otherY,otherWidth,otherHeight):
    if abs(otherX - X) <= Width/2 + otherWidth/2 and abs(otherY - Y) <= Height/2 + otherHeight/2:
        return True
    return False
