# Name:          Farris Matar
# Date:          March , 2017
# Class:         ICS3U1-03
# Description:   Python programming test 2 part 2, drawing a picture.

# Starting up pygame.
import pygame
pygame.init()

# Getting the screen size from the user.
length = int(input("Enter the desired screen length: "))
width = int(input("Enter the desired screen width: "))

# Setting up some variables for the screen and colours.
SIZE = (length,width)
screen = pygame.display.set_mode(SIZE)
BACKGROUND = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
screen.fill(BACKGROUND)
pygame.display.flip()

# Drawing the circles.
pygame.draw.circle(screen,GREEN,(length//4,width//4),length//4)
pygame.draw.circle(screen,BLUE,(length//4*3,width//4),length//4)
pygame.draw.circle(screen,GREEN,(length//4*3,width//4*3),length//4)
pygame.draw.circle(screen,BLUE,(length//4,width//4*3),length//4)
pygame.display.flip()

# Drawing the rectangle.
pygame.draw.rect(screen,BLACK,pygame.Rect(length//4,width//4,length//2,width//2),5)
pygame.display.flip()

# Drawing the white lines.
pygame.draw.line(screen,WHITE,(0,width),(length//2,width//2),20)
pygame.draw.line(screen,WHITE,(length,width),(length//2,width//2),20)
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()