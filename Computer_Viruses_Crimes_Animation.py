# Name:          Farris Matar
# Date:          April 27, 2017
# Description:   Creating an informational program
#                about computer viruses and crimes.

# Starting up Pygame.
import pygame
pygame.init()

# Setting up some variables for the screen and colours.
SIZE = (800,600)
screen = pygame.display.set_mode(SIZE)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GRAY = (122,122,122)
STEEL = (181,189,204)
LIGHT_STEEL = (225,231,242)
LIGHT_GREEN = (150,255,150)
LIGHT_RED = (255,100,100)
LIGHT_BLUE = (100,100,255)
LIGHT_GRAY = (210,210,210)
COMPUTER_GRAY = (214,214,214)
DOT_GREEN = (42,206,30)
MOUSE_RED = (173,12,12)
DARK_GREEN = (3,150,5)
DARK_RED = (175,0,0)
DARK_GRAY = (50,50,50)

# Making variables for various loops.
scene = 1
sizeFactor = 1
dotX1 = 755
dotMove1 = -2
dotX2 = 45
dotMove2 = 2
dotY1 = 30
dotYMove1 = 2
dotY2 = 570
dotYMove2 = -2
bombX1 = 160
bombMove1 = -1
bombX2 = 560
bombMove2 = 1
fishX1 = 201
fishMove1 = -1
fishX2 = 609
fishMove2 = 1

# Making variables for the fonts, images and sounds.
# Fonts
titleFont = pygame.font.SysFont("Courier New",47)
buttonFont = pygame.font.SysFont("OCR A Extended",45)
backButtonFont = pygame.font.SysFont("OCR A Extended",27)
shutDownFont = pygame.font.SysFont("Times New Roman",75)
normalTextFont1 = pygame.font.SysFont("Times New Roman",19)
normalTextFont2 = pygame.font.SysFont("Times New Roman",20)

# Sounds
laserSound = pygame.mixer.Sound("fire.wav")
powerupSound = pygame.mixer.Sound("PowerUp.wav")
powerdownSound = pygame.mixer.Sound("PowerDown.wav")
liftSound = pygame.mixer.Sound("Lift_Sound.wav")

# Images
virusSymbol = pygame.image.load("ComputerVirus.png")
handcuffs = pygame.image.load("Handcuffs.png")
exitDoor = pygame.image.load("ExitDoor.png")
smallExitDoor = pygame.image.load("SmallExitDoor.png")
bomb = pygame.image.load("Bomb.png")

# Making constants for the buttons.
# Computer Virus button.
VIRUS_BUTTON_X = 200
VIRUS_BUTTON_Y = 225
VIRUS_BUTTON_WIDTH = 400
VIRUS_BUTTON_HEIGHT = 75
virusColor = (0,0,0)

# Computer Crime button.
CRIME_BUTTON_X = 200
CRIME_BUTTON_Y = 325
CRIME_BUTTON_WIDTH = 400
CRIME_BUTTON_HEIGHT = 75
crimeColor = (0,0,0)

# Quit button.
QUIT_BUTTON_X = 200
QUIT_BUTTON_Y = 425
QUIT_BUTTON_WIDTH = 400
QUIT_BUTTON_HEIGHT = 75
quitColor = (0,0,0)

# Back button.
BACK_BUTTON_X = 15
BACK_BUTTON_Y = 15
BACK_BUTTON_WIDTH = 75
BACK_BUTTON_HEIGHT = 40
backColor = (0,0,0)

# Drawing rectangles for indicating the collisions.
quitIndicator = pygame.Rect(QUIT_BUTTON_X, QUIT_BUTTON_Y, QUIT_BUTTON_WIDTH, QUIT_BUTTON_HEIGHT)
crimeIndicator = pygame.Rect(CRIME_BUTTON_X, CRIME_BUTTON_Y, CRIME_BUTTON_WIDTH, CRIME_BUTTON_HEIGHT)
virusIndicator = pygame.Rect(VIRUS_BUTTON_X, VIRUS_BUTTON_Y, VIRUS_BUTTON_WIDTH, VIRUS_BUTTON_HEIGHT)
backIndicator = pygame.Rect(BACK_BUTTON_X, BACK_BUTTON_Y, BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT)

# Powering up (sound).
powerupSound.play()

# Making a function to draw the main screen.
def drawScene1(screen,mx,my):
    # Drawing the background.
    screen.fill(BLACK)
    pygame.display.set_caption("The Dark Side of Computers!")
    pygame.draw.line(screen,DARK_GREEN,(0,300),(100,300),5)
    pygame.draw.line(screen,DARK_GREEN,(98,300),(150,200),5)
    pygame.draw.line(screen,DARK_GREEN,(150,200),(262.5,450),5)
    pygame.draw.line(screen,DARK_GREEN,(262.5,450),(400,100),5)
    pygame.draw.line(screen,DARK_GREEN,(400,100),(500,400),5)
    pygame.draw.line(screen,DARK_GREEN,(500,400),(550,200),5)
    pygame.draw.line(screen,DARK_GREEN,(550,200),(600,300),5)
    pygame.draw.line(screen,DARK_GREEN,(600,300),(800,300),5)
    pygame.draw.rect(screen,COMPUTER_GRAY,pygame.Rect(0,0,800,600),25)
    
    # Drawing circles to move across the screen.
    pygame.draw.circle(screen,DOT_GREEN,(dotX1,150),10)
    pygame.draw.circle(screen,DOT_GREEN,(dotX2,450),10)
    pygame.draw.circle(screen,DOT_GREEN,(100,dotY1),10)
    pygame.draw.circle(screen,DOT_GREEN,(700,dotY2),10)
    
    # Checking if the mouse is in each box and highlighting it if so.
    # Virus button
    if mx > VIRUS_BUTTON_X and my > VIRUS_BUTTON_Y and mx < VIRUS_BUTTON_X + VIRUS_BUTTON_WIDTH and my < VIRUS_BUTTON_Y + VIRUS_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_BLUE,virusIndicator,0)
        
        # Drawing a play/pause button for the mouse.
        pygame.draw.rect(screen,RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.polygon(screen,WHITE,[[mx-10,my+9],[mx-10,my-9],[mx+10,my]])
        
        # Drawing a virus next to the button.
        screen.blit(virusSymbol,pygame.Rect(VIRUS_BUTTON_X-75, VIRUS_BUTTON_Y+10, 20, 15))
        screen.blit(virusSymbol,pygame.Rect(VIRUS_BUTTON_X+VIRUS_BUTTON_WIDTH+10, VIRUS_BUTTON_Y+10, 65, 55))
        virusColor = (255,255,255)
    else:
        pygame.draw.rect(screen,BLUE,virusIndicator,0)
        virusColor = (0,0,0)
        
    # Crime button
    if mx > CRIME_BUTTON_X and my > CRIME_BUTTON_Y and mx < CRIME_BUTTON_X + CRIME_BUTTON_WIDTH and my < CRIME_BUTTON_Y + CRIME_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_GREEN,crimeIndicator,0)
        
        # Drawing handcuffs next to the button.
        screen.blit(handcuffs,pygame.Rect(CRIME_BUTTON_X-85, CRIME_BUTTON_Y+10, 75, 55))
        screen.blit(handcuffs,pygame.Rect(CRIME_BUTTON_X+CRIME_BUTTON_WIDTH+10, CRIME_BUTTON_Y+10, 75, 55))
        crimeColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GREEN,crimeIndicator,0)
        crimeColor = (0,0,0)
    # Quit Button
    if mx > QUIT_BUTTON_X and my > QUIT_BUTTON_Y and mx < QUIT_BUTTON_X + QUIT_BUTTON_WIDTH and my < QUIT_BUTTON_Y + QUIT_BUTTON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,quitIndicator,0)
        
        # Drawing a play/pause button for the mouse.
        pygame.draw.rect(screen,RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.polygon(screen,WHITE,[[mx-10,my+9],[mx-10,my-9],[mx+10,my]])
        
        # Drawing exit doors next to the button.
        screen.blit(exitDoor,pygame.Rect(QUIT_BUTTON_X-80,QUIT_BUTTON_Y+10,70,60))
        screen.blit(exitDoor,pygame.Rect(QUIT_BUTTON_X+QUIT_BUTTON_WIDTH+10,QUIT_BUTTON_Y+10,70,60))
        quitColor = (255,255,255)
    else:
        pygame.draw.rect(screen,RED,quitIndicator,0)
        quitColor = (0,0,0)
        
    # Writing out the title and labes for the buttons.
    # Title
    title = titleFont.render("THE DARK SIDE OF COMPUTERS",1,WHITE)
    screen.blit(title,pygame.Rect(30,50,700,100))
    
    # Virus button
    virusButton = buttonFont.render("Computer Virus",1,virusColor)
    screen.blit(virusButton,pygame.Rect(VIRUS_BUTTON_X+10, VIRUS_BUTTON_Y+10, VIRUS_BUTTON_WIDTH-10, VIRUS_BUTTON_HEIGHT-10))
    
    # Crime button
    crimeButton = buttonFont.render("Computer Crime",1,crimeColor)
    screen.blit(crimeButton,pygame.Rect(CRIME_BUTTON_X+10, CRIME_BUTTON_Y+10, CRIME_BUTTON_WIDTH-10, CRIME_BUTTON_HEIGHT-10))
    
    # Quit button
    quitButton = buttonFont.render("Quit",1,quitColor)
    screen.blit(quitButton,pygame.Rect(QUIT_BUTTON_X+140, QUIT_BUTTON_Y+10, QUIT_BUTTON_WIDTH-140, QUIT_BUTTON_HEIGHT-10))
    
    # Making the default mouse invisible.
    pygame.mouse.set_visible(0)
    
    # Drawing a pause/play button for a mouse, based on whether or not it is on the button.
    if mx > QUIT_BUTTON_X and my > QUIT_BUTTON_Y and mx < QUIT_BUTTON_X + QUIT_BUTTON_WIDTH and my < QUIT_BUTTON_Y + QUIT_BUTTON_HEIGHT or mx > CRIME_BUTTON_X and my > CRIME_BUTTON_Y and mx < CRIME_BUTTON_X + CRIME_BUTTON_WIDTH and my < CRIME_BUTTON_Y + CRIME_BUTTON_HEIGHT or mx > VIRUS_BUTTON_X and my > VIRUS_BUTTON_Y and mx < VIRUS_BUTTON_X + VIRUS_BUTTON_WIDTH and my < VIRUS_BUTTON_Y + VIRUS_BUTTON_HEIGHT:
        pygame.draw.rect(screen,RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.polygon(screen,WHITE,[[mx-10,my+9],[mx-10,my-9],[mx+10,my]])
    else:
        pygame.draw.rect(screen,MOUSE_RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.rect(screen,WHITE,pygame.Rect(mx-8,my-10,5,20))
        pygame.draw.rect(screen,WHITE,pygame.Rect(mx+3,my-10,5,20))        

# Making a function to draw virus scene.
def drawScene2(screen,mx,my):
    # Drawing the background.
    screen.fill(BLACK)
    pygame.draw.line(screen,DARK_GREEN,(0,300),(100,300),5)
    pygame.draw.line(screen,DARK_GREEN,(98,300),(150,200),5)
    pygame.draw.line(screen,DARK_GREEN,(150,200),(262.5,450),5)
    pygame.draw.line(screen,DARK_GREEN,(262.5,450),(400,100),5)
    pygame.draw.line(screen,DARK_GREEN,(400,100),(500,400),5)
    pygame.draw.line(screen,DARK_GREEN,(500,400),(550,200),5)
    pygame.draw.line(screen,DARK_GREEN,(550,200),(600,300),5)
    pygame.draw.line(screen,DARK_GREEN,(600,300),(800,300),5)
    pygame.draw.rect(screen,COMPUTER_GRAY,pygame.Rect(0,0,800,600),25)
    pygame.display.set_caption("Computer Viruses!")
    
    # Checking if the mouse is on the back button.
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:    
        pygame.draw.rect(screen,LIGHT_GRAY,backIndicator,0)
        pygame.draw.rect(screen,RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.polygon(screen,WHITE,[[mx-10,my+9],[mx-10,my-9],[mx+10,my]])
        
        # Drawing an exit door next to the button.
        screen.blit(smallExitDoor,pygame.Rect(BACK_BUTTON_X+BACK_BUTTON_WIDTH+5,BACK_BUTTON_Y+5,40,35))
        backColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GRAY,backIndicator,0)
        backColor = (0,0,0)
    
    # Drawing the bombs to move.
    screen.blit(bomb,pygame.Rect(bombX1,30,90,90))
    screen.blit(bomb,pygame.Rect(bombX2,30,90,90))
    
    # Writing the title.
    virusTitle = titleFont.render("Logic Bombs!",1,WHITE)
    screen.blit(virusTitle,pygame.Rect(240,50,700,100))
    
    # Writing out the text.
    virusText1 = normalTextFont1.render("A logic bomb is a set of code inserted into a larger program, in which once certain",1,WHITE)
    virusText2 = normalTextFont1.render("conditions are met, the logic bomb goes off and runs code to do a certain undesirable",1,WHITE)
    virusText3 = normalTextFont1.render("action. For instance, someone might install a logic bomb into their employer's computer",1,WHITE)
    virusText4 = normalTextFont1.render("so that, in the event that they are fired, the bomb will then delete various files.",1,WHITE)
    virusText5 = normalTextFont1.render("A famous example of the destructive power of a logic bomb occurred in 1982. The problem",1,WHITE)
    virusText6 = normalTextFont1.render("started when the CIA got a tip about plans for the KGB to steal complex regulation software",1,WHITE)
    virusText7 = normalTextFont1.render("from a Canadian firm. The CIA decided to plant a logic bomb in the program to switch the code",1,WHITE)
    virusText8 = normalTextFont1.render("after running a certain number of times. The software was stolen and then used to regulate",1,WHITE)
    virusText9 = normalTextFont1.render("the Trans-Siberian-Pipeline. For a few months, it worked perfectly fine, until eventually",1,WHITE)
    virusText10 = normalTextFont1.render("the bomb went off and was set to build pressure in the pipelines in various areas. What was",1,WHITE)
    virusText11 = normalTextFont1.render("supposed to happen was a few leaks in various areas in the pipeline. Instead, it built up so",1,WHITE)
    virusText12 = normalTextFont1.render("much that it created a massively devastating explosion one-fifth the power of an atomic bomb.",1,WHITE)
    
    screen.blit(virusText1,pygame.Rect(30,140,700,400))
    screen.blit(virusText2,pygame.Rect(30,175,700,400))
    screen.blit(virusText3,pygame.Rect(30,210,700,400))
    screen.blit(virusText4,pygame.Rect(30,245,700,400))
    screen.blit(virusText5,pygame.Rect(30,280,700,400))
    screen.blit(virusText6,pygame.Rect(30,315,700,400))
    screen.blit(virusText7,pygame.Rect(30,350,700,400))
    screen.blit(virusText8,pygame.Rect(30,385,700,400))
    screen.blit(virusText9,pygame.Rect(30,420,700,400))
    screen.blit(virusText10,pygame.Rect(30,455,700,400))
    screen.blit(virusText11,pygame.Rect(30,490,700,400))
    screen.blit(virusText12,pygame.Rect(30,525,700,400))
    
    # Writing out the label for the back button.
    backButton = backButtonFont.render("BACK",1,backColor)
    screen.blit(backButton,pygame.Rect(BACK_BUTTON_X+5, BACK_BUTTON_Y+5, BACK_BUTTON_WIDTH-5, BACK_BUTTON_HEIGHT-5))
    
    # Drawing a pause/play button for a mouse, based on whether or not it is on the button.
    pygame.mouse.set_visible(0)
        
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:
        pygame.draw.rect(screen,RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.polygon(screen,WHITE,[[mx-10,my+9],[mx-10,my-9],[mx+10,my]])        
    else:
        pygame.draw.rect(screen,MOUSE_RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.rect(screen,WHITE,pygame.Rect(mx-8,my-10,5,20))
        pygame.draw.rect(screen,WHITE,pygame.Rect(mx+3,my-10,5,20))
    
    pygame.display.flip()

# Making two functions to draw a fish looking either direction.
def drawLeftFish(fishX):
    pygame.draw.ellipse(screen,BLUE,pygame.Rect(fishX-30,60,60,40))
    pygame.draw.polygon(screen,BLUE,[[fishX+30,80],[fishX+60,60],[fishX+60,100]])
    pygame.draw.circle(screen,WHITE,(fishX-15,80),8)

def drawRightFish(fishX):
    pygame.draw.ellipse(screen,BLUE,pygame.Rect(fishX-30,60,60,40))
    pygame.draw.polygon(screen,BLUE,[[fishX-30,80],[fishX-60,60],[fishX-60,100]])
    pygame.draw.circle(screen,WHITE,(fishX+15,80),8)

# Making a function to draw crime scene.
def drawScene3(screen,mx,my):
    screen.fill(BLACK)
    pygame.draw.line(screen,DARK_GREEN,(0,300),(100,300),5)
    pygame.draw.line(screen,DARK_GREEN,(98,300),(150,200),5)
    pygame.draw.line(screen,DARK_GREEN,(150,200),(262.5,450),5)
    pygame.draw.line(screen,DARK_GREEN,(262.5,450),(400,100),5)
    pygame.draw.line(screen,DARK_GREEN,(400,100),(500,400),5)
    pygame.draw.line(screen,DARK_GREEN,(500,400),(550,200),5)
    pygame.draw.line(screen,DARK_GREEN,(550,200),(600,300),5)
    pygame.draw.line(screen,DARK_GREEN,(600,300),(800,300),5)
    pygame.draw.rect(screen,COMPUTER_GRAY,pygame.Rect(0,0,800,600),25)
    pygame.display.set_caption("Computer Crimes!")
    
    # Making if statements to know which fish to draw; if the fish is supposed to be moving right (based on the fishMove variable),
    # it will draw the right fish. If it's supposed to be moving left, it will draw the left fish.
    if fishMove1 == 1:
        drawRightFish(fishX1)
    if fishMove1 == -1:
        drawLeftFish(fishX1)
    if fishMove2 == 1:
        drawRightFish(fishX2)
    if fishMove2 == -1:
        drawLeftFish(fishX2)
    
    # Checking if the mouse is on the back button.
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:    
        pygame.draw.rect(screen,LIGHT_GRAY,backIndicator,0)
        
        # Drawing an exit door next to the button.
        screen.blit(smallExitDoor,pygame.Rect(BACK_BUTTON_X+BACK_BUTTON_WIDTH+5,BACK_BUTTON_Y+5,40,35))
        backColor = (255,255,255)
    else:
        pygame.draw.rect(screen,GRAY,backIndicator,0)
        backColor = (0,0,0)
    
    # Writing out the text.
    crimeText1 = normalTextFont2.render("Phishing is an unfortunately common computer crime in which personal information,",1,WHITE)
    crimeText2 = normalTextFont2.render("such as a person's identities, passwords, addresses and/or banking information,",1,WHITE)
    crimeText3 = normalTextFont2.render("are unknowingly stolen from the user via seemingly trustworthy electronic communication." ,1,WHITE)
    crimeText4 = normalTextFont2.render("There are 3 types of phishing: the first is spear phishing, in which specific",1,WHITE)
    crimeText5 = normalTextFont2.render("individuals are targetted using personal information the criminal has gathered to",1,WHITE)
    crimeText6 = normalTextFont2.render("appear authentic. The second type is clone phishing, in which an originally authentic",1,WHITE)
    crimeText7 = normalTextFont2.render("email with an attachment is sent again with a different attachment to steal the user's",1,WHITE)
    crimeText8 = normalTextFont2.render("information. The email contains the same address, making it difficult to tell if it is",1,WHITE)
    crimeText9 = normalTextFont2.render("authentic. The third type is whaling. Whailing involves targetting high-profile people,",1,WHITE)
    crimeText10 = normalTextFont2.render("such as CEO's or upper managers. It requires more skill to effectively disguise the bait,",1,WHITE)
    crimeText11 = normalTextFont2.render("which can vary from a company-wide problem email, a customer concern, a legal issue",1,WHITE)
    crimeText12 = normalTextFont2.render("and other forms. Whaling is usually the most damaging and dangerous type of phishing.",1,WHITE)
    
    screen.blit(crimeText1,pygame.Rect(30,120,700,400))
    screen.blit(crimeText2,pygame.Rect(30,155,700,400))
    screen.blit(crimeText3,pygame.Rect(30,190,700,400))
    screen.blit(crimeText4,pygame.Rect(30,225,700,400))
    screen.blit(crimeText5,pygame.Rect(30,260,700,400))
    screen.blit(crimeText6,pygame.Rect(30,295,700,400))
    screen.blit(crimeText7,pygame.Rect(30,330,700,400))
    screen.blit(crimeText8,pygame.Rect(30,365,700,400))
    screen.blit(crimeText9,pygame.Rect(30,400,700,400))
    screen.blit(crimeText10,pygame.Rect(30,435,700,400))
    screen.blit(crimeText11,pygame.Rect(30,470,700,400))
    screen.blit(crimeText12,pygame.Rect(30,505,700,400))
    
    # Writing the title.
    crimeTitle = titleFont.render("Phishing!",1,WHITE)
    screen.blit(crimeTitle,pygame.Rect(280,40,700,100))
    
    # Writing out the label for the back button.
    backButton = backButtonFont.render("BACK",1,backColor)
    screen.blit(backButton,pygame.Rect(BACK_BUTTON_X+5, BACK_BUTTON_Y+5, BACK_BUTTON_WIDTH-5, BACK_BUTTON_HEIGHT-5))

    # Drawing a pause/play button for a mouse, based on whether or not it is on the button.
    pygame.mouse.set_visible(0)
    
    if mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:
        pygame.draw.rect(screen,RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.polygon(screen,WHITE,[[mx-10,my+9],[mx-10,my-9],[mx+10,my]])        
    else:
        pygame.draw.rect(screen,MOUSE_RED,pygame.Rect(mx-20,my-15,40,30))
        pygame.draw.rect(screen,WHITE,pygame.Rect(mx-8,my-10,5,20))
        pygame.draw.rect(screen,WHITE,pygame.Rect(mx+3,my-10,5,20))    
    
    pygame.display.flip()

# Making a function to draw the error triangle.
def errorTriangleEffect(sizeFactor):
    screen.fill(LIGHT_GRAY)
    pygame.draw.polygon(screen,BLACK,[[400,300-(25*sizeFactor)],[400-(32*sizeFactor),300+(25*sizeFactor)],[400+(32*sizeFactor),300+(25*sizeFactor)]])
    pygame.draw.polygon(screen,DARK_RED,[[400,300-(25*sizeFactor)],[400-(32*sizeFactor),300+(25*sizeFactor)],[400+(32*sizeFactor),300+(25*sizeFactor)]],int(sizeFactor))
    pygame.draw.rect(screen,WHITE,pygame.Rect(400-(3*sizeFactor),300-(12*sizeFactor),6*sizeFactor,20*sizeFactor))
    pygame.draw.rect(screen,WHITE,pygame.Rect(400-(3*sizeFactor),300+(12*sizeFactor),6*sizeFactor,6*sizeFactor))
    
    pygame.display.flip()

# Making a function to draw the power button.
def powerButtonAnimation(sizeFactor):
    # Drawing the background
    screen.fill(BLACK)
    pygame.display.set_caption("Shutting down...")
    pygame.draw.line(screen,DARK_GREEN,(0,300),(100,300),5)
    pygame.draw.line(screen,DARK_GREEN,(98,300),(150,200),5)
    pygame.draw.line(screen,DARK_GREEN,(150,200),(262.5,450),5)
    pygame.draw.line(screen,DARK_GREEN,(262.5,450),(400,100),5)
    pygame.draw.line(screen,DARK_GREEN,(400,100),(500,400),5)
    pygame.draw.line(screen,DARK_GREEN,(500,400),(550,200),5)
    pygame.draw.line(screen,DARK_GREEN,(550,200),(600,300),5)
    pygame.draw.line(screen,DARK_GREEN,(600,300),(800,300),5)
    
    # Drawing the power button
    pygame.draw.circle(screen,DARK_RED,(400,300),int(10*sizeFactor), int(sizeFactor))
    pygame.draw.circle(screen,DARK_RED,(400,300),int(10*sizeFactor), int(sizeFactor))
    pygame.draw.circle(screen,DARK_RED,(401,300),int(10*sizeFactor), int(sizeFactor))
    pygame.draw.arc(screen,BLACK,[400-(10*sizeFactor),300-(10*sizeFactor),20*sizeFactor,20*sizeFactor],0.9,2.3,int(sizeFactor))
    pygame.draw.arc(screen,BLACK,[400-(10*sizeFactor),(300-(10*sizeFactor))+2,20*sizeFactor,20*sizeFactor],0.9,2.3,int(sizeFactor))
    pygame.draw.arc(screen,BLACK,[400-(10*sizeFactor),(300-(10*sizeFactor))-1,20*sizeFactor,20*sizeFactor],0.9,2.3,int(sizeFactor))
    pygame.draw.line(screen,DARK_RED,(400,300-(3*sizeFactor)),(400,300-(12*sizeFactor)),int(1*sizeFactor))
    pygame.draw.rect(screen,COMPUTER_GRAY,pygame.Rect(0,0,800,600),25)    
    
    pygame.display.flip()

# Making a function to draw handcuffs.
def handcuffsAnimation(sizeFactor):
    screen.fill(DARK_GRAY)
    pygame.draw.circle(screen,STEEL,(int(400-(15*sizeFactor)),300),int(10*sizeFactor),int(2*sizeFactor))
    pygame.draw.circle(screen,STEEL,(int((400-(15*sizeFactor))-1),300),int(10*sizeFactor),int(2*sizeFactor))
    pygame.draw.circle(screen,STEEL,(int((400-(15*sizeFactor))+1),300),int(10*sizeFactor),int(2*sizeFactor))
    pygame.draw.circle(screen,STEEL,(int(400+(15*sizeFactor)),300),int(10*sizeFactor),int(2*sizeFactor))
    pygame.draw.circle(screen,STEEL,(int((400+(15*sizeFactor))+1),300),int(10*sizeFactor),int(2*sizeFactor))
    pygame.draw.circle(screen,STEEL,(int((400+(15*sizeFactor))-1),300),int(10*sizeFactor),int(2*sizeFactor))
    
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect(400-(0.1*sizeFactor),300,9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect((400-(0.1*sizeFactor))-1,300,9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect((400-(0.1*sizeFactor))+1,300,9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect(400-(4.5*sizeFactor),(300+1.5*sizeFactor),9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect((400-(4.5*sizeFactor))+1,(300+1.5*sizeFactor),9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect((400-(4.5*sizeFactor))-1,(300+1.5*sizeFactor),9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect(400-(8.9*sizeFactor),300,9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect((400-(8.9*sizeFactor))-1,300,9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    pygame.draw.ellipse(screen,LIGHT_STEEL,pygame.Rect((400-(8.9*sizeFactor))+1,300,9*sizeFactor,5*sizeFactor),int(0.8*sizeFactor))
    
    pygame.display.flip()    

# Making a function to clear the screen when going back to the menu.
def clearScreen(sizeFactor):
    pygame.draw.circle(screen,WHITE,(400,300),sizeFactor)
    pygame.display.flip()

# Making a function to know which scene to draw.
def drawScene():
    if scene == 1:
        drawScene1(screen,mx,my)
    elif scene == 2:
        drawScene2(screen,mx,my)
    elif scene == 3:
        drawScene3(screen,mx,my)

# Making a function to get the coordinates of the mouse and checking if it's pressed.
def getMouse():
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()[0]
    return (mx, my, mb)

# Making a loop to constantly get the mouse position, draw the scenes and run the events..
running = True

while running:
    # Making a loop to check for any events.
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            mb = evnt.button
    
    # Using the functions.
    mx, my, mb = getMouse()
    drawScene()
    pygame.display.flip()
    
    # Making the green dots on the menu move.
    if scene == 1:
        dotX1 += dotMove1
        dotX2 += dotMove2
        dotY1 += dotYMove1
        dotY2 += dotYMove2
        
        if dotX1 < 25:
            dotMove1 = 2
        if dotX2 < 25:
            dotMove2 = 2
        if dotX1 > 775:
            dotMove1 = -2
        if dotX2 > 775:
            dotMove2 = -2
        
        if dotY1 < 25:
            dotYMove1 = 2
        if dotY2 < 25:
            dotYMove2 = 2
        if dotY1 > 575:
            dotYMove1 = -2
        if dotY2 > 575:
            dotYMove2 = -2
    
    # Making the bombs move in the computer virus scene.
    if scene == 2:
        bombX1 += bombMove1
        bombX2 += bombMove2
        
        if bombX1 < 35:
            bombMove1 = 1
        if bombX1 > 165:
            bombMove1 = -1
        if bombX2 > 690:
            bombMove2 = -1
        if bombX2 < 560:
            bombMove2 = 1
    
    # Making the fish move in the computer crime scene.
    if scene == 3:
        fishX1 += fishMove1
        fishX2 += fishMove2
        
        if fishX1 < 70:
            fishMove1 = 1
        if fishX1 > 220:
            fishMove1 = -1
        if fishX2 < 585:
            fishMove2 = 1
        if fishX2 > 735:
            fishMove2 = -1
    
    # Making the buttons to do what they're supposed to by checking if the user clicked inside of them in the appropriate scene.
    # Computer Virus button.
    if mb == 1 and mx > VIRUS_BUTTON_X and my > VIRUS_BUTTON_Y and mx < VIRUS_BUTTON_X + VIRUS_BUTTON_WIDTH and my < VIRUS_BUTTON_Y + VIRUS_BUTTON_HEIGHT and scene == 1:
        laserSound.play()
        # Using a loop to create the error triangle animation.
        sizeFactor = 1
        for count in range(160):
            errorTriangleEffect(sizeFactor)
            pygame.time.wait(10)
            sizeFactor += 0.1
        scene = 2
    # Computer Crime button.
    if mb == 1 and mx > CRIME_BUTTON_X and my > CRIME_BUTTON_Y and mx < CRIME_BUTTON_X + CRIME_BUTTON_WIDTH and my < CRIME_BUTTON_Y + CRIME_BUTTON_HEIGHT and scene == 1:
        laserSound.play()
        # Using a loop to create the handcuffs animation.
        sizeFactor = 1
        for count in range(160):
            handcuffsAnimation(sizeFactor)
            pygame.time.wait(10)
            sizeFactor += 0.1
        scene = 3
    # Quit button.
    if mb == 1 and mx > QUIT_BUTTON_X and my > QUIT_BUTTON_Y and mx < QUIT_BUTTON_X + QUIT_BUTTON_WIDTH and my < QUIT_BUTTON_Y + QUIT_BUTTON_HEIGHT and scene == 1:
        powerdownSound.play()
        # Using a loop to create the power button animation.
        sizeFactor = 35
        for count in range(160):
            powerButtonAnimation(sizeFactor)
            pygame.time.wait(10)
            sizeFactor -= 0.2
        running = False
    # Back button.
    if mb == 1 and mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT and scene == 2 or mb == 1 and mx > BACK_BUTTON_X and my > BACK_BUTTON_Y and mx < BACK_BUTTON_X + BACK_BUTTON_WIDTH and my < BACK_BUTTON_Y + BACK_BUTTON_HEIGHT and scene == 3:
        # Using an animation to clear the screen.
        sizeFactor = 1
        liftSound.play()
        for count in range(500):
            clearScreen(sizeFactor)
            pygame.time.wait(5)
            sizeFactor += 1
        for count in range(500):
            drawScene1(screen,mx,my)
            clearScreen(sizeFactor)
            pygame.time.wait(5)
            sizeFactor -= 1
        scene = 1

pygame.quit()
