
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
    HEALTHBARWIDTH = 700
    AMMOTEXTPADDING = 10

#define game images
class GameImages:
    PLAYERIMAGE = ["static/playerUp.png","static/playerDown.png","static/playerLeft.png","static/playerRight.png"]
    MONSTERIMAGE = "static/virus.png"
    HEALTHIMAGE = "static/pickup_Health.png"
    AMMOIMAGE = "static/pickup_Ammo.png"

#constants for movements
class MoveConstants:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    
class PlayerConstants:
    AMMOLIMIT = 30
    MAXHEALTH = 10
    PLAYERWIDTH = 50
    PLAYERHEIGHT = 50