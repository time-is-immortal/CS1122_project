
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
    GREY = (68,68,68)

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
    PLAYERIMAGE = ["static/player-up.png","static/player-down.png","static/player-left.png","static/player-right.png","static/player-upright.png", "static/player-upleft.png", "static/player-downright.png", "static/player-downleft.png"]
    MONSTERIMAGE = "static/virus.png"
    HEALTHIMAGE = "static/pickup_Health.png"
    AMMOIMAGE = "static/pickup_Ammo.png"
    BACKGROUNDIMAGE = "static/back.png"
    CURSORIMAGE = "static/pointer.png"

class Sounds:
    SHOOTSOUND = "static/shootSound.wav"
    HITSOUND = "static/hitSound.wav"
    PICKUPSOUND = "static/pickupSound.wav"
    EXPLOSIONSOUND = "static/explosion/cydon.wav"

#constants for movements
class MoveConstants:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    UPRIGHT = 4
    UPLEFT = 5
    DOWNRIGHT = 6
    DOWNLEFT = 7

class PlayerConstants:
    AMMOLIMIT = 100
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
    HEALTHRESTORE = 5
    AMMORESTORE = 10

class BombConstants:
    TRIGGERRADIUS = 50 # pixels
    BEEPRADIUS = 500 # pixels
    MINLEVEL = 1 # do not plant bombs below this level
    BEEPHERTZMAX = 2
    BEEPHERTZMIN = 0.5
    BEEP_SOUNDS = [
        "static/explosion/sonar-1.wav",
        "static/explosion/sonar-2.wav",
        "static/explosion/sonar-3.wav",
        "static/explosion/sonar-4.wav",
        "static/explosion/sonar-5.wav"
    ]
    EXPLOSION = [
        "static/explosion/explosion-09.png",
        "static/explosion/explosion-10.png",
        "static/explosion/explosion-11.png",
        "static/explosion/explosion-12.png",
        "static/explosion/explosion-13.png",
        "static/explosion/explosion-14.png",
        "static/explosion/explosion-15.png",
        "static/explosion/explosion-16.png",
        "static/explosion/explosion-17.png",
        "static/explosion/explosion-01.png",
        "static/explosion/explosion-02.png",
        "static/explosion/explosion-03.png",
        "static/explosion/explosion-04.png",
        "static/explosion/explosion-05.png",
        "static/explosion/explosion-06.png",
        "static/explosion/explosion-07.png",
        "static/explosion/explosion-08.png"
    ]
    EXPLOSION_SIZE = (200, 200)
    EXPLOSION_REGISTRATION = (97, 156)
    EXPLOSION_FPS = 10

#collision between two rectangles 
def CHECKRECT(X,Y,Width,Height,otherX,otherY,otherWidth,otherHeight):
    if abs(otherX - X) <= Width/2 + otherWidth/2 and abs(otherY - Y) <= Height/2 + otherHeight/2:
        return True
    return False
