# Name:          Farris Matar
# Date:          May 29, 2017
# Class:         ICS3U1-03
# Description:   Final summative, making a game.

# -----------------------------------------------------------------------------------------
# Initialization and Variable Definition
# ----------------------------------------------------------------------------------------- 

# Starting up Pygame.
import pygame
import random
pygame.init()

# Setting up some variables for the screen and colours.
SIZE = (800,700)
screen = pygame.display.set_mode(SIZE)
BLACK = (0,0,0)
DARK_GRAY = (50,50,50)
DARKISH_GRAY = (90,90,90)
GRAY = (122,122,122)
STONE_GRAY = (181,181,181)
LIGHT_GRAY = (220,220,220)
YELLOW_GRAY = (191,191,156)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (229,117,48)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (170,0,255)
CYAN = (0,255,255)
BEIGE = (255,230,186)
BROWN = (81,49,8)
SILVER = (199,207,229)
COMPUTER_GRAY = (55,71,54)
LAUNCHER_STEEL = (170,172,175)
DARK_LAUNCHER_STEEL = (100,102,104)
DARK_RED = (170,0,0)
DARK_GREEN = (0,170,0)
DARK_CYAN = (0,170,170)
DARK_BROWN = (96,87,69)
DARK_PURPLE = (42,29,51)
DARKER_GREEN = (0,80,0)
DARKER_PURPLE = (27,19,33)
DARKER_BROWN = (40,24,3)
DARKER_RED = (114,0,0)
LIGHT_RED = (255,100,100)
LIGHT_YELLOW = (255,255,100)
LIGHT_GREEN = (150,255,150)
LIGHT_BLUE = (100,100,255)
LIGHT_PURPLE = (206,109,255)
LIGHT_ORANGE = (255,195,107)
SHIRT_RED = (178,74,74)
SHIRT_WHITE = (224,224,224)
CLOUD_GRAY = (80,80,80)
PANTS_BROWN = (104,91,71)
TITLE_YELLOW = (226,215,0)
BULLET_GOLD = (237,202,47)
scene = 1

# Making variables for the fonts, images and sounds.
# Fonts
titleFont = pygame.font.SysFont("Courier New",90)
gameTitleFont = pygame.font.SysFont("Algerian",75)
instructionsTitleFont = pygame.font.SysFont("Courier New",60)
instructionsSubtitleFont = pygame.font.SysFont("Times New Roman",36)
instructionsFont = pygame.font.SysFont("Times New Roman",18)
gameOverFont = pygame.font.SysFont("Stencil",90)
finalScoreFont = pygame.font.SysFont("Courier New",50)
buttonFont = pygame.font.SysFont("OCR A Extended",45)
backButtonFont = pygame.font.SysFont("OCR A Extended",27)
statusBarFont = pygame.font.SysFont("COLONNA",24)
scoreFont = pygame.font.SysFont("OCR A Extended",60)
scoreTitleFont = pygame.font.SysFont("COLONNA",50)

# Images
crossbow = pygame.image.load("Crossbow.png")
rifle = pygame.image.load("Rifle.png")
rocket = pygame.image.load("Missile.png")

# Sounds
footsteps = pygame.mixer.Sound("New Climbing Sound.wav")
thunderStrike = pygame.mixer.Sound("New Thunder Strike.wav")
crossbowFiring = pygame.mixer.Sound("New Crossbow Firing.wav")
gunshot = pygame.mixer.Sound("New Gunshot.wav")
missileFiring = pygame.mixer.Sound("New Missile Launch.wav")
robotDeath = pygame.mixer.Sound("New Dying Robot.wav")
fallingSound = pygame.mixer.Sound("New Falling Sound.wav")
rumbling = pygame.mixer.Sound("New Earthquake.wav")
boom = pygame.mixer.Sound("New Boom.wav")
powSound = pygame.mixer.Sound("Pow.wav")
gameOverSound = pygame.mixer.Sound("New Game Over.wav")

pygame.mixer.music.load("New Raining Sound.wav")
rainSoundTime = 300
rainPlayCount = 2

# High scores file.
scoreRecord = open("High Scores.txt","r")
scoreUpdate = open("High Scores.txt","a")

# Making a list to hold all the scores.
highScores = []

while True:
    text = scoreRecord.readline()
    if text == "":
        break
    highScores.append(int(text[:-1]))

# Sorting the list from highest to lowest.
highScores.sort(reverse=True)
newHighScore = False
newHighScoreColor = (255,255,255)

# Setting the volume for music and some sounds.
pygame.mixer.music.set_volume(0.4)
missileFiring.set_volume(0.6)
robotDeath.set_volume(0.75)
footsteps.set_volume(0.5)

# Making variables for the buttons to work.
# Play button.
PLAY_BUTTON_X = 200
PLAY_BUTTON_Y = 350
PLAY_BUTTON_WIDTH = 400
PLAY_BUTTON_HEIGHT = 75
playColor = (0,0,0)

# How to play button.
INSTRUCTIONS_BUTTON_X = 200
INSTRUCTIONS_BUTTON_Y = 450
INSTRUCTIONS_BUTTON_WIDTH = 400
INSTRUCTIONS_BUTTON_HEIGHT = 75
instructionsColor = (0,0,0)

# Next page button.
NEXT_BUTTON_X = 710
NEXT_BUTTON_Y = 635
NEXT_BUTTON_WIDTH = 75
NEXT_BUTTON_HEIGHT = 40
nextColor = (0,0,0)

# Previous page button.
PREVIOUS_BUTTON_X = 15
PREVIOUS_BUTTON_Y = 635
PREVIOUS_BUTTON_WIDTH = 75
PREVIOUS_BUTTON_HEIGHT = 40
previousColor = (0,0,0)

# Quit button.
# Main menu.
QUIT_BUTTON_X = 200
QUIT_BUTTON_Y = 550
QUIT_BUTTON_WIDTH = 400
QUIT_BUTTON_HEIGHT = 75
quitColor = (0,0,0)
# Game over screen.
QUIT_BUTTON2_X = 500
QUIT_BUTTON2_Y = 600
QUIT_BUTTON2_WIDTH = 200
QUIT_BUTTON2_HEIGHT = 75
quitColor2 = (0,0,0)

# Back button.
BACK_BUTTON_X = 15
BACK_BUTTON_Y = 15
BACK_BUTTON_WIDTH = 75
BACK_BUTTON_HEIGHT = 40
backColor = (0,0,0)

# Resume button.
RESUME_BUTTON_X = 200
RESUME_BUTTON_Y = 300
RESUME_BUTTON_WIDTH = 400
RESUME_BUTTON_HEIGHT = 75
resumeColor = (0,0,0)

# Return-to-menu button.
# Pause menu.
RETURN_BUTTON_X = 200
RETURN_BUTTON_Y = 425
RETURN_BUTTON_WIDTH = 400
RETURN_BUTTON_HEIGHT = 75
returnColor = (0,0,0)
# Game over screen.
RETURN_BUTTON2_X = 100
RETURN_BUTTON2_Y = 600
RETURN_BUTTON2_WIDTH = 200
RETURN_BUTTON2_HEIGHT = 75
returnColor2 = (0,0,0)

# Drawing rectangles for indicating the collisions.
playIndicator = pygame.Rect(PLAY_BUTTON_X, PLAY_BUTTON_Y, PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT)
instructionsIndicator = pygame.Rect(INSTRUCTIONS_BUTTON_X, INSTRUCTIONS_BUTTON_Y, INSTRUCTIONS_BUTTON_WIDTH, INSTRUCTIONS_BUTTON_HEIGHT)
nextIndicator = pygame.Rect(NEXT_BUTTON_X, NEXT_BUTTON_Y, NEXT_BUTTON_WIDTH, NEXT_BUTTON_HEIGHT)
previousIndicator = pygame.Rect(PREVIOUS_BUTTON_X, PREVIOUS_BUTTON_Y, PREVIOUS_BUTTON_WIDTH, PREVIOUS_BUTTON_HEIGHT)
quitIndicator = pygame.Rect(QUIT_BUTTON_X, QUIT_BUTTON_Y, QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGHT)
backIndicator = pygame.Rect(BACK_BUTTON_X, BACK_BUTTON_Y, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)
resumeIndicator = pygame.Rect(RESUME_BUTTON_X, RESUME_BUTTON_Y, RESUME_BUTTON_WIDTH, RESUME_BUTTON_HEIGHT)
returnIndicator = pygame.Rect(RETURN_BUTTON_X, RETURN_BUTTON_Y, RETURN_BUTTON_WIDTH, RETURN_BUTTON_HEIGHT)
return2Indicator = pygame.Rect(RETURN_BUTTON2_X, RETURN_BUTTON2_Y, RETURN_BUTTON2_WIDTH, RETURN_BUTTON2_HEIGHT)
quit2Indicator = pygame.Rect(QUIT_BUTTON2_X, QUIT_BUTTON2_Y, QUIT_BUTTON2_WIDTH, QUIT_BUTTON2_HEIGHT)

# Making variables for the position of the character.
playerX = 85
playerY = 300
playerState = 1
circleRadius = 25
recoil = False

# Making variables for the position of the castle.
castleX = 40
castleY = 242
CASTLE_WIDTH = 100
CASTLE_HEIGHT = 450

# Making variables for the enemies.
enemyStandby = []
enemySpawned = []
targetHealth = []
targetWidth = 80
targetHeight = 80
targetMove = -2

# Making variables for various aspects of the status bar.
# Power bar
POWER_X = 25
POWER_Y = 25
powerWidth = 0
powerRate = 1

# Health bar
HEALTH_X = 25
HEALTH_Y = 75
health = 100
healthColor = (0,255,0)

# Weapons
weapon = 1
weaponFired = 0

CROSSBOW_X = 275
CROSSBOW_Y = 35
crossbowReload = 0
arrowX = playerX
arrowY = playerY
arrowTimer = 0
arrowFired = False

RIFLE_X = 350
RIFLE_Y = 35
rifleReload = 0
bulletX = playerX+65
bulletY = playerY
bulletTimer = 0
bulletFired = False

ROCKET_X = 425
ROCKET_Y = 35
rocketReload = 0
rocketX = playerX+65
rocketY = playerY
rocketTimer = 0
rocketFired = False
explosionRadius = 15
explosion = False

# Score
score = 0
scoreCheck = 0
scoreDifficulty = 0
SCORE_X = 525
SCORE_Y = 1

# Making some variables for the explosions animation.
explosionAnimation = False
explosionAnimationX = 120
explosionAnimationY = 300
explosionSize = 1
explosionAnimationX2 = 60
explosionAnimationY2 = 600
explosionSize2 = -24
boomPlayed = False

# Making variables for the lightning animation.
lightningAnimation = False
lightningSize = 1

# Making a list to hold the coordinates of the raindrops.
raindrops = []
# Using a nested loop to add all the coordinates of the raindrops.
for count in range(20):
    for count2 in range(17):
        raindrops.append([(count+1)*40-20,(count2+1)*40+120])

# Playing an initial lightning crash.
thunderStrike.play()

# -----------------------------------------------------------------------------------------
# Character Sprites and Weapon Designs
# ----------------------------------------------------------------------------------------- 

# Making functions to draw the weapons.
# Crossbow
def drawCrossbow(playerX,playerY,sizeFactor):
    # Stock
    pygame.draw.rect(screen,BROWN,pygame.Rect(playerX-25*sizeFactor,playerY,70*sizeFactor,5*sizeFactor))
    pygame.draw.polygon(screen,DARKER_BROWN,[[playerX,playerY+5*sizeFactor],[playerX-25*sizeFactor,playerY+5*sizeFactor],[playerX-25*sizeFactor,playerY+15*sizeFactor]])
    pygame.draw.rect(screen,DARKER_BROWN,pygame.Rect(playerX+5*sizeFactor,playerY+5*sizeFactor,20*sizeFactor,5*sizeFactor))
    
    # Sights
    pygame.draw.rect(screen,SILVER,pygame.Rect(playerX+26*sizeFactor,playerY+1*sizeFactor,27*sizeFactor,2*sizeFactor))
    
    # Bow
    pygame.draw.arc(screen,SILVER,[playerX-5*sizeFactor,playerY-4*sizeFactor,60*sizeFactor,12*sizeFactor],4.5,7.9,1*sizeFactor)
    pygame.draw.arc(screen,SILVER,[playerX-5*sizeFactor,playerY-5*sizeFactor,60*sizeFactor,12*sizeFactor],4.5,7.9,1*sizeFactor)
    pygame.draw.arc(screen,SILVER,[playerX-5*sizeFactor,playerY-3*sizeFactor,60*sizeFactor,12*sizeFactor],4.5,7.9,1*sizeFactor)

# Rifle
def drawRifle(playerX,playerY,sizeFactor):
    # Stock
    pygame.draw.rect(screen,DARKER_BROWN,pygame.Rect(playerX-50*sizeFactor,playerY,115*sizeFactor,5*sizeFactor))
    pygame.draw.polygon(screen,DARKER_BROWN,[[playerX-15*sizeFactor,playerY+5*sizeFactor],[playerX-50*sizeFactor,playerY+5*sizeFactor],[playerX-50*sizeFactor,playerY+15*sizeFactor]])
    
    # Scope
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+10*sizeFactor,playerY-3*sizeFactor,25*sizeFactor,3*sizeFactor))
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+17.5*sizeFactor,playerY-7*sizeFactor,10*sizeFactor,4*sizeFactor))
    
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+10*sizeFactor,playerY-12*sizeFactor,3*sizeFactor,7*sizeFactor))
    pygame.draw.polygon(screen,BLACK,[[playerX+13*sizeFactor,playerY-12*sizeFactor],[playerX+13*sizeFactor,playerY-6*sizeFactor],[playerX+20*sizeFactor,playerY-8*sizeFactor],[playerX+20*sizeFactor,playerY-10*sizeFactor]])
    pygame.draw.polygon(screen,BLACK,[[playerX+20*sizeFactor,playerY-10*sizeFactor],[playerX+20*sizeFactor,playerY-8*sizeFactor],[playerX+25*sizeFactor,playerY-8*sizeFactor],[playerX+25*sizeFactor,playerY-10*sizeFactor]])
    pygame.draw.polygon(screen,BLACK,[[playerX+25*sizeFactor,playerY-10*sizeFactor],[playerX+25*sizeFactor,playerY-8*sizeFactor],[playerX+32*sizeFactor,playerY-6*sizeFactor],[playerX+32*sizeFactor,playerY-12*sizeFactor]])
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+32*sizeFactor,playerY-12*sizeFactor,3*sizeFactor,7*sizeFactor))
    
    # Muzzle
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+60*sizeFactor,playerY,5*sizeFactor,5*sizeFactor))
    
    # Trigger
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+8*sizeFactor,playerY+5*sizeFactor,3*sizeFactor,6*sizeFactor))
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+14*sizeFactor,playerY+5*sizeFactor,3*sizeFactor,3*sizeFactor))
    pygame.draw.arc(screen,BLACK,[playerX+3*sizeFactor,playerY-1*sizeFactor,18*sizeFactor,12*sizeFactor],4.3,6.5,2*sizeFactor)

# Missile launcher
def drawMissileLauncher(playerX,playerY,sizeFactor):
    # Body
    pygame.draw.rect(screen,DARKER_RED,pygame.Rect(playerX-47*sizeFactor,playerY-12*sizeFactor,119*sizeFactor,14*sizeFactor))
    pygame.draw.rect(screen,LAUNCHER_STEEL,pygame.Rect(playerX-45*sizeFactor,playerY-10*sizeFactor,115*sizeFactor,10*sizeFactor))
    
    pygame.draw.rect(screen,DARKER_RED,pygame.Rect(playerX-52*sizeFactor,playerY-17*sizeFactor,12*sizeFactor,24*sizeFactor))
    pygame.draw.rect(screen,LAUNCHER_STEEL,pygame.Rect(playerX-50*sizeFactor,playerY-15*sizeFactor,10*sizeFactor,20*sizeFactor))
    
    # Handles
    pygame.draw.rect(screen,DARKER_RED,pygame.Rect(playerX+1*sizeFactor,playerY,9*sizeFactor,17*sizeFactor))
    pygame.draw.rect(screen,LAUNCHER_STEEL,pygame.Rect(playerX+3*sizeFactor,playerY,5*sizeFactor,15*sizeFactor))
    
    pygame.draw.rect(screen,DARKER_RED,pygame.Rect(playerX+35*sizeFactor,playerY,9*sizeFactor,17*sizeFactor))
    pygame.draw.rect(screen,LAUNCHER_STEEL,pygame.Rect(playerX+37*sizeFactor,playerY,5*sizeFactor,15*sizeFactor))
    
    # Screws
    pygame.draw.circle(screen,DARK_LAUNCHER_STEEL,(int(playerX-45*sizeFactor),int(playerY-10*sizeFactor)),int(2*sizeFactor))
    pygame.draw.circle(screen,DARK_LAUNCHER_STEEL,(int(playerX-45*sizeFactor),playerY),int(2*sizeFactor))
    
    # Details
    pygame.draw.rect(screen,DARK_LAUNCHER_STEEL,pygame.Rect(playerX-22*sizeFactor,playerY-10*sizeFactor,1*sizeFactor,10*sizeFactor))
    pygame.draw.rect(screen,DARK_LAUNCHER_STEEL,pygame.Rect(playerX-40*sizeFactor,playerY-10*sizeFactor,3*sizeFactor,10*sizeFactor))
    pygame.draw.rect(screen,DARK_LAUNCHER_STEEL,pygame.Rect(playerX-4*sizeFactor,playerY-10*sizeFactor,1*sizeFactor,10*sizeFactor))
    pygame.draw.rect(screen,DARK_LAUNCHER_STEEL,pygame.Rect(playerX+25*sizeFactor,playerY-10*sizeFactor,1*sizeFactor,10*sizeFactor))
    pygame.draw.rect(screen,DARK_LAUNCHER_STEEL,pygame.Rect(playerX+33*sizeFactor,playerY-10*sizeFactor,1*sizeFactor,10*sizeFactor))
    pygame.draw.rect(screen,DARK_LAUNCHER_STEEL,pygame.Rect(playerX+60*sizeFactor,playerY-10*sizeFactor,1*sizeFactor,10*sizeFactor))

# Making a function to draw an arrow projectile.
def drawArrow(arrowX,arrowY):
    # Shaft
    pygame.draw.rect(screen,DARKER_BROWN,pygame.Rect(arrowX-15,arrowY-2,30,4))
    
    # Arrowhead
    pygame.draw.polygon(screen,WHITE,[[arrowX+15,arrowY-5],[arrowX+15,arrowY+5],[arrowX+20,arrowY]])
    
    # Fletching
    pygame.draw.polygon(screen,WHITE,[[arrowX-15,arrowY-2],[arrowX-12,arrowY-2],[arrowX-16,arrowY-7],[arrowX-19,arrowY-7]])
    pygame.draw.polygon(screen,WHITE,[[arrowX-16,arrowY-7],[arrowX-19,arrowY-7],[arrowX-23,arrowY-8],[arrowX-20,arrowY-4]])
    pygame.draw.polygon(screen,WHITE,[[arrowX-15,arrowY+2],[arrowX-12,arrowY+2],[arrowX-16,arrowY+7],[arrowX-19,arrowY+7]])
    pygame.draw.polygon(screen,WHITE,[[arrowX-16,arrowY+7],[arrowX-19,arrowY+7],[arrowX-23,arrowY+8],[arrowX-20,arrowY+4]])
    pygame.draw.rect(screen,WHITE,pygame.Rect(arrowX-20,arrowY-1,10,3))

# Making a function to draw a rocket projectile.
def drawRocket(rocketX,rocketY):
    # Body
    pygame.draw.ellipse(screen,RED,pygame.Rect(rocketX,rocketY-8,20,16))
    pygame.draw.rect(screen,SILVER,pygame.Rect(rocketX-10,rocketY-8,20,16))
    
    # Fins
    pygame.draw.polygon(screen,DARK_RED,[[rocketX-10,rocketY-8],[rocketX,rocketY-8],[rocketX-10,rocketY-16],[rocketX-20,rocketY-16]])
    pygame.draw.polygon(screen,DARK_RED,[[rocketX-10,rocketY+8],[rocketX,rocketY+8],[rocketX-10,rocketY+16],[rocketX-20,rocketY+16]])
    
    # Fire
    pygame.draw.rect(screen,RED,pygame.Rect(rocketX-15,rocketY-8,5,16))
    pygame.draw.polygon(screen,RED,[[rocketX-15,rocketY-8],[rocketX-15,rocketY+6],[rocketX-30,rocketY]])
    pygame.draw.rect(screen,ORANGE,pygame.Rect(rocketX-14,rocketY-6,3,12))
    pygame.draw.polygon(screen,ORANGE,[[rocketX-14,rocketY-5],[rocketX-14,rocketY+4],[rocketX-26,rocketY]])

# Making a function to draw the player.
def drawPlayer(playerX,playerY,sizeFactor):
    # Drawing the player's head.
    pygame.draw.rect(screen,BEIGE,pygame.Rect(playerX-25*sizeFactor,playerY-60*sizeFactor,50*sizeFactor,50*sizeFactor))
    # Eyes
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX-10*sizeFactor,playerY-45*sizeFactor,10*sizeFactor,15*sizeFactor))
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX+8*sizeFactor,playerY-45*sizeFactor,10*sizeFactor,15*sizeFactor))
    # Hair
    pygame.draw.rect(screen,DARK_BROWN,pygame.Rect(playerX-25*sizeFactor,playerY-60*sizeFactor,50*sizeFactor,10*sizeFactor))
    # Mouth
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX-8*sizeFactor,playerY-20*sizeFactor,25*sizeFactor,3*sizeFactor))
    
    # Drawing the player's body.
    # Left Arm
    pygame.draw.polygon(screen,BLACK,[[playerX+25*sizeFactor,playerY-10*sizeFactor],[playerX+22*sizeFactor,playerY-5*sizeFactor],[playerX+29*sizeFactor,playerY+10*sizeFactor],[playerX+32*sizeFactor,playerY+5*sizeFactor]])
    pygame.draw.polygon(screen,BLACK,[[playerX+29*sizeFactor,playerY+10*sizeFactor],[playerX+32*sizeFactor,playerY+5*sizeFactor],[playerX+37*sizeFactor,playerY+5*sizeFactor],[playerX+34*sizeFactor,playerY+10*sizeFactor]])
    
    # Shirt
    pygame.draw.rect(screen,SHIRT_WHITE,pygame.Rect(playerX-25*sizeFactor,playerY-10*sizeFactor,50*sizeFactor,40*sizeFactor))
    pygame.draw.rect(screen,SHIRT_RED,pygame.Rect(playerX-25*sizeFactor,playerY-10*sizeFactor,20*sizeFactor,30*sizeFactor))
    pygame.draw.rect(screen,SHIRT_RED,pygame.Rect(playerX+15*sizeFactor,playerY-10*sizeFactor,10*sizeFactor,30*sizeFactor))
    
    # Pants
    pygame.draw.rect(screen,PANTS_BROWN,pygame.Rect(playerX-25*sizeFactor,playerY+30*sizeFactor,12*sizeFactor,25*sizeFactor))
    pygame.draw.rect(screen,PANTS_BROWN,pygame.Rect(playerX+13*sizeFactor,playerY+30*sizeFactor,12*sizeFactor,25*sizeFactor))
    
    # Right Arm
    pygame.draw.polygon(screen,BLACK,[[playerX-25*sizeFactor,playerY],[playerX-28*sizeFactor,playerY-5*sizeFactor],[playerX-21*sizeFactor,playerY+10*sizeFactor],[playerX-18*sizeFactor,playerY+5*sizeFactor]])
    pygame.draw.polygon(screen,BLACK,[[playerX-21*sizeFactor,playerY+10*sizeFactor],[playerX-18*sizeFactor,playerY+5*sizeFactor],[playerX+5*sizeFactor,playerY+5*sizeFactor],[playerX+5*sizeFactor,playerY+10*sizeFactor]])

    # Drawing the player's weapon over their body.
    if weapon == 1:
        drawCrossbow(playerX,playerY,sizeFactor)
    if weapon == 2:
        drawRifle(playerX,playerY,sizeFactor)
    if weapon == 3:
        drawMissileLauncher(playerX,playerY,sizeFactor)

# Making a function to draw the player while they are experiencing recoil.
def drawRecoilingPlayer(playerX,playerY):
    # Drawing the player's head.
    pygame.draw.rect(screen,BEIGE,pygame.Rect(playerX-25,playerY-60,50,50))
    # Eyes
    pygame.draw.line(screen,BLACK,(playerX-12,playerY-45),(playerX-2,playerY-40),2)
    pygame.draw.line(screen,BLACK,(playerX-12,playerY-40),(playerX-2,playerY-40),2)
    pygame.draw.line(screen,BLACK,(playerX-12,playerY-35),(playerX-2,playerY-40),2)
    
    pygame.draw.line(screen,BLACK,(playerX+15,playerY-45),(playerX+5,playerY-40),2)
    pygame.draw.line(screen,BLACK,(playerX+15,playerY-40),(playerX+5,playerY-40),2)
    pygame.draw.line(screen,BLACK,(playerX+15,playerY-35),(playerX+5,playerY-40),2)
    # Hair
    pygame.draw.rect(screen,DARK_BROWN,pygame.Rect(playerX-25,playerY-60,50,10))
    # Mouth
    pygame.draw.rect(screen,BLACK,pygame.Rect(playerX-9,playerY-25,25,8))
    pygame.draw.ellipse(screen,RED,pygame.Rect(playerX-4,playerY-22,15,8))
    pygame.draw.rect(screen,BEIGE,pygame.Rect(playerX-9,playerY-17,25,7))
    
    # Drawing the player's body.
    # Left Arm
    pygame.draw.polygon(screen,BLACK,[[playerX+25,playerY-10],[playerX+22,playerY-5],[playerX+29,playerY+10],[playerX+32,playerY+5]])
    pygame.draw.polygon(screen,BLACK,[[playerX+29,playerY+10],[playerX+32,playerY+5],[playerX+37,playerY+5],[playerX+34,playerY+10]])
        
    # Shirt
    pygame.draw.rect(screen,SHIRT_WHITE,pygame.Rect(playerX-25,playerY-10,50,40))
    pygame.draw.rect(screen,SHIRT_RED,pygame.Rect(playerX-25,playerY-10,20,30))
    pygame.draw.rect(screen,SHIRT_RED,pygame.Rect(playerX+15,playerY-10,10,30))
    
    # Pants
    pygame.draw.polygon(screen,PANTS_BROWN,[[playerX+13,playerY+30],[playerX+25,playerY+30],[playerX+40,playerY+55],[playerX+28,playerY+55]])
    pygame.draw.polygon(screen,PANTS_BROWN,[[playerX-25,playerY+30],[playerX-13,playerY+30],[playerX+2,playerY+55],[playerX-10,playerY+55]])
    
    # Right Arm
    pygame.draw.polygon(screen,BLACK,[[playerX-25,playerY],[playerX-28,playerY-5],[playerX-21,playerY+10],[playerX-18,playerY+5]])
    pygame.draw.polygon(screen,BLACK,[[playerX-21,playerY+10],[playerX-18,playerY+5],[playerX+5,playerY+5],[playerX+5,playerY+10]])
    
    # Drawing the player's weapon over their body.
    if weapon == 1:
        drawCrossbow(playerX,playerY,1)
    if weapon == 2:
        drawRifle(playerX,playerY,1)
    if weapon == 3:
        drawMissileLauncher(playerX,playerY,1)

# Making two functions to switch between drawing them to make the player look like they are climbing.
# Right image
def drawClimbingPlayerRight(playerX,playerY):
    # Drawing the player's head.
    pygame.draw.rect(screen,BEIGE,pygame.Rect(playerX-25,playerY-60,50,50))
    # Hair
    pygame.draw.rect(screen,DARK_BROWN,pygame.Rect(playerX-25,playerY-60,50,10))

    # Drawing the player's body.
    # Right Arm
    pygame.draw.polygon(screen,BLACK,[[playerX+25,playerY-10],[playerX+25,playerY+2],[playerX+42,playerY-60],[playerX+36,playerY-60]])
        
    # Shirt
    pygame.draw.rect(screen,SHIRT_RED,pygame.Rect(playerX-25,playerY-10,50,30))
    pygame.draw.rect(screen,WHITE,pygame.Rect(playerX-25,playerY+20,50,10))
    
    # Pants
    pygame.draw.rect(screen,PANTS_BROWN,pygame.Rect(playerX-25,playerY+30,12,25))
    pygame.draw.rect(screen,PANTS_BROWN,pygame.Rect(playerX+13,playerY+30,12,15))
    
    # Left Arm
    pygame.draw.polygon(screen,BLACK,[[playerX-25,playerY],[playerX-25,playerY+10],[playerX-40,playerY-30],[playerX-35,playerY-30]])

# Left image
def drawClimbingPlayerLeft(playerX,playerY):
    # Drawing the player's head.
    pygame.draw.rect(screen,BEIGE,pygame.Rect(playerX-25,playerY-60,50,50))
    # Hair
    pygame.draw.rect(screen,DARK_BROWN,pygame.Rect(playerX-25,playerY-60,50,10))

    # Drawing the player's body.
    # Right Arm
    pygame.draw.polygon(screen,BLACK,[[playerX+25,playerY-2],[playerX+25,playerY+8],[playerX+39,playerY-30],[playerX+35,playerY-30]])
        
    # Shirt
    pygame.draw.rect(screen,SHIRT_RED,pygame.Rect(playerX-25,playerY-10,50,30))
    pygame.draw.rect(screen,WHITE,pygame.Rect(playerX-25,playerY+20,50,10))
    
    # Pants
    pygame.draw.rect(screen,PANTS_BROWN,pygame.Rect(playerX-25,playerY+30,12,15))
    pygame.draw.rect(screen,PANTS_BROWN,pygame.Rect(playerX+13,playerY+30,12,25))
    
    # Left Arm
    pygame.draw.polygon(screen,BLACK,[[playerX-25,playerY-8],[playerX-25,playerY+2],[playerX-41,playerY-60],[playerX-35,playerY-60]])

# Making a function to draw an enemy.
def drawEnemy(enemyX,enemyY,sizeFactor):
    # Antenna
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(enemyX-2*sizeFactor,enemyY-40*sizeFactor,4*sizeFactor,20*sizeFactor))
    pygame.draw.circle(screen,DARK_RED,(enemyX,int(enemyY-41*sizeFactor)),int(5*sizeFactor))
    
    # Body
    pygame.draw.rect(screen,COMPUTER_GRAY,pygame.Rect(enemyX-12*sizeFactor,enemyY-20*sizeFactor,24*sizeFactor,40*sizeFactor))
    
    # Jet
    pygame.draw.polygon(screen,DARK_GRAY,[[enemyX+12*sizeFactor,enemyY+20*sizeFactor],[enemyX-12*sizeFactor,enemyY+20*sizeFactor],[enemyX-12*sizeFactor,enemyY+30*sizeFactor],[enemyX+12*sizeFactor,enemyY+25*sizeFactor]])
    
    pygame.draw.polygon(screen,RED,[[enemyX+12*sizeFactor,enemyY+25*sizeFactor],[enemyX-12*sizeFactor,enemyY+30*sizeFactor],[enemyX-6*sizeFactor,enemyY+37*sizeFactor],[enemyX+18*sizeFactor,enemyY+32*sizeFactor]])
    pygame.draw.polygon(screen,RED,[[enemyX+18*sizeFactor,enemyY+32*sizeFactor],[enemyX-6*sizeFactor,enemyY+37*sizeFactor],[enemyX+15*sizeFactor,enemyY+45*sizeFactor]])
    pygame.draw.polygon(screen,ORANGE,[[enemyX+6*sizeFactor,enemyY+25*sizeFactor],[enemyX-6*sizeFactor,enemyY+30*sizeFactor],[enemyX-2*sizeFactor,enemyY+35*sizeFactor],[enemyX+12*sizeFactor,enemyY+32*sizeFactor]])
    pygame.draw.polygon(screen,ORANGE,[[enemyX-5*sizeFactor,enemyY+35*sizeFactor],[enemyX+12*sizeFactor,enemyY+32*sizeFactor],[enemyX+13*sizeFactor,enemyY+40*sizeFactor]])
    
    # Eye
    pygame.draw.ellipse(screen,GRAY,pygame.Rect(enemyX-10*sizeFactor,enemyY-15*sizeFactor,16*sizeFactor,26*sizeFactor))
    pygame.draw.ellipse(screen,GREEN,pygame.Rect(enemyX-7*sizeFactor,enemyY-12*sizeFactor,10*sizeFactor,20*sizeFactor))
    
    # Right arm
    pygame.draw.arc(screen,DARK_GRAY,[enemyX-1*sizeFactor,enemyY,40*sizeFactor,25*sizeFactor],0.1,2,int(5*sizeFactor))
    pygame.draw.arc(screen,DARK_GRAY,[enemyX-2*sizeFactor,enemyY,40*sizeFactor,25*sizeFactor],0.1,2,int(5*sizeFactor))
    pygame.draw.arc(screen,DARK_GRAY,[enemyX-3*sizeFactor,enemyY,40*sizeFactor,25*sizeFactor],0.1,2,int(5*sizeFactor))
    pygame.draw.circle(screen,COMPUTER_GRAY,(int(enemyX+40*sizeFactor),int(enemyY+13*sizeFactor)),int(8*sizeFactor))
    
    pygame.draw.line(screen,DARK_GRAY,(enemyX+37*sizeFactor,enemyY+13*sizeFactor),(enemyX+30*sizeFactor,enemyY+20*sizeFactor),int(4*sizeFactor))
    pygame.draw.line(screen,DARK_GRAY,(enemyX+40*sizeFactor,enemyY+15*sizeFactor),(enemyX+40*sizeFactor,enemyY+25*sizeFactor),int(4*sizeFactor))
    pygame.draw.line(screen,DARK_GRAY,(enemyX+43*sizeFactor,enemyY+13*sizeFactor),(enemyX+50*sizeFactor,enemyY+20*sizeFactor),int(4*sizeFactor))
    
    # Left arm
    pygame.draw.arc(screen,DARK_GRAY,[enemyX-36*sizeFactor,enemyY,40*sizeFactor,25*sizeFactor],1.3,3.4,int(5*sizeFactor))
    pygame.draw.arc(screen,DARK_GRAY,[enemyX-37*sizeFactor,enemyY,40*sizeFactor,25*sizeFactor],1.3,3.4,int(5*sizeFactor))
    pygame.draw.arc(screen,DARK_GRAY,[enemyX-38*sizeFactor,enemyY,40*sizeFactor,25*sizeFactor],1.3,3.4,int(5*sizeFactor))
    pygame.draw.circle(screen,COMPUTER_GRAY,(int(enemyX-33*sizeFactor),int(enemyY+20*sizeFactor)),int(8*sizeFactor))
    
    pygame.draw.line(screen,DARK_GRAY,(enemyX-30*sizeFactor,enemyY+20*sizeFactor),(enemyX-23*sizeFactor,enemyY+27*sizeFactor),int(4*sizeFactor))
    pygame.draw.line(screen,DARK_GRAY,(enemyX-33*sizeFactor,enemyY+22*sizeFactor),(enemyX-33*sizeFactor,enemyY+32*sizeFactor),int(4*sizeFactor))
    pygame.draw.line(screen,DARK_GRAY,(enemyX-36*sizeFactor,enemyY+20*sizeFactor),(enemyX-43*sizeFactor,enemyY+27*sizeFactor),int(4*sizeFactor)) 

# -----------------------------------------------------------------------------------------
# Background elements.
# ----------------------------------------------------------------------------------------- 

# Making a function to draw the cloud.
def drawCloud(cloudX,cloudY,sizeFactor):
    pygame.draw.rect(screen,CLOUD_GRAY,pygame.Rect(cloudX,cloudY,150*sizeFactor,30*sizeFactor))
    pygame.draw.ellipse(screen,CLOUD_GRAY,pygame.Rect(cloudX-30*sizeFactor,cloudY-30*sizeFactor,60*sizeFactor,60*sizeFactor))
    pygame.draw.ellipse(screen,CLOUD_GRAY,pygame.Rect(cloudX+20*sizeFactor,cloudY-60*sizeFactor,80*sizeFactor,80*sizeFactor))
    pygame.draw.ellipse(screen,CLOUD_GRAY,pygame.Rect(cloudX+95*sizeFactor,cloudY-30*sizeFactor,60*sizeFactor,60*sizeFactor))
    pygame.draw.ellipse(screen,CLOUD_GRAY,pygame.Rect(cloudX-25*sizeFactor,cloudY,185*sizeFactor,45*sizeFactor))
    
# Making a function to draw a lightning bolt.
def drawLightning(lightningX,lightningY,sizeFactor):
    pygame.draw.polygon(screen,YELLOW,[[lightningX,lightningY],[lightningX-3*sizeFactor,lightningY+3*sizeFactor],[lightningX-1*sizeFactor,lightningY+3*sizeFactor]])
    pygame.draw.polygon(screen,YELLOW,[[lightningX-3*sizeFactor,lightningY+3*sizeFactor],[lightningX-1*sizeFactor,lightningY+3*sizeFactor],[int(lightningX+0.5*sizeFactor),lightningY+4*sizeFactor],[int(lightningX-1.5*sizeFactor),lightningY+4*sizeFactor]])
    pygame.draw.polygon(screen,YELLOW,[[int(lightningX+0.5*sizeFactor),lightningY+4*sizeFactor],[int(lightningX-1.5*sizeFactor),lightningY+4*sizeFactor],[lightningX-3*sizeFactor,lightningY+7*sizeFactor]])

# Making a function to draw a tree.
def drawTree(treeX,treeY,sizeFactor):
    # Trunk
    pygame.draw.polygon(screen,BLACK,[[treeX-27*sizeFactor,treeY-77*sizeFactor],[treeX+37*sizeFactor,treeY-77*sizeFactor],[treeX+37*sizeFactor,treeY+2*sizeFactor],[treeX-27*sizeFactor,treeY+2*sizeFactor]])
    pygame.draw.polygon(screen,BROWN,[[treeX-25*sizeFactor,treeY-75*sizeFactor],[treeX+35*sizeFactor,treeY-75*sizeFactor],[treeX+35*sizeFactor,treeY],[treeX-25*sizeFactor,treeY]])
    
    # Leaves base 1
    pygame.draw.polygon(screen,BLACK,[[treeX-124*sizeFactor,treeY-73*sizeFactor],[treeX+124*sizeFactor,treeY-73*sizeFactor],[treeX,treeY-177*sizeFactor]])
    pygame.draw.polygon(screen,DARKER_GREEN,[[treeX-120*sizeFactor,treeY-75*sizeFactor],[treeX+120*sizeFactor,treeY-75*sizeFactor],[treeX,treeY-175*sizeFactor]])
    
    # Leaves base 2
    pygame.draw.polygon(screen,BLACK,[[treeX-84*sizeFactor,treeY-148*sizeFactor],[treeX+84*sizeFactor,treeY-148*sizeFactor],[treeX,treeY-227*sizeFactor]])
    pygame.draw.polygon(screen,DARKER_GREEN,[[treeX-80*sizeFactor,treeY-150*sizeFactor],[treeX+80*sizeFactor,treeY-150*sizeFactor],[treeX,treeY-225*sizeFactor]])
    
    # Leaves base 3
    pygame.draw.polygon(screen,BLACK,[[treeX-64*sizeFactor,treeY-198*sizeFactor],[treeX+64*sizeFactor,treeY-198*sizeFactor],[treeX,treeY-277*sizeFactor]])
    pygame.draw.polygon(screen,DARKER_GREEN,[[treeX-60*sizeFactor,treeY-200*sizeFactor],[treeX+60*sizeFactor,treeY-200*sizeFactor],[treeX,treeY-275*sizeFactor]])

# Making a function to draw the castle.
def drawCastle(castleX,castleY):
    # Basic body.
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX-4,castleY-4,CASTLE_WIDTH+8,CASTLE_HEIGHT+8))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX-34,castleY-14,CASTLE_WIDTH+68,48))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX-34,castleY-64,38,58))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX+31,castleY-64,38,58))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX+96,castleY-64,38,58))
    
    pygame.draw.rect(screen,GRAY,pygame.Rect(castleX,castleY,CASTLE_WIDTH,CASTLE_HEIGHT))
    pygame.draw.rect(screen,GRAY,pygame.Rect(castleX-30,castleY-10,CASTLE_WIDTH+60,40))
    pygame.draw.rect(screen,GRAY,pygame.Rect(castleX-30,castleY-60,30,50))
    pygame.draw.rect(screen,GRAY,pygame.Rect(castleX+35,castleY-60,30,50))
    pygame.draw.rect(screen,GRAY,pygame.Rect(castleX+100,castleY-60,30,50))
    
    # Bricks.
    for count in range(4):
        pygame.draw.line(screen,DARKISH_GRAY,(castleX+10+25*count,castleY+30),(castleX+10+25*count,castleY+CASTLE_HEIGHT),3)
    for count in range(12):
        pygame.draw.line(screen,DARKISH_GRAY,(castleX,castleY+30+50*count),(castleX+CASTLE_WIDTH,castleY+30+50*count),3)
    pygame.draw.line(screen,DARKISH_GRAY,(castleX-30,castleY+30),(castleX+130,castleY+30),3)
    
    pygame.draw.line(screen,DARKISH_GRAY,(castleX-30,castleY+10),(castleX+130,castleY+10),3)
    pygame.draw.line(screen,DARKISH_GRAY,(castleX-30,castleY-10),(castleX+130,castleY-10),3)
    
    pygame.draw.line(screen,DARKISH_GRAY,(castleX-15,castleY-60),(castleX-15,castleY+30),3)
    pygame.draw.line(screen,DARKISH_GRAY,(castleX+17,castleY-10),(castleX+17,castleY+30),3)
    pygame.draw.line(screen,DARKISH_GRAY,(castleX+50,castleY-60),(castleX+50,castleY+30),3)
    pygame.draw.line(screen,DARKISH_GRAY,(castleX+82,castleY-10),(castleX+82,castleY+30),3)
    pygame.draw.line(screen,DARKISH_GRAY,(castleX+115,castleY-60),(castleX+115,castleY+30),3)
    
    # Windows.    
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX+26,castleY+96,48,48))
    pygame.draw.ellipse(screen,DARK_GRAY,pygame.Rect(castleX+26,castleY+66,48,68))
    pygame.draw.rect(screen,BLACK,pygame.Rect(castleX+30,castleY+100,40,40))
    pygame.draw.ellipse(screen,BLACK,pygame.Rect(castleX+30,castleY+70,40,60))
    
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX+26,castleY+256,48,48))
    pygame.draw.ellipse(screen,DARK_GRAY,pygame.Rect(castleX+26,castleY+226,48,68))
    pygame.draw.rect(screen,BLACK,pygame.Rect(castleX+30,castleY+260,40,40))
    pygame.draw.ellipse(screen,BLACK,pygame.Rect(castleX+30,castleY+230,40,60))
    
    # Flags.
    pygame.draw.rect(screen,BROWN,pygame.Rect(castleX-20,castleY-95,4,35))
    pygame.draw.polygon(screen,LIGHT_RED,[[castleX-16,castleY-95],[castleX-16,castleY-75],[castleX+15,castleY-85]])
    
    pygame.draw.rect(screen,BROWN,pygame.Rect(castleX+45,castleY-110,4,50))
    pygame.draw.polygon(screen,LIGHT_RED,[[castleX+49,castleY-110],[castleX+49,castleY-90],[castleX+80,castleY-100]])
    
    pygame.draw.rect(screen,BROWN,pygame.Rect(castleX+110,castleY-95,4,35))
    pygame.draw.polygon(screen,LIGHT_RED,[[castleX+114,castleY-95],[castleX+114,castleY-75],[castleX+145,castleY-85]])

# Making a function to draw a raindrop.
def drawRaindrop(dropX,dropY,sizeFactor):
    pygame.draw.polygon(screen,BLUE,[[dropX,dropY],[dropX-1*sizeFactor,dropY+3*sizeFactor],[dropX+1*sizeFactor,dropY+3*sizeFactor]])
    pygame.draw.arc(screen,BLUE,[(dropX-1*sizeFactor),dropY+1*sizeFactor,2*sizeFactor,4*sizeFactor],3.2,6.3,int(1*sizeFactor))
    pygame.draw.arc(screen,BLUE,[(dropX-1*sizeFactor)+1,dropY+1*sizeFactor,2*sizeFactor,4*sizeFactor],3.2,6.3,int(1*sizeFactor))
    pygame.draw.arc(screen,BLUE,[(dropX-1*sizeFactor)+2,dropY+1*sizeFactor,2*sizeFactor,4*sizeFactor],3.2,6.3,int(1*sizeFactor))

# -----------------------------------------------------------------------------------------
# Game Screens
# ----------------------------------------------------------------------------------------- 


# Making a function to draw the main menu.
def drawScene1(screen,mx,my):
    # Drawing the background.
    screen.fill(DARK_PURPLE)
    
    # Castle
    pygame.draw.rect(screen,GRAY,pygame.Rect(175,625,450,125))
    pygame.draw.rect(screen,GRAY,pygame.Rect(250,375,300,250))
    pygame.draw.rect(screen,GRAY,pygame.Rect(175,300,75,75))
    pygame.draw.rect(screen,GRAY,pygame.Rect(300,300,75,75))
    pygame.draw.rect(screen,GRAY,pygame.Rect(425,300,75,75))
    pygame.draw.rect(screen,GRAY,pygame.Rect(550,300,75,75))

    # Lightning
    pygame.draw.polygon(screen,YELLOW,[[20,60],[130,200],[170,200]])
    pygame.draw.polygon(screen,YELLOW,[[130,200],[170,200],[150,215],[110,210]])
    pygame.draw.polygon(screen,YELLOW,[[150,215],[110,210],[220,300]])
    
    pygame.draw.polygon(screen,YELLOW,[[760,0],[670,160],[630,160]])
    pygame.draw.polygon(screen,YELLOW,[[630,160],[670,160],[690,175],[650,175]])
    pygame.draw.polygon(screen,YELLOW,[[690,175],[650,175],[570,300]])
    
    # Clouds
    drawCloud(0,55,1)
    drawCloud(160,50,1.5)
    drawCloud(320,45,1.2)
    drawCloud(525,30,1.7)
    drawCloud(700,90,0.8)
    
    # Writing the title.
    gameTitle = gameTitleFont.render("DEFEND THE TOWER",1,TITLE_YELLOW)
    screen.blit(gameTitle,pygame.Rect(70,150,0,0))
    
    # Checking if the mouse is in a button and highlighting it if so.
    # Play Button
    if mx > PLAY_BUTTON_X and my > PLAY_BUTTON_Y and mx < PLAY_BUTTON_X + PLAY_BUTTON_WIDTH and my < PLAY_BUTTON_Y + PLAY_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_BLUE,playIndicator,0)
        playColor = (255,255,255)
    else:
        pygame.draw.rect(screen,BLUE,playIndicator,0)
        playColor = (0,0,0)
    # How-To-Play Button
    if mx > INSTRUCTIONS_BUTTON_X and my > INSTRUCTIONS_BUTTON_Y and mx < INSTRUCTIONS_BUTTON_X + INSTRUCTIONS_BUTTON_WIDTH and my < INSTRUCTIONS_BUTTON_Y + INSTRUCTIONS_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_GREEN,instructionsIndicator,0)
        instructionsColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GREEN,instructionsIndicator,0)
        instructionsColor = (0,0,0)
    # Quit Button
    if mx > QUIT_BUTTON_X and my > QUIT_BUTTON_Y and mx < QUIT_BUTTON_X + QUIT_BUTTON_WIDTH and my < QUIT_BUTTON_Y + QUIT_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,quitIndicator,0)
        quitColor = (255,255,255)
    else:
        pygame.draw.rect(screen,RED,quitIndicator,0)
        quitColor = (0,0,0)
    
    # Writing out the labels for the buttons.
    # Play button.
    playButton = buttonFont.render("Play",1,playColor)
    screen.blit(playButton,pygame.Rect(PLAY_BUTTON_X+140, PLAY_BUTTON_Y+10, PLAY_BUTTON_WIDTH-140, PLAY_BUTTON_HEIGHT-10))
    # How-To-Play button.
    instructionsButton = buttonFont.render("How to Play",1,instructionsColor)
    screen.blit(instructionsButton,pygame.Rect(INSTRUCTIONS_BUTTON_X+50, INSTRUCTIONS_BUTTON_Y+10, INSTRUCTIONS_BUTTON_WIDTH-50, INSTRUCTIONS_BUTTON_HEIGHT-10))
    # Quit button
    quitButton = buttonFont.render("Quit",1,quitColor)
    screen.blit(quitButton,pygame.Rect(QUIT_BUTTON_X+140, QUIT_BUTTON_Y+10, QUIT_BUTTON_WIDTH-140, QUIT_BUTTON_HEIGHT-10))    
    
    pygame.display.flip()

# Making a function to draw the game scene.
def drawScene2(screen,mx,my):
    global playerX
    global playerY
    
    # Drawing the background.
    screen.fill(DARKER_PURPLE)
    
    # -----------------------------------------------------------------------------------------
    # Environment
    # -----------------------------------------------------------------------------------------    
    
    # Drawing the lightning occasionally.
    if lightningAnimation == True:
        drawLightning(lightningX,lightningY,lightningSize)
    
    
    # Drawing the trees.
    drawTree(treeXList[0],690,treeSizeList[0])
    drawTree(treeXList[1],690,treeSizeList[1])
    drawTree(treeXList[2],690,treeSizeList[2])
    drawTree(treeXList[3],690,treeSizeList[3])
    drawTree(treeXList[4],690,treeSizeList[4])
    drawTree(treeXList[5],690,treeSizeList[5])
    drawTree(treeXList[6],690,treeSizeList[6])
    drawTree(treeXList[7],690,treeSizeList[7])
    drawTree(treeXList[8],690,treeSizeList[8])
    drawTree(treeXList[9],690,treeSizeList[9])
    
    # Drawing all the raindrops.
    for count in range(len(raindrops)):
        drawRaindrop(raindrops[count][0],raindrops[count][1],2)    
    
    # Drawing the clouds.
    drawCloud(0,160,1.4)
    drawCloud(200,175,1)
    drawCloud(325,150,0.8)
    drawCloud(350,205,0.5)
    drawCloud(450,175,1.3)
    drawCloud(550,200,1.1)
    drawCloud(630,120,1.5)
    
    # Drawing the castle.
    drawCastle(castleX,castleY)
    
    # If the castle is being destroyed, drawing the explosions.
    if explosionAnimation == True:
        pygame.draw.circle(screen,ORANGE,(explosionAnimationX,explosionAnimationY),explosionSize)
        pygame.draw.circle(screen,YELLOW,(explosionAnimationX,explosionAnimationY),explosionSize//3*2)
        
        if explosionSize2 >= 0:
            pygame.draw.circle(screen,ORANGE,(explosionAnimationX2,explosionAnimationY2),explosionSize2)
            pygame.draw.circle(screen,YELLOW,(explosionAnimationX2,explosionAnimationY2),explosionSize2//3*2)
    
    # Drawing the player.
    # Normal
    if playerState == 1:
        drawPlayer(playerX,playerY,1)
    # Recoiling
    if playerState == 2:
        drawRecoilingPlayer(playerX-25,playerY)
    # Climbing
    if playerState == 3:
        drawClimbingPlayerRight(playerX+2,playerY)
    if playerState == 4:
        drawClimbingPlayerLeft(playerX-2,playerY)
    
    # Drawing the dirt ground.
    pygame.draw.rect(screen,DARKER_BROWN,pygame.Rect(0,693,800,20))
    
    # -----------------------------------------------------------------------------------------
    # Status bar
    # -----------------------------------------------------------------------------------------    
    
    # Drawing the status bar.
    pygame.draw.rect(screen,STONE_GRAY,pygame.Rect(0,0,800,115))

    # Weapon power bar.
    powerTitle = statusBarFont.render("POWER",1,BLACK)
    pygame.draw.rect(screen,RED,pygame.Rect(POWER_X,POWER_Y,powerWidth,20))
    pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(POWER_X,POWER_Y,200,20),5)
    screen.blit(powerTitle,pygame.Rect(POWER_X,POWER_Y-24,0,0))
    
    # Health bar.
    healthTitle = statusBarFont.render("HEALTH",1,BLACK)
    if health > 0:
        pygame.draw.rect(screen,healthColor,pygame.Rect(HEALTH_X,HEALTH_Y,health*2,20))
    pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(HEALTH_X,HEALTH_Y,200,20),5)
    screen.blit(healthTitle,pygame.Rect(HEALTH_X,HEALTH_Y-24,0,0))
    
    # Weapon selection.
    # Crossbow
    screen.blit(crossbow,pygame.Rect(CROSSBOW_X,CROSSBOW_Y,50,50))
    # Highlighting the box if the crossbow is selected.
    if weapon == 1:
        pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(CROSSBOW_X-5,CROSSBOW_Y-5,60,60),8)
    else:
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(CROSSBOW_X-5,CROSSBOW_Y-5,60,60),4)
    
    # Drawing a red bar to signify the reload times.
    # Crossbow
    if crossbowReload > 0:
        pygame.draw.rect(screen,GRAY,pygame.Rect(CROSSBOW_X-1,CROSSBOW_Y+64,54,7))
        pygame.draw.rect(screen,RED,pygame.Rect(CROSSBOW_X,CROSSBOW_Y+65,(50*crossbowReload//45),5))
    # Rifle
    if rifleReload > 0:
        pygame.draw.rect(screen,GRAY,pygame.Rect(RIFLE_X-1,RIFLE_Y+64,54,7))
        pygame.draw.rect(screen,RED,pygame.Rect(RIFLE_X,RIFLE_Y+65,(50*rifleReload//150),5))
    # Missile launcher
    if rocketReload > 0:
        pygame.draw.rect(screen,GRAY,pygame.Rect(ROCKET_X-1,ROCKET_Y+64,54,7))
        pygame.draw.rect(screen,RED,pygame.Rect(ROCKET_X,ROCKET_Y+65,(50*rocketReload//300),5))    
        
    # Rifle
    screen.blit(rifle,pygame.Rect(RIFLE_X,RIFLE_Y,50,50))
    # Highlighting the box if the rifle is selected.
    if weapon == 2:
        pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(RIFLE_X-5,RIFLE_Y-5,60,60),8)
    else:
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(RIFLE_X-5,RIFLE_Y-5,60,60),4)
        
    # Rocket
    screen.blit(rocket,pygame.Rect(ROCKET_X,ROCKET_Y,50,50))
    # Highlighting the box if the rocket is selected.
    if weapon == 3:
        pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(ROCKET_X-5,ROCKET_Y-5,60,60),8)
    else:
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(ROCKET_X-5,ROCKET_Y-5,60,60),4)
        
    # Title
    weaponTitle = statusBarFont.render("WEAPONS",1,BLACK)
    screen.blit(weaponTitle,pygame.Rect(CROSSBOW_X,CROSSBOW_Y-30,0,0))
    
    # Score
    scoreTitle = scoreTitleFont.render("SCORE",1,BLACK)
    scoreNum = scoreFont.render(str(score),1,BLACK)
    screen.blit(scoreTitle,pygame.Rect(SCORE_X,SCORE_Y,0,0))
    screen.blit(scoreNum,pygame.Rect(SCORE_X,SCORE_Y+35,0,0))
    
    # -----------------------------------------------------------------------------------------
    # Enemies.
    # -----------------------------------------------------------------------------------------
    
    # Using a loop to draw all enemies that are spawned.
    for count in range(len(enemySpawned)):
        drawEnemy((enemySpawned[count][0])+40,(enemySpawned[count][1])+40,0.75)
    
    # -----------------------------------------------------------------------------------------
    # Weapon projectiles
    # -----------------------------------------------------------------------------------------
    # Making the projectiles next to the circle
    arrowY = playerY-2
    bulletY = playerY
    rocketY = playerY-2
    
    # Checking if a projectile has been fired, and drawing it if so.
    # Arrows
    if arrowFired == True:
        drawArrow(arrowX,arrowY)
    # Bullets
    if bulletFired == True:
        pygame.draw.ellipse(screen,BULLET_GOLD,pygame.Rect(bulletX+6,bulletY-4,12,8))
        pygame.draw.rect(screen,BULLET_GOLD,pygame.Rect(bulletX,bulletY-4,12,8))
    # Rockets
    if rocketFired == True:
        drawRocket(rocketX,rocketY)
    # Explosion
    if explosion == True:
        pygame.draw.circle(screen,ORANGE,(int(rocketX),rocketY),int(explosionRadius))
        pygame.draw.circle(screen,YELLOW,(int(rocketX),rocketY),int(explosionRadius-15))
    
    pygame.display.set_caption("Defend the tower!")
    pygame.display.flip()

# Making a function to draw the instructions screen.
def drawScene3(screen,mx,my):
    screen.fill(GRAY)
    
    # Drawing a sample game screen.
    # Castle
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX,castleY,CASTLE_WIDTH,CASTLE_HEIGHT))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX-30,castleY-10,CASTLE_WIDTH+60,40))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX-30,castleY-60,30,50))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX+35,castleY-60,30,50))
    pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(castleX+100,castleY-60,30,50))
    
    # Player
    drawPlayer(playerX,playerY,1)
    
    # Enemy
    drawEnemy(700,400,1)
    
    # Status bar
    # Drawing the status bar.
    pygame.draw.rect(screen,STONE_GRAY,pygame.Rect(0,0,800,115))

    # Weapon power bar.
    powerWidth = 80
    
    powerTitle = statusBarFont.render("POWER",1,BLACK)
    pygame.draw.rect(screen,RED,pygame.Rect(POWER_X,POWER_Y,powerWidth,20))
    pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(POWER_X,POWER_Y,200,20),5)
    screen.blit(powerTitle,pygame.Rect(POWER_X,POWER_Y-24,0,0))
    
    # Health bar.
    healthTitle = statusBarFont.render("HEALTH",1,BLACK)
    if health > 0:
        pygame.draw.rect(screen,healthColor,pygame.Rect(HEALTH_X,HEALTH_Y,health*2,20))
    pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(HEALTH_X,HEALTH_Y,200,20),5)
    screen.blit(healthTitle,pygame.Rect(HEALTH_X,HEALTH_Y-24,0,0))
    
    # Weapon selection.
    # Crossbow
    screen.blit(crossbow,pygame.Rect(CROSSBOW_X,CROSSBOW_Y,50,50))
    # Highlighting the box if the crossbow is selected.
    if weapon == 1:
        pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(CROSSBOW_X-5,CROSSBOW_Y-5,60,60),8)
    else:
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(CROSSBOW_X-5,CROSSBOW_Y-5,60,60),4)
    
    # Drawing a red bar to signify the reload times.
    # Crossbow
    if crossbowReload > 0:
        pygame.draw.rect(screen,GRAY,pygame.Rect(CROSSBOW_X-1,CROSSBOW_Y+64,54,7))
        pygame.draw.rect(screen,RED,pygame.Rect(CROSSBOW_X,CROSSBOW_Y+65,(50*crossbowReload//45),5))
    # Rifle
    if rifleReload > 0:
        pygame.draw.rect(screen,GRAY,pygame.Rect(RIFLE_X-1,RIFLE_Y+64,54,7))
        pygame.draw.rect(screen,RED,pygame.Rect(RIFLE_X,RIFLE_Y+65,(50*rifleReload//150),5))
    # Missile launcher
    if rocketReload > 0:
        pygame.draw.rect(screen,GRAY,pygame.Rect(ROCKET_X-1,ROCKET_Y+64,54,7))
        pygame.draw.rect(screen,RED,pygame.Rect(ROCKET_X,ROCKET_Y+65,(50*rocketReload//300),5))    
        
    # Rifle
    screen.blit(rifle,pygame.Rect(RIFLE_X,RIFLE_Y,50,50))
    # Highlighting the box if the rifle is selected.
    if weapon == 2:
        pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(RIFLE_X-5,RIFLE_Y-5,60,60),8)
    else:
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(RIFLE_X-5,RIFLE_Y-5,60,60),4)
        
    # Rocket
    screen.blit(rocket,pygame.Rect(ROCKET_X,ROCKET_Y,50,50))
    # Highlighting the box if the rocket is selected.
    if weapon == 3:
        pygame.draw.rect(screen,LIGHT_GRAY,pygame.Rect(ROCKET_X-5,ROCKET_Y-5,60,60),8)
    else:
        pygame.draw.rect(screen,DARK_GRAY,pygame.Rect(ROCKET_X-5,ROCKET_Y-5,60,60),4)
        
    # Title
    weaponTitle = statusBarFont.render("WEAPONS",1,BLACK)
    screen.blit(weaponTitle,pygame.Rect(CROSSBOW_X,CROSSBOW_Y-30,0,0))
    
    # Score
    scoreTitle = scoreTitleFont.render("SCORE",1,BLACK)
    scoreNum = scoreFont.render("500",1,BLACK)
    screen.blit(scoreTitle,pygame.Rect(SCORE_X,SCORE_Y,0,0))
    screen.blit(scoreNum,pygame.Rect(SCORE_X,SCORE_Y+35,0,0))
    
    # Writing out the title
    instructionsTitle = instructionsTitleFont.render("HOW TO PLAY",1,BLACK)
    screen.blit(instructionsTitle,pygame.Rect(210,125,0,0))
    
    # Explaining the key objectives of the game.
    pygame.draw.line(screen,BLACK,(500,600),(675,445),3)
    pygame.draw.polygon(screen,BLACK,[[680,450],[670,440],[685,435]])
    shootFont = instructionsSubtitleFont.render("Shoot the enemies!",1,BLACK)
    screen.blit(shootFont,pygame.Rect(375,600,0,0))
    
    pygame.draw.line(screen,BLACK,(685,195),(598,85),3)
    pygame.draw.polygon(screen,BLACK,[[595,90],[605,85],[592,78]])
    scoreInstructionFont = instructionsSubtitleFont.render("Score points!",1,BLACK)
    screen.blit(scoreInstructionFont,pygame.Rect(600,200,0,0))
    
    pygame.draw.line(screen,BLACK,(250,355),(165,320),3)
    pygame.draw.polygon(screen,BLACK,[[160,327],[170,312],[150,315]])
    moveInstructions = instructionsSubtitleFont.render("Move your player!",1,BLACK)
    screen.blit(moveInstructions,pygame.Rect(200,370,0,0))
    
    pygame.draw.line(screen,BLACK,(235,525),(160,525),3)
    pygame.draw.polygon(screen,BLACK,[[160,515],[160,535],[145,525]])
    defendInstruction = instructionsSubtitleFont.render("Defend the castle!",1,BLACK)
    screen.blit(defendInstruction,pygame.Rect(250,500,0,0))
    
    # Checking if the mouse is in a button and highlighting it if so.
    # Back button
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:    
        pygame.draw.rect(screen,LIGHT_GRAY,backIndicator,0)
        backColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GRAY,backIndicator,0)
        backColor = (0,0,0)
    # Next button
    if mx > NEXT_BUTTON_X and my > NEXT_BUTTON_Y and mx < NEXT_BUTTON_X + NEXT_BUTTON_WIDTH and my < NEXT_BUTTON_Y + NEXT_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_ORANGE,nextIndicator,0)
        nextColor = (255,255,255)
    else:
        pygame.draw.rect(screen,ORANGE,nextIndicator,0)
        nextColor = (0,0,0)
    
    # Writing out the label for the buttons.
    # Back button
    backButton = backButtonFont.render("BACK",1,backColor)
    screen.blit(backButton,pygame.Rect(BACK_BUTTON_X+5, BACK_BUTTON_Y+5, BACK_BUTTON_WIDTH-5, BACK_BUTTON_HEIGHT-5))
    # Next button
    nextButton = backButtonFont.render("NEXT",1,nextColor)
    screen.blit(nextButton,pygame.Rect(NEXT_BUTTON_X+5, NEXT_BUTTON_Y+5, NEXT_BUTTON_WIDTH-5, NEXT_BUTTON_HEIGHT-5))
    
    pygame.display.flip()
    

# Making a function to draw the player controls.
def drawScene3_1(screen,mx,my):
    screen.fill(DARK_GRAY)
    
    # Drawing the player (giant).
    drawPlayer(400,200,3)
    
    # Checking if the mouse is in a button and highlighting it if so.
    # Back button
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:    
        pygame.draw.rect(screen,LIGHT_GRAY,backIndicator,0)
        backColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GRAY,backIndicator,0)
        backColor = (0,0,0)
    # Next button
    if mx > NEXT_BUTTON_X and my > NEXT_BUTTON_Y and mx < NEXT_BUTTON_X + NEXT_BUTTON_WIDTH and my < NEXT_BUTTON_Y + NEXT_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_ORANGE,nextIndicator,0)
        nextColor = (255,255,255)
    else:
        pygame.draw.rect(screen,ORANGE,nextIndicator,0)
        nextColor = (0,0,0)
    # Previous button
    if mx > PREVIOUS_BUTTON_X and my > PREVIOUS_BUTTON_Y and mx < PREVIOUS_BUTTON_X + PREVIOUS_BUTTON_WIDTH and my < PREVIOUS_BUTTON_Y + PREVIOUS_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_ORANGE,previousIndicator,0)
        previousColor = (255,255,255)
    else:
        pygame.draw.rect(screen,ORANGE,previousIndicator,0)
        previousColor = (0,0,0)

    # Writing out the title.
    instructionsTitle = instructionsTitleFont.render("PLAYER CONTROLS",1,WHITE)
    screen.blit(instructionsTitle,pygame.Rect(125,375,0,0))
    
    # Writing out the controls.
    # Movement
    movementTitle = instructionsSubtitleFont.render("Movement",1,WHITE)
    screen.blit(movementTitle,pygame.Rect(100,440,0,0))
    moveUp = instructionsFont.render("Up    -     W key",1,WHITE)
    screen.blit(moveUp,pygame.Rect(100,480,0,0))
    moveDown = instructionsFont.render("Down    -     S key",1,WHITE)
    screen.blit(moveDown,pygame.Rect(100,505,0,0))
    
    # Weapon switch
    weaponTitle = instructionsSubtitleFont.render("Weapon Switch",1,WHITE)
    screen.blit(weaponTitle,pygame.Rect(275,540,0,0))
    switch1 = instructionsFont.render("Crossbow   -   1 key",1,WHITE)
    screen.blit(switch1,pygame.Rect(275,580,0,0))
    switch1 = instructionsFont.render("Rifle   -   2 key",1,WHITE)
    screen.blit(switch1,pygame.Rect(275,605,0,0))
    switch1 = instructionsFont.render("Missile Launcher   -   3 key",1,WHITE)
    screen.blit(switch1,pygame.Rect(275,630,0,0))
    
    # Weapon firing
    firingTitle = instructionsSubtitleFont.render("Firing Weapons",1,WHITE)
    screen.blit(firingTitle,pygame.Rect(500,440,0,0))
    powerWeapon = instructionsFont.render("Power up   -   Hold left-click",1,WHITE)
    screen.blit(powerWeapon,pygame.Rect(500,480,0,0))
    fireWeapon = instructionsFont.render("Fire   -   Release left-click",1,WHITE)
    screen.blit(fireWeapon,pygame.Rect(500,505,0,0))
    
    # Pausing
    pauseText = instructionsSubtitleFont.render("Pause Game   -   Esc",1,WHITE)
    screen.blit(pauseText,pygame.Rect(245,660,0,0))
    
    # Writing out the label for the buttons.
    # Back button
    backButton = backButtonFont.render("BACK",1,backColor)
    screen.blit(backButton,pygame.Rect(BACK_BUTTON_X+5, BACK_BUTTON_Y+5, BACK_BUTTON_WIDTH-5, BACK_BUTTON_HEIGHT-5))
    # Next button
    nextButton = backButtonFont.render("NEXT",1,nextColor)
    screen.blit(nextButton,pygame.Rect(NEXT_BUTTON_X+5, NEXT_BUTTON_Y+5, NEXT_BUTTON_WIDTH-5, NEXT_BUTTON_HEIGHT-5))
    # Previous button
    previousButton = backButtonFont.render("PREV",1,previousColor)
    screen.blit(previousButton,pygame.Rect(PREVIOUS_BUTTON_X+5, PREVIOUS_BUTTON_Y+5, PREVIOUS_BUTTON_WIDTH-5, PREVIOUS_BUTTON_HEIGHT-5))
    
    pygame.display.flip()

# Making a function to draw the weapon overview screen.
def drawScene3_2(screen,mx,my):
    screen.fill(DARK_GRAY)
    
    # Writing out the title.
    instructionsTitle = instructionsTitleFont.render("WEAPONS OVERVIEW",1,WHITE)
    screen.blit(instructionsTitle,pygame.Rect(125,30,0,0))
    
    # Drawing the weapons.
    # Crossbow
    drawCrossbow(125,175,4)
    drawRifle(180,370,3)
    drawMissileLauncher(180,550,3)
    
    # Explaining each weapon.
    # Crossbow
    crossbowTitle = instructionsSubtitleFont.render("Crossbow",1,WHITE)
    screen.blit(crossbowTitle,pygame.Rect(390,90,0,0))
    
    crossbowText1 = instructionsFont.render("The crossbow is a low power weapon that deals",1,WHITE)
    crossbowText2 = instructionsFont.render("moderate damage when powered up. Although it",1,WHITE)
    crossbowText3 = instructionsFont.render("seems weak, this weapon reloads the fastest",1,WHITE)
    crossbowText4 = instructionsFont.render("and earns the most points, making it the most",1,WHITE)
    crossbowText5 = instructionsFont.render("viable weapon to use of the three.",1,WHITE)
    crossbowText6 = instructionsFont.render("Max damage: 50            Score: 150",1,WHITE)
    crossbowText7 = instructionsFont.render("Reload time: 0.75 seconds",1,WHITE)
    
    screen.blit(crossbowText1,pygame.Rect(390,130,0,0))
    screen.blit(crossbowText2,pygame.Rect(390,150,0,0))
    screen.blit(crossbowText3,pygame.Rect(390,170,0,0))
    screen.blit(crossbowText4,pygame.Rect(390,190,0,0))
    screen.blit(crossbowText5,pygame.Rect(390,210,0,0))
    screen.blit(crossbowText6,pygame.Rect(390,235,0,0))
    screen.blit(crossbowText7,pygame.Rect(390,255,0,0))
    
    # Rifle
    rifleTitle = instructionsSubtitleFont.render("Rifle",1,WHITE)
    screen.blit(rifleTitle,pygame.Rect(400,290,0,0))
    
    rifleText1 = instructionsFont.render("The rifle is high power weapon. It powers up",1,WHITE)
    rifleText2 = instructionsFont.render("the fastest, deals high damage and its recoil",1,WHITE)
    rifleText3 = instructionsFont.render("is the shortest. Be careful, as the reload",1,WHITE)
    rifleText4 = instructionsFont.render("time is significantly longer than the crossbow's.",1,WHITE)
    rifleText5 = instructionsFont.render("Max damage: 100           Score: 100",1,WHITE)
    rifleText6 = instructionsFont.render("Reload time: 2 seconds",1,WHITE)
    
    screen.blit(rifleText1,pygame.Rect(400,330,0,0))
    screen.blit(rifleText2,pygame.Rect(400,350,0,0))
    screen.blit(rifleText3,pygame.Rect(400,370,0,0))
    screen.blit(rifleText4,pygame.Rect(400,390,0,0))
    screen.blit(rifleText5,pygame.Rect(400,415,0,0))
    screen.blit(rifleText6,pygame.Rect(400,435,0,0))
    
    # Missile launcher.
    launcherTitle = instructionsSubtitleFont.render("Missile Launcher",1,WHITE)
    screen.blit(launcherTitle,pygame.Rect(410,470,0,0))
    
    launcherText1 = instructionsFont.render("The missile launcher has the potential to deal",1,WHITE)
    launcherText2 = instructionsFont.render("massive damage across multiple enemies at once.",1,WHITE)
    launcherText3 = instructionsFont.render("However, it suffers from a slow power up and",1,WHITE)
    launcherText4 = instructionsFont.render("long reload time, as well as the most recoil.",1,WHITE)
    launcherText5 = instructionsFont.render("Use it only when necessary!",1,WHITE)
    launcherText6 = instructionsFont.render("Max damage: 400           Score: 75",1,WHITE)
    launcherText7 = instructionsFont.render("Reload time: 5 seconds",1,WHITE)
    
    screen.blit(launcherText1,pygame.Rect(410,510,0,0))
    screen.blit(launcherText2,pygame.Rect(410,530,0,0))
    screen.blit(launcherText3,pygame.Rect(410,550,0,0))
    screen.blit(launcherText4,pygame.Rect(410,570,0,0))
    screen.blit(launcherText5,pygame.Rect(410,590,0,0))
    screen.blit(launcherText6,pygame.Rect(410,615,0,0))
    screen.blit(launcherText7,pygame.Rect(410,635,0,0))
    
    # Checking if the mouse is in a button and highlighting it if so.
    # Back button
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:    
        pygame.draw.rect(screen,LIGHT_GRAY,backIndicator,0)
        backColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GRAY,backIndicator,0)
        backColor = (0,0,0)
    # Next button
    if mx > NEXT_BUTTON_X and my > NEXT_BUTTON_Y and mx < NEXT_BUTTON_X + NEXT_BUTTON_WIDTH and my < NEXT_BUTTON_Y + NEXT_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_ORANGE,nextIndicator,0)
        nextColor = (255,255,255)
    else:
        pygame.draw.rect(screen,ORANGE,nextIndicator,0)
        nextColor = (0,0,0)
    # Previous button
    if mx > PREVIOUS_BUTTON_X and my > PREVIOUS_BUTTON_Y and mx < PREVIOUS_BUTTON_X + PREVIOUS_BUTTON_WIDTH and my < PREVIOUS_BUTTON_Y + PREVIOUS_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_ORANGE,previousIndicator,0)
        previousColor = (255,255,255)
    else:
        pygame.draw.rect(screen,ORANGE,previousIndicator,0)
        previousColor = (0,0,0)
    
    # Writing out the label for the buttons.
    # Back button
    backButton = backButtonFont.render("BACK",1,backColor)
    screen.blit(backButton,pygame.Rect(BACK_BUTTON_X+5, BACK_BUTTON_Y+5, BACK_BUTTON_WIDTH-5, BACK_BUTTON_HEIGHT-5))
    # Next button
    nextButton = backButtonFont.render("NEXT",1,nextColor)
    screen.blit(nextButton,pygame.Rect(NEXT_BUTTON_X+5, NEXT_BUTTON_Y+5, NEXT_BUTTON_WIDTH-5, NEXT_BUTTON_HEIGHT-5))
    # Previous button
    previousButton = backButtonFont.render("PREV",1,previousColor)
    screen.blit(previousButton,pygame.Rect(PREVIOUS_BUTTON_X+5, PREVIOUS_BUTTON_Y+5, PREVIOUS_BUTTON_WIDTH-5, PREVIOUS_BUTTON_HEIGHT-5))
    
    pygame.display.flip()    

# Making a function to draw the enemy overview screen.
def drawScene3_3(screen,mx,my):
    screen.fill(GRAY)
    
    # Writing out the title.
    instructionsTitle = instructionsTitleFont.render("E-WASTE BOT OVERVIEW",1,WHITE)
    screen.blit(instructionsTitle,pygame.Rect(50,50,0,0))
    
    # Drawing a giant enemy.
    drawEnemy(400,300,4)
    
    # Explaining enemy stats.
    enemyHealth = instructionsSubtitleFont.render("Base Health: 50",1,BLACK)
    enemyHealthIncrease = instructionsSubtitleFont.render("Health Increase: 10",1,BLACK)
    
    enemyDamage = instructionsSubtitleFont.render("Base Damage: 10",1,BLACK)
    enemyDamageIncrease = instructionsSubtitleFont.render("Damage Increase: 2",1,BLACK)
    
    increaseExplanation = instructionsSubtitleFont.render("The enemy's stats increase every 2500 score you gain.",1,BLACK)
    
    screen.blit(enemyHealth,pygame.Rect(50,490,0,0))
    screen.blit(enemyHealthIncrease,pygame.Rect(50,530,0,0))
    screen.blit(enemyDamage,pygame.Rect(450,490,0,0))
    screen.blit(enemyDamageIncrease,pygame.Rect(450,530,0,0))
    screen.blit(increaseExplanation,pygame.Rect(20,580,0,0))
    
    # Checking if the mouse is in a button and highlighting it if so.
    # Back button
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:    
        pygame.draw.rect(screen,LIGHT_GRAY,backIndicator,0)
        backColor = (255,255,255)
    else:
        pygame.draw.rect(screen,(150,150,150),backIndicator,0)
        backColor = (0,0,0)
    # Previous button
    if mx > PREVIOUS_BUTTON_X and my > PREVIOUS_BUTTON_Y and mx < PREVIOUS_BUTTON_X + PREVIOUS_BUTTON_WIDTH and my < PREVIOUS_BUTTON_Y + PREVIOUS_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_ORANGE,previousIndicator,0)
        previousColor = (255,255,255)
    else:
        pygame.draw.rect(screen,ORANGE,previousIndicator,0)
        previousColor = (0,0,0)    
    
    # Writing out the label for the buttons.
    # Back button
    backButton = backButtonFont.render("BACK",1,backColor)
    screen.blit(backButton,pygame.Rect(BACK_BUTTON_X+5, BACK_BUTTON_Y+5, BACK_BUTTON_WIDTH-5, BACK_BUTTON_HEIGHT-5))
    # Previous button
    previousButton = backButtonFont.render("PREV",1,previousColor)
    screen.blit(previousButton,pygame.Rect(PREVIOUS_BUTTON_X+5, PREVIOUS_BUTTON_Y+5, PREVIOUS_BUTTON_WIDTH-5, PREVIOUS_BUTTON_HEIGHT-5))
    
    pygame.display.flip()

# Making a function to draw the pause scene.
def drawScene4(screen,mx,my):
    screen.fill(YELLOW_GRAY)
    
    # Drawing the buttons and highlighting them if the mouse is on them.
    # Resume button.
    if mx > RESUME_BUTTON_X and my > RESUME_BUTTON_Y and mx < RESUME_BUTTON_X + RESUME_BUTTON_WIDTH and my < RESUME_BUTTON_Y + RESUME_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_YELLOW,resumeIndicator)
        resumeColor = (255,255,255)
    else:
        pygame.draw.rect(screen,YELLOW,resumeIndicator)
        resumeColor = (0,0,0)
    
    # Main Menu button.
    if mx > RETURN_BUTTON_X and my > RETURN_BUTTON_Y and mx < RETURN_BUTTON_X + RETURN_BUTTON_WIDTH and my < RETURN_BUTTON_Y + RETURN_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_PURPLE,returnIndicator)
        returnColor = (255,255,255)
    else:
        pygame.draw.rect(screen,PURPLE,returnIndicator)
        returnColor = (0,0,0)
    
    # Writing the title of the pause menu.
    pauseTitle = titleFont.render("PAUSED",1,BLACK)
    screen.blit(pauseTitle,pygame.Rect(240,100,0,0))
    
    # Writing the labels for the buttons.
    # Resume button.
    resumeButton = buttonFont.render("RESUME",1,resumeColor)
    screen.blit(resumeButton,pygame.Rect(RESUME_BUTTON_X+120, RESUME_BUTTON_Y+15, RESUME_BUTTON_WIDTH-70, RESUME_BUTTON_HEIGHT-5))
    # Return button.
    returnButton = buttonFont.render("RETURN TO MENU",1,returnColor)
    screen.blit(returnButton,pygame.Rect(RETURN_BUTTON_X+7, RETURN_BUTTON_Y+15, RETURN_BUTTON_WIDTH-7, RETURN_BUTTON_HEIGHT-5))
    
    pygame.display.set_caption("Paused...")
    pygame.display.flip()

def drawScene5(screen,mx,my):
    # Drawing the background and the game over title.
    screen.fill(DARK_RED)
    # Game over text.
    gameOver = gameOverFont.render("GAME OVER",1,BLACK)
    screen.blit(gameOver,pygame.Rect(160,100,0,0))
    # New high score text.
    if newHighScore == True:
        newScoreText = finalScoreFont.render("NEW HIGH SCORE!",1,WHITE)
        screen.blit(newScoreText,pygame.Rect(175,200,0,0))
    # User's score
    finalScoreText = finalScoreFont.render("YOUR SCORE:",1,BLACK)
    finalScore = finalScoreFont.render(str(score),1,BLACK)
    screen.blit(finalScoreText,pygame.Rect(150,270,0,0))
    screen.blit(finalScore,pygame.Rect(500,270,0,0))
    # High scores.
    highScoresTitle = finalScoreFont.render("HIGH SCORES",1,BLACK)
    screen.blit(highScoresTitle,pygame.Rect(240,360,0,0))
    
    # Writing the high score in white if it is new, else it is black.
    highScore1 = ("1. "+str(highScores[0]))
    if highScores[0] == score:
        highScoreBoard1 = buttonFont.render(highScore1,1,newHighScoreColor)
    else:
        highScoreBoard1 = buttonFont.render(highScore1,1,BLACK)
    highScore2 = ("2. "+str(highScores[1]))
    if highScores[1] == score:
        highScoreBoard2 = buttonFont.render(highScore2,1,WHITE)
    else:
        highScoreBoard2 = buttonFont.render(highScore2,1,BLACK)
    highScore3 = ("3. "+str(highScores[2]))
    if highScores[2] == score:
        highScoreBoard3 = buttonFont.render(highScore3,1,WHITE)
    else:
        highScoreBoard3 = buttonFont.render(highScore3,1,BLACK)
    
    # Writing the scores.
    screen.blit(highScoreBoard1,pygame.Rect(240,410,0,0))
    screen.blit(highScoreBoard2,pygame.Rect(240,460,0,0))
    screen.blit(highScoreBoard3,pygame.Rect(240,510,0,0))
    
    # Return to menu button.
    if mx > RETURN_BUTTON2_X and my > RETURN_BUTTON2_Y and mx < RETURN_BUTTON2_X + RETURN_BUTTON2_WIDTH and my < RETURN_BUTTON2_Y + RETURN_BUTTON2_HEIGHT:
        pygame.draw.rect(screen,GREEN,return2Indicator)
        returnColor2 = (255,255,255)
    else:
        pygame.draw.rect(screen,DARK_GREEN,return2Indicator)
        returnColor2 = (0,0,0)
    # Quit button.
    if mx > QUIT_BUTTON2_X and my > QUIT_BUTTON2_Y and mx < QUIT_BUTTON2_X + QUIT_BUTTON2_WIDTH and my < QUIT_BUTTON2_Y + QUIT_BUTTON2_HEIGHT:
        pygame.draw.rect(screen,CYAN,quit2Indicator)
        quitColor2 = (255,255,255)
    else:
        pygame.draw.rect(screen,DARK_CYAN,quit2Indicator)
        quitColor2 = (0,0,0)
    
    # Writing the labels for the buttons.
    # Return to menu button.
    returnButton2 = buttonFont.render("MENU",1,returnColor2)
    screen.blit(returnButton2,pygame.Rect(RETURN_BUTTON2_X+40,RETURN_BUTTON2_Y+10,0,0))
    # Quit button.
    quitButton2 = buttonFont.render("QUIT",1,quitColor2)
    screen.blit(quitButton2,pygame.Rect(QUIT_BUTTON2_X+40,QUIT_BUTTON2_Y+10,0,0))
    
    pygame.display.flip()

# Making a function to know which scene to draw.
def drawScene():
    if scene == 1:
        drawScene1(screen,mx,my)
    if scene == 2:
        drawScene2(screen,mx,my)
    if scene == 3:
        drawScene3(screen,mx,my)
    if scene == 3.1:
        drawScene3_1(screen,mx,my)
    if scene == 3.2:
        drawScene3_2(screen,mx,my)
    if scene == 3.3:
        drawScene3_3(screen,mx,my)
    if scene == 4:
        drawScene4(screen,mx,my)
    if scene == 5:
        drawScene5(screen,mx,my)

# Making a function to get the coordinates of the mouse and checking if it's pressed.
def getMouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)

# Making a loop to constantly get the mouse position, draw the scenes and run the events..
running = True
myClock = pygame.time.Clock()

while running:
    # -----------------------------------------------------------------------------------------
    # Events
    # -----------------------------------------------------------------------------------------
    
    # Making a loop to check for any events.
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            mb = evnt.button
        if evnt.type == pygame.KEYDOWN:
            pressedKey = evnt.key
    
    # Using the functions.
    mx, my, mb = getMouse()
    pressedKey = pygame.key.get_pressed()
    drawScene()
    
    # -----------------------------------------------------------------------------------------
    # Enemy movements
    # -----------------------------------------------------------------------------------------
    
    for count in range(len(enemySpawned)):
        if scene == 2:
            enemySpawned[count][0] += targetMove
            if enemySpawned[count][1] > 225 and enemySpawned[count][1] < 600:
                enemySpawned[count][1] += enemySpawned[count][3]
    
    # -----------------------------------------------------------------------------------------
    # Responding to user input
    # -----------------------------------------------------------------------------------------
    
    # Checking if the user wants to move the circle.
    # Moving up.
    if pressedKey[pygame.K_w] and scene == 2 and recoil == False:
        if playerY-circleRadius > castleY:
            playerY -= 4
            footsteps.play()
        # Swiching between two images to make the player appear as if they are climbing.
        if playerState == 1:
            playerState = 4
        
        if playerState == 3:
            playerState = 4
        elif playerState == 4:
            playerState = 3
    
    # Moving down.
    if pressedKey[pygame.K_s] and scene == 2 and recoil == False:
        if playerY+circleRadius < castleY+CASTLE_HEIGHT-25:
            playerY += 4
            footsteps.play()
            # Swiching between two images to make the player appear as if they are climbing.
            if playerState == 1:
                playerState = 4
            
            if playerState == 3:
                playerState = 4
            elif playerState == 4:
                playerState = 3
    elif pressedKey[pygame.K_w] == False and recoil == False:
        playerState = 1
    
    # Using the escape button to pause the game.
    if pressedKey[pygame.K_ESCAPE] and scene == 2:
        scene = 4
        # Pausing the rain sound.
        pygame.mixer.music.pause()
    
    # -----------------------------------------------------------------------------------------
    # Firing weapons
    # -----------------------------------------------------------------------------------------
    
    # Powering up
    if mb == 1 and my > 100 and scene == 2 and recoil == False and weapon == 1 and crossbowReload == 0 or mb == 1 and my > 100 and scene == 2 and recoil == False and weapon == 2 and rifleReload == 0 or mb == 1 and my > 100 and scene == 2 and recoil == False and weapon == 3 and rocketReload == 0:
        if powerWidth < 200:
            powerWidth += 4*powerRate
        if powerWidth > 200:
            powerWidth = 200
    # Releasing power
    if mb == 0 and powerWidth > 0 and scene == 2 and recoil == False:
        # Firing the projectile of the respective weapon.
        # Crossbow
        if weapon == 1:
            weaponFired = 1
        # Rifle
        if weapon == 2:
            weaponFired = 2
        # Missile launcher
        if weapon == 3:
            weaponFired = 3
            
    # Moving the projectile.
    # Arrow
    if weaponFired == 1 and recoil == False and scene == 2:
        # Indicating an arrow was fired.
        arrowFired = True
        # Setting reload time.
        crossbowReload = 45
        # Setting recoil to immobilize the player.
        recoil = True
        playerState = 2
        weaponFired = 0
        # Playing the crossbow sound.
        crossbowFiring.play()
        
    if arrowFired == True and scene == 2:
        # Moving the arrow.
        arrowX += 12*(powerWidth/200)
        # Updating the timer to ensure a certain time the arrow stays moving (range).
        arrowTimer += 1
        
    # Checking if the arrow has reached its limit for time.
    if arrowTimer == 48 and scene == 2:
        # Deleting the arrow.
        arrowFired = False
        # Resetting the arrow's position.
        arrowX = playerX+25
        # Resetting the arrow timer.
        arrowTimer = 0
        # Resetting variables used in firing a weapon.
        weaponFired = 0
        powerWidth = 0
        # Removing recoil.
        recoil = False
        playerState = 1
    
    # Updating reload timer until it is 0.
    if crossbowReload > 0:
        crossbowReload -= 1
    
    # Bullet
    if weaponFired == 2 and scene == 2:
        # indicating a bullet was fired.
        bulletFired = True
        # Setting reload time for the rifle.
        rifleReload = 150
        # Setting recoil to immobilize the player.
        recoil = True
        playerState = 2
        weaponFired = 0
        # Playing the gunshot sound
        gunshot.play()
    if bulletFired == True and scene == 2:
        # Moving the bullet.
        bulletX += 32*(powerWidth/200)
        # Updating the timer to ensure a certain time the bullet stays moving (range).
        bulletTimer += 1
    # Checking if the bullet has reached its limit for time.
    if bulletTimer == 25 and scene == 2:
        # Deleting the bullet.
        bulletFired = False
        # Resetting the bullet's position.
        bulletX = playerX+65
        # Resetting the bullet timer.
        bulletTimer = 0
        # Removing recoil.
        recoil = False
        playerState = 1
        # Resetting variables used in firing a weapon.
        weaponFired = 0
        powerWidth = 0
    
    # Updating the rifle's reload time.
    if rifleReload > 0:
        rifleReload -= 1
    
    # Rocket
    if weaponFired == 3 and scene == 2:
        # Indicating a rocket was fired.
        rocketFired = True
        # Setting a reload time for the launcher.
        rocketReload = 300
        # Setting recoil to immobilize the player.
        recoil = True
        playerState = 2
        weaponFired = 0
        # Playing the missile firing sound.
        missileFiring.play()
    if rocketFired == True and scene == 2 and weapon == 3:
        # Moving the rocket.
        rocketX += 20*(powerWidth/200)
        # Updating the timer to ensure a certain time the rocket stays moving (range).
        rocketTimer += 1
    # Checking if the rocket has reached its limit for time.
    if rocketTimer == 30 and scene == 2 and weapon == 3:
        # Deleting the rocket.
        rocketFired = False
        # Making the explosion.
        explosion = True
    if explosion == True:
        # Increasing the size of the explosion.
        explosionRadius += 2.5
    if explosionRadius > 60:
        # Deleting the explosion
        explosion = False
        explosionRadius = 15
        # Resetting the rocket's position.
        rocketX = playerX + 65
        # Resetting the rocket timer.
        rocketTimer = 0
        # Removing recoil.
        recoil = False
        playerState = 1
        # Resetting variables used in firing a weapon.
        weaponFired = 0
        powerWidth = 0
    
    # Updating the rocket's reload time.
    if rocketReload > 0:
        rocketReload -= 1
    
    # Checking if the user is selecting a weapon.
    if pressedKey[pygame.K_1] and scene == 2 and recoil == False and weapon != 1:
        weapon = 1
        powerRate = 1
        # Resetting power.
        powerWidth = 0
    if pressedKey[pygame.K_2] and scene == 2 and recoil == False and weapon != 2:
        weapon = 2
        powerRate = 1.5
        # Resetting power.
        powerWidth = 0
    if pressedKey[pygame.K_3] and scene == 2 and recoil == False and weapon != 3:
        weapon = 3
        powerRate = 0.5
        # Resetting power.
        powerWidth = 0

    # -----------------------------------------------------------------------------------------
    # Enemy spawning.
    # -----------------------------------------------------------------------------------------
    # Increasing the chance of an enemy spawning based on score.
    spawnChance = 2 + 1*scoreDifficulty
    # Increasing maximum enemies allowed on screen based on score.
    maxSpawn = 2 + 0.5*scoreDifficulty
    # Using a random variable to have a small chance of spawning an enemy.
    spawnTry= random.randint(1,100)
    
    # If the right number is chosen and not too many enemies already exist, spawning a new enemy.
    if spawnTry < spawnChance and (len(enemySpawned)) < int(maxSpawn):
        enemyY = random.randint(225,625)
        # Making the enemy move a small, random amount up or down as it moves across screen.
        enemyYMove = round(random.uniform(-0.75,0.75),1)
        # Increasing the enemy's health based on the score.
        enemySpawned.append([900,enemyY,int(50+10*scoreDifficulty),enemyYMove])
    
    # -----------------------------------------------------------------------------------------
    # Collision detection.
    # -----------------------------------------------------------------------------------------     
    # Checking if a projectile's coordinates collide with the enemy coordinates and it is in line with the character.
    # Arrow
    for count in range(len(enemySpawned)):
        if arrowX+20 > enemySpawned[count][0] and playerY > enemySpawned[count][1] and playerY < enemySpawned[count][1] + targetHeight:
            # Dealing damage to the enemy.
            enemySpawned[count][2] -= 50*(powerWidth/200)
            # Deleting the enemy if they lose all their health.
            if enemySpawned[count][2] <= 0:
                removePos = enemySpawned[count]
                enemySpawned.remove(removePos)
                # Adding score.
                score += 150
                scoreCheck += 150
                # Playing the death sound.
                robotDeath.play()
    
            # Resetting arrow.
            arrowFired = False
            arrowX = playerX+25
            arrowTimer = 0
            # Resetting power.
            powerWidth = 0
            # Removing recoil.
            recoil = False
            playerState = 1
            
            # Breaking out of the loop to avoid errors due to the change in list length.
            break
    
        
        # Bullet
        if bulletX+12 > enemySpawned[count][0] and playerY > enemySpawned[count][1] and playerY < enemySpawned[count][1] + targetHeight:
            # Dealing damage to the enemy.
            enemySpawned[count][2] -= 100*(powerWidth/200)
            # Deleting the enemy if they lose all their health.
            if enemySpawned[count][2] <= 0:
                removePos = enemySpawned[count]
                enemySpawned.remove(removePos)
                # Adding score.
                score += 100
                scoreCheck += 100
                # Playing the death sound.
                robotDeath.play()
            
            # Resetting bullet.
            bulletFired = False
            bulletX = playerX+25
            bulletTimer = 0
            # Resetting power.
            powerWidth = 0
            # Removing recoil.
            recoil = False
            playerState = 1
            
            # Breaking out of the loop to avoid errors due to the change in list length.
            break
        
        # Rocket
        if rocketX+20 > enemySpawned[count][0] and playerY > enemySpawned[count][1] and playerY < enemySpawned[count][1] + targetHeight and rocketFired == True or rocketX+20 > enemySpawned[count][0] and playerY > enemySpawned[count][1] and playerY < enemySpawned[count][1] + targetHeight and explosion == True:
            # Creating an explosion.
            explosion = True
            # Deleting the rocket.
            rocketFired = False
            rocketTimer = 0
            # Dealing damage to the enemy.
            enemySpawned[count][2] -= 8*(powerWidth/200)
            # Deleting the enemy if they lose all their health.
            if enemySpawned[count][2] <= 0:
                removePos = enemySpawned[count]
                enemySpawned.remove(removePos)
                # Adding score.
                score += 75
                scoreCheck += 75
                # Playing the death sound.
                robotDeath.play()
                
                # Breaking out of the loop to avoid errors due to the change in list length.
                break
        
        # Explosion, checks if the enemy's coordinates are within the explosion of the rocket.
        if enemySpawned[count][0] > rocketX - explosionRadius and enemySpawned[count][1] > playerY - explosionRadius and enemySpawned[count][0] < rocketX + explosionRadius and enemySpawned[count][1] + explosionRadius:
            # Dealing damage to the enemy.
            enemySpawned[count][2] -= 8*(powerWidth/200)
            # Deleting the enemy if they lose all their health.
            if enemySpawned[count][2] <= 0:
                removePos = enemySpawned[count]
                enemySpawned.remove(removePos)
                # Adding score.
                score += 75
                scoreCheck += 75
                # Playing the death sound.
                robotDeath.play()
                
                # Breaking out of the loop to avoid errors due to the change in list length.
                break
        
    # Checking if an enemy hit the castle.
    for count in range(len(enemySpawned)):
        if enemySpawned[count][0] < castleX + CASTLE_WIDTH:
            # Increasing damage dealt as the score increases.
            health -= int(10+2*scoreDifficulty)
            # Deleting the enemy.
            removePos = enemySpawned[count]
            enemySpawned.remove(removePos)
            
            # Breaking out of the loop to avoid errors due to the change in list length.
            break
        
    # Changing the health bar color based on remaining health.
    if health > 50:
        healthColor = (0,255,0)
    if health <= 50 and health > 20:
        healthColor = (255,255,0)
    if health <= 20:
        healthColor = (255,0,0)
    
    # Playing an animation of the castle being destroyed if the user's health becomes zero.
    if health <= 0 and scene == 2:
        castleX += 5
        pygame.time.wait(1000)
        
        
        # Pausing the rain sound and playing a rumbling sound.
        pygame.mixer.music.pause()
        rumbling.play()
        
        for count in range(100):            
            # Moving the castle left and right quickly to make it look like it is shaking.
            castleX -= 10
            
            # Continuing the rain animation.
            for count in range(len(raindrops)):
                raindrops[count][1] += 5
                # Bringing the raindrops back to the top of the screen if they reach the bottom.
                if raindrops[count][1] > 700:
                    raindrops[count][0] = random.randint(5,795)
                    raindrops[count][1] = random.randint(130,160)             
            
            # Redrawing the background
            drawScene2(screen,mx,my)
            
            # Flipping the screen and waiting a bit.
            pygame.display.flip()
            pygame.time.wait(20)

            castleX += 10
            
            # Continuing the rain animation.
            for count in range(len(raindrops)):
                raindrops[count][1] += 5
                # Bringing the raindrops back to the top of the screen if they reach the bottom.
                if raindrops[count][1] > 700:
                    raindrops[count][0] = random.randint(5,795)
                    raindrops[count][1] = random.randint(130,160)             
            
            # Redrawing the background
            drawScene2(screen,mx,my)
            
            # Flipping the screen and waiting a bit.
            pygame.display.flip()
            pygame.time.wait(20)
            
        # Indicating the castle has died to draw the explosions.
        explosionAnimation = True
        
        for count in range(140):
            # Resetting the explosion if it has gotten too large.
            # Explosion 1
            if explosionSize > 45:
                explosionSize = 1
                # Playing a sound if castle is falling.
                if boomPlayed == False:
                    powSound.play()
                if castleY < 700:
                    explosionAnimationX = random.randint(25,200)
                    explosionAnimationY = random.randint(castleY,700)
            elif explosionSize < 45:
                explosionSize += 8
                
            # Explosion 2
            if explosionSize2 > 45:
                explosionSize2 = 1
                # Playing a sound if castle is falling.
                if boomPlayed == False:
                    powSound.play()
                if castleY < 700:
                    explosionAnimationX2 = random.randint(25,200)
                    explosionAnimationY2 = random.randint(castleY,800)
            elif explosionSize2 < 45:
                explosionSize2 += 8
            
            # Stopping the explosions if the castle has gone off screen.
            if castleY > 800 and boomPlayed == False:
                explosionAnimation = False
                # Playing the boom.
                boom.play()
                boomPlayed = True
                
            # Doing the same shaking as above, but also slowly lowering the castle.
            castleX -= 10
            castleY += 4
            
            # Continuing the rain animation.
            for count in range(len(raindrops)):
                raindrops[count][1] += 5
                # Bringing the raindrops back to the top of the screen if they reach the bottom.
                if raindrops[count][1] > 700:
                    raindrops[count][0] = random.randint(5,795)
                    raindrops[count][1] = random.randint(130,160)            
            
            # Redrawing the background.
            drawScene2(screen,mx,my)
            
            # Flipping the screen and waiting a bit.
            pygame.display.flip()
            pygame.time.wait(20)
            
            # Continuing the animation.
            castleX += 10
            castleY += 4
            
            # Continuing the rain animation.
            for count in range(len(raindrops)):
                raindrops[count][1] += 5
                # Bringing the raindrops back to the top of the screen if they reach the bottom.
                if raindrops[count][1] > 700:
                    raindrops[count][0] = random.randint(5,795)
                    raindrops[count][1] = random.randint(130,160)             
            
            # Redrawing the background.
            drawScene2(screen,mx,my)
            
            # Flipping the screen and waiting a bit.
            pygame.display.flip()
            pygame.time.wait(20)
        
        # Playing the falling sound.
        fallingSound.play()
        
        # Making the player fall from the screen.
        for count in range(120):
            playerY += 10
            playerState = 2
            
            # Continuing the rain animation.
            for count in range(len(raindrops)):
                raindrops[count][1] += 5
                # Bringing the raindrops back to the top of the screen if they reach the bottom.
                if raindrops[count][1] > 700:
                    raindrops[count][0] = random.randint(5,795)
                    raindrops[count][1] = random.randint(130,160)             
            
            drawScene2(screen,mx,my)
            
            # Flipping the screen and waiting a bit.
            pygame.display.flip()
            pygame.time.wait(20)
        
        # Updating the scores.
        highScores.append(score)
        
        # Checking if the score is one of the top 3.
        for count in range(3):
            if score > highScores[count]:
                newHighScore = True
        highScores.sort(reverse=True)
        
        # Writing it into the score file.
        scoreUpdate.write(str(score)+"\n")
        
        # Going to the game over screen and playing the game over sound.
        fallingSound.stop()
        gameOverSound.play()
        scene = 5
        
    # -----------------------------------------------------------------------------------------
    # Other animations.
    # -----------------------------------------------------------------------------------------     
    # Making a random chance to make lightning.
    if lightningAnimation == False and scene == 2:
        lightningSpawnTry = random.randint(1,500)
        if lightningSpawnTry < 2:
            lightningX = random.randint(50,800)
            lightningY = random.randint(175,225)
            lightningSize = 1
            lightningAnimation = True
            thunderStrike.play()
    
    # If there is lightning, increasing its size over time.
    if lightningAnimation == True and scene == 2:
        lightningSize += 0.8
        if lightningSize > 25:
            lightningAnimation = False
    
    # Moving the rain down the screen.
    for count in range(len(raindrops)):
        raindrops[count][1] += 5
        # Bringing the raindrops back to the top of the screen if they reach the bottom.
        if raindrops[count][1] > 700:
            raindrops[count][0] = random.randint(5,795)
            raindrops[count][1] = random.randint(130,160)
    
    # Playing the rain sound effect.
    if scene == 2:
        pygame.mixer.music.play(1)
    
    # -----------------------------------------------------------------------------------------
    # Score checking
    # -----------------------------------------------------------------------------------------    
    # Every time the user get 2500 points, the game will get slightly harder.
    if scoreCheck >= 2500:
        scoreDifficulty += 1
        scoreCheck = 0
    
    # -----------------------------------------------------------------------------------------
    # Buttons and mouse input
    # -----------------------------------------------------------------------------------------    
    
    # Making the buttons to do what they're supposed to by checking if the user clicked inside of them in the appropriate scene.
    # Play Button
    if mb == 1 and mx > PLAY_BUTTON_X and my > PLAY_BUTTON_Y and mx < PLAY_BUTTON_X + PLAY_BUTTON_WIDTH and my < PLAY_BUTTON_Y + PLAY_BUTTON_HEIGHT and scene == 1:
        scene = 2
        
        # Resetting all the variables for the game.
        weapon = 1
        weaponFired = 0
        
        castleX = 40
        castleY = 240
        health = 100
        
        explosionAnimation = False
        explosionAnimationX = 120
        explosionAnimationY = 300
        explosionSize = 1
        
        score = 0
        scoreCheck = 0
        scoreDifficulty = 0
        newHighScore = False
        
        playerY = 300
        recoil = False
        playerState = 1
        
        arrowFired = False
        arrowX = playerX+25
        arrowTimer = 0
        crossbowReload = 0
        
        bulletFired = False
        bulletX = playerX+65
        bulletTimer = 0
        rifleReload = 0
        
        rocketFired = False
        rocketX = playerX+65
        rocketTimer = 0
        rocketReload = 0
        explosion = False
        
        enemySpawned = []
        
        powerWidth = 0
        powerRate = 1
        
        # Re-randomizing the tree x-values and sizes.
        treeXList = []
        treeSizeList = []
        for count in range(10):
            treeXList.append(random.randint(200,750))
            treeSizeList.append(round(random.uniform(0.5,1.5),1))
        
        # Waiting a bit to avoid double-clicking.
        pygame.time.wait(200)
        
    # How-To-Play Button
    if mb == 1 and mx > INSTRUCTIONS_BUTTON_X and my > INSTRUCTIONS_BUTTON_Y and mx < INSTRUCTIONS_BUTTON_X + INSTRUCTIONS_BUTTON_WIDTH and my < INSTRUCTIONS_BUTTON_Y + INSTRUCTIONS_BUTTON_HEIGHT and scene == 1:
        scene = 3
        
        # Resetting position of player and castle.
        playerY = 300
        
        castleX = 40
        caslteY = 240
        
    # Quit button.
    if mb == 1 and mx > QUIT_BUTTON_X and my > QUIT_BUTTON_Y and mx < QUIT_BUTTON_X + QUIT_BUTTON_WIDTH and my < QUIT_BUTTON_Y + QUIT_BUTTON_HEIGHT and scene == 1:
        running = False
    # Back button (how-to-play screen).
    if mb == 1 and mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT and scene >= 3 and scene < 4:
        scene = 1
    # Next button (how-to-play screen).
    if mb == 1 and mx > NEXT_BUTTON_X and my > NEXT_BUTTON_Y and mx < NEXT_BUTTON_X + NEXT_BUTTON_WIDTH and my < NEXT_BUTTON_Y + NEXT_BUTTON_HEIGHT and scene > 2.9 and scene < 3.3:
        if scene == 3:
            scene = 3.1
            # Waiting a bit to avoid double-clicking.
            pygame.time.wait(200)
        elif scene == 3.1:
            scene = 3.2
            # Waiting a bit to avoid double-clicking.
            pygame.time.wait(200)
        elif scene == 3.2:
            scene = 3.3
            # Waiting a bit to avoid double-clicking.
            pygame.time.wait(200)
    # Previous button (how-to-play screen).
    if mb == 1 and mx > PREVIOUS_BUTTON_X and my > PREVIOUS_BUTTON_Y and mx < PREVIOUS_BUTTON_X + PREVIOUS_BUTTON_WIDTH and my < PREVIOUS_BUTTON_Y + PREVIOUS_BUTTON_HEIGHT and scene > 3 and scene < 4:
        if scene == 3.1:
            scene = 3
            # Waiting a bit to avoid double-clicking.
            pygame.time.wait(200)
        elif scene == 3.2:
            scene = 3.1
            # Waiting a bit to avoid double-clicking.
            pygame.time.wait(200)
        elif scene == 3.3:
            scene = 3.2
            # Waiting a bit to avoid double-clicking.
            pygame.time.wait(200)
    # Resume button (pause screen).
    if mb == 1 and mx > RESUME_BUTTON_X and my > RESUME_BUTTON_Y and mx < RESUME_BUTTON_X + RESUME_BUTTON_WIDTH and my < RESUME_BUTTON_Y + RESUME_BUTTON_HEIGHT and scene == 4:
        scene = 2
        # Waiting a bit to avoid double-clicking.
        pygame.time.wait(200)
    # Return button (pause screen).
    if mb == 1 and mx > RETURN_BUTTON_X and my > RETURN_BUTTON_Y and mx < RETURN_BUTTON_X + RETURN_BUTTON_WIDTH and my < RETURN_BUTTON_Y + RETURN_BUTTON_HEIGHT and scene == 4:
        scene = 1
        # Waiting a bit to avoid double-clicking.
        pygame.time.wait(200)
    # Return button (game over screen).
    if mb == 1 and mx > RETURN_BUTTON2_X and my > RETURN_BUTTON2_Y and mx < RETURN_BUTTON2_X + RETURN_BUTTON2_WIDTH and my < RETURN_BUTTON2_Y + RETURN_BUTTON2_HEIGHT and scene == 5:
        scene = 1
        # Waiting a bit to avoid double-clicking.
        pygame.time.wait(200)
    # Quit button (game over screen).
    if mb == 1 and mx > QUIT_BUTTON2_X and my > QUIT_BUTTON2_Y and mx < QUIT_BUTTON2_X + QUIT_BUTTON2_WIDTH and my < QUIT_BUTTON2_Y + QUIT_BUTTON2_HEIGHT and scene == 5:
        running = False
    
    # Making a framerate that increases based on the difficulty to make the game faster.
    frameRate = 60 + (5*scoreDifficulty)
    
    myClock.tick(frameRate)

pygame.quit()

# Closing the files.
scoreRecord.close()
scoreUpdate.close()