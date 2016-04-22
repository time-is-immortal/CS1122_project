

#define colors    
class Color:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    darkred = (128,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    grayish = (192,192,192)
   
#define borders
class Layout:
    screen_width = 800
    screen_height = 600
    borderOffSet = 5
    topOffSet = 25
    healthBarWidth = 500

#define game images
class GameImages:
    playerImage = ["static/playerUp.png","static/playerDown.png","static/playerLeft.png","static/playerRight.png"]
    monsterImage = "static/virus.png"
    healthImage = "static/pickup_Health.png"
    ammoImage = "static/pickup_Ammo.png"

#constants for movements
class MoveConstants():
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    