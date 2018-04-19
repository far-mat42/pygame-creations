# Name:          Farris Matar
# Date:          April 4, 2017
# Class:         ICS3U1-03
# Description:   Assignment 1, building a house.

# Starting up Pygame.
import pygame
import random
pygame.init()

# Setting up some variables for the screen and colours.
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
waitTime = 5000
WHITE = (255,255,255)
CLOUD1 = (86,209,255)
CLOUD2 = (127,221,255)
CLOUD3 = (163,230,255)
CLOUD4 = (209,242,255)
BLACK = (0,0,0)
RED = (255,25,0)
LIGHT_RED = (255, 142, 130)
DARK_RED = (160,15,0)
GLASS = (204,249,255)
BROWN = (68,44,21)
DARK_BROWN = (61,38,0)
YELLOW = (255,255,0)
DOORKNOB_YELLOW = (255,204,0)
MUSTARD = (214,157,2)
BEVEL_BROWN = (168,134,94)
LIGHT_BROWN = (204,164,116)
BRICK_RED = (183,50,45)
BRICK_LINE = (255, 135, 135)
BACKGROUND = (66,191,244)
houseX = 400
houseY = 300

# Making a background.
screen.fill(BACKGROUND)
pygame.draw.circle(screen,YELLOW,(80,80),60)

# Making a function to draw background clouds.
def drawBackCloud(x,y,sizeFactor,colour):
    pygame.draw.rect(screen,colour,pygame.Rect(x,y,150*sizeFactor,30*sizeFactor))
    pygame.draw.ellipse(screen,colour,pygame.Rect(x-30*sizeFactor,y-30*sizeFactor,60*sizeFactor,60*sizeFactor))
    pygame.draw.ellipse(screen,colour,pygame.Rect(x+20*sizeFactor,y-60*sizeFactor,80*sizeFactor,80*sizeFactor))
    pygame.draw.ellipse(screen,colour,pygame.Rect(x+95*sizeFactor,y-30*sizeFactor,60*sizeFactor,60*sizeFactor))
    pygame.draw.ellipse(screen,colour,pygame.Rect(x-25*sizeFactor,y,185*sizeFactor,45*sizeFactor))
    pygame.display.flip()

# Making a function to draw the windows.
def drawWindow(windowX,windowY):
    pygame.draw.rect(screen,DARK_BROWN,pygame.Rect(windowX+27,windowY+33,55,65))
    pygame.draw.rect(screen,GLASS,pygame.Rect(windowX+32.5,windowY+39,20,25))
    pygame.draw.rect(screen,GLASS,pygame.Rect(windowX+56,windowY+39,20,25))
    pygame.draw.rect(screen,GLASS,pygame.Rect(windowX+32.5,windowY+67,20,25))
    pygame.draw.rect(screen,GLASS,pygame.Rect(windowX+56,windowY+67,20,25))
    pygame.display.flip()

# Making a function to draw a balloon in a random place.
def drawBalloon():
    x = random.randint(200,600)
    y = random.randint(50,200)
    colour1 = random.randint(0,255)
    colour2 = random.randint(0,255)
    colour3 = random.randint(0,255)
    pygame.draw.ellipse(screen,(colour1,colour2,colour3),pygame.Rect(x-24,y-31,48,62))
    pygame.draw.ellipse(screen,WHITE,pygame.Rect(x-14,y-23,16,20))
    pygame.draw.line(screen,BLACK,(x,y+31),(houseX,houseY),1)
    pygame.draw.polygon(screen,(colour1,colour2,colour3),[[x,y+31],[x-5,y+36],[x+5,y+36]])
    pygame.display.flip()

# Making a function to draw a cloud in a random place.
def drawCloud():
    x = random.randint(40,700)
    y = random.randint(485,570)
    sizeFactor = round(random.uniform(1,1.6),1)
    pygame.draw.rect(screen,WHITE,pygame.Rect(x,y,150*sizeFactor,30*sizeFactor))
    pygame.draw.ellipse(screen,WHITE,pygame.Rect(x-30*sizeFactor,y-30*sizeFactor,60*sizeFactor,60*sizeFactor))
    pygame.draw.ellipse(screen,WHITE,pygame.Rect(x+20*sizeFactor,y-60*sizeFactor,80*sizeFactor,80*sizeFactor))
    pygame.draw.ellipse(screen,WHITE,pygame.Rect(x+95*sizeFactor,y-30*sizeFactor,60*sizeFactor,60*sizeFactor))
    pygame.draw.ellipse(screen,WHITE,pygame.Rect(x-25*sizeFactor,y,185*sizeFactor,45*sizeFactor))
    pygame.display.flip()

# Making a function to draw a bird in a random place.
def drawBird():
    x = random.randint(50,750)
    y = random.randint(30,100)
    # Body
    pygame.draw.ellipse(screen,RED,pygame.Rect(x-20,y-12.5,50,25))
    pygame.draw.ellipse(screen,LIGHT_RED,pygame.Rect(x-15,y,29,12))
    
    # Head
    pygame.draw.circle(screen,RED,(x-24,y-12),15)
    pygame.draw.circle(screen,BLACK,(x-27,y-15),5)
    pygame.draw.polygon(screen,DOORKNOB_YELLOW,[[x-50,y-12],[x-38,y-6],[x-38,y-18]])
    
    # Wing
    pygame.draw.polygon(screen,DARK_RED,[[x-4,y-11],[x+12,y-11],[x+15,y-30]])
    
    # Outline for the feet.
    pygame.draw.line(screen,BLACK,(x+4.5,y+10),(x+10,y+18),4)
    pygame.draw.line(screen,BLACK,(x+9.5,y+18),(x+10,y+25.5),4)
    pygame.draw.line(screen,BLACK,(x+9.5,y+18),(x+18,y+15.5),4)
    pygame.draw.line(screen,BLACK,(x+9.5,y+18),(x+17,y+22.5),4)

    pygame.draw.line(screen,BLACK,(x-5.5,y+10),(x,y+18),4)
    pygame.draw.line(screen,BLACK,(x-0.5,y+18),(x,y+25.5),4)
    pygame.draw.line(screen,BLACK,(x-0.5,y+18),(x+8,y+15.5),4)
    pygame.draw.line(screen,BLACK,(x-0.5,y+18),(x+7,y+22.5),4)
        
    # Feet
    pygame.draw.line(screen,MUSTARD,(x+5,y+10),(x+10,y+18),3)
    pygame.draw.line(screen,MUSTARD,(x+10,y+18),(x+10,y+25),3)
    pygame.draw.line(screen,MUSTARD,(x+10,y+18),(x+18,y+15),3)
    pygame.draw.line(screen,MUSTARD,(x+10,y+18),(x+17,y+22),3)
    
    pygame.draw.line(screen,MUSTARD,(x-5,y+10),(x,y+18),3)
    pygame.draw.line(screen,MUSTARD,(x,y+18),(x,y+25),3)
    pygame.draw.line(screen,MUSTARD,(x,y+18),(x+8,y+15),3)
    pygame.draw.line(screen,MUSTARD,(x,y+18),(x+7,y+22),3)    

# Making a function to draw the house.
def drawHouse(houseX,houseY):
    # Drawing the basic shape.
    pygame.draw.rect(screen,BRICK_RED,pygame.Rect(houseX-150,houseY+20,300,180))
    pygame.draw.polygon(screen,BROWN,[[houseX-180,houseY+20],[houseX,houseY-90],[houseX+180,houseY+20]])
    
    # Drawing the lines to make bricks.
    pygame.draw.line(screen,BRICK_LINE,(houseX-140,houseY+20),(houseX-140,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-120,houseY+20),(houseX-120,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-100,houseY+20),(houseX-100,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-80,houseY+20),(houseX-80,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-60,houseY+20),(houseX-60,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-40,houseY+20),(houseX-40,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-20,houseY+20),(houseX-20,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX,houseY+20),(houseX,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+20,houseY+20),(houseX+20,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+40,houseY+20),(houseX+40,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+60,houseY+20),(houseX+60,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+80,houseY+20),(houseX+80,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+100,houseY+20),(houseX+100,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+120,houseY+20),(houseX+120,houseY+200),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX+140,houseY+20),(houseX+140,houseY+200),2)
    
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+30),(houseX+150,houseY+30),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+50),(houseX+150,houseY+50),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+70),(houseX+150,houseY+70),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+90),(houseX+150,houseY+90),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+110),(houseX+150,houseY+110),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+130),(houseX+150,houseY+130),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+150),(houseX+150,houseY+150),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+170),(houseX+150,houseY+170),2)
    pygame.draw.line(screen,BRICK_LINE,(houseX-150,houseY+190),(houseX+150,houseY+190),2)
    
    # Drawing the door with details.
    pygame.draw.rect(screen,LIGHT_BROWN,pygame.Rect(houseX-30,houseY+115,60,85))
    pygame.draw.rect(screen,BEVEL_BROWN,pygame.Rect(houseX-20,houseY+125,15,30),2)
    pygame.draw.rect(screen,BEVEL_BROWN,pygame.Rect(houseX+5,houseY+125,15,30),2)
    pygame.draw.rect(screen,BEVEL_BROWN,pygame.Rect(houseX-20,houseY+165,15,30),2)
    pygame.draw.rect(screen,BEVEL_BROWN,pygame.Rect(houseX+5,houseY+165,15,30),2)
    pygame.draw.circle(screen,DOORKNOB_YELLOW,(houseX+22,houseY+160),5)
    
    # Drawing the windows.
    drawWindow(houseX-150,houseY)
    drawWindow(houseX-150,houseY+85)
    drawWindow(houseX-50,houseY)
    drawWindow(houseX+50,houseY)
    drawWindow(houseX+50,houseY+85)
    pygame.display.flip()

# Running the functions to draw everything.
# Drawing the background clouds.
# Layer 1
drawBackCloud(0,350,0.45,CLOUD1)
drawBackCloud(60,350,0.45,CLOUD1)
drawBackCloud(120,350,0.45,CLOUD1)
drawBackCloud(180,350,0.45,CLOUD1)
drawBackCloud(240,350,0.45,CLOUD1)
drawBackCloud(300,350,0.45,CLOUD1)
drawBackCloud(360,350,0.45,CLOUD1)
drawBackCloud(420,350,0.45,CLOUD1)
drawBackCloud(480,350,0.45,CLOUD1)
drawBackCloud(540,350,0.45,CLOUD1)
drawBackCloud(600,350,0.45,CLOUD1)
drawBackCloud(660,350,0.45,CLOUD1)
drawBackCloud(720,350,0.45,CLOUD1)
drawBackCloud(780,350,0.45,CLOUD1)

# Layer 2
drawBackCloud(0,388,0.7,CLOUD2)
drawBackCloud(85,388,0.7,CLOUD2)
drawBackCloud(170,388,0.7,CLOUD2)
drawBackCloud(255,388,0.7,CLOUD2)
drawBackCloud(340,388,0.7,CLOUD2)
drawBackCloud(425,388,0.7,CLOUD2)
drawBackCloud(510,388,0.7,CLOUD2)
drawBackCloud(595,388,0.7,CLOUD2)
drawBackCloud(680,388,0.7,CLOUD2)
drawBackCloud(765,388,0.7,CLOUD2)

# Layer 3
drawBackCloud(0,442,1.1,CLOUD3)
drawBackCloud(135,442,1.1,CLOUD3)
drawBackCloud(270,442,1.1,CLOUD3)
drawBackCloud(405,442,1.1,CLOUD3)
drawBackCloud(540,442,1.1,CLOUD3)
drawBackCloud(675,442,1.1,CLOUD3)
drawBackCloud(800,442,1.1,CLOUD3)

# Layer 4
drawBackCloud(0,525,1.9,CLOUD4)
drawBackCloud(250,525,1.9,CLOUD4)
drawBackCloud(500,525,1.9,CLOUD4)
drawBackCloud(750,525,1.9,CLOUD4)

# Drawing 50 balloons.
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()
drawBalloon()

# Drawing some birds.
drawBird()
drawBird()
drawBird()
drawBird()

# Drawing the basic house.
drawHouse(houseX,houseY)

# Drawing some clouds.
drawCloud()
drawCloud()
drawCloud()
drawCloud()
drawCloud()

pygame.time.wait(waitTime)

pygame.quit()