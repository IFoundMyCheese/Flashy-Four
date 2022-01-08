#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title: Flashy Four
# Programmer: Khaled Yaakoub Agha
# Date modified: 22 January 2020
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from tkinter import *
from time import *
from random import *
from gradientCreator import *
import winsound

root = Tk()
screen = Canvas(root, width=800, height=800, background="black")
screen.pack()

#--------------------------------------------------------------------------------- Initial Values -----------------------------------------------------------------------------------------------------#
def setInitialValues():
    global pattern, patternArray, dimColours, brightColours, xTile1, xTile2, yTile1, yTile2, xPattern1, xPattern2, yPattern1, yPattern2
    global score, lives, roundNumber, gameRunning, beepHertz, gamemode, instructions
    global numOfColors, patternPlay, proceedToNextRound, canClick, restartPattern, gameover
    global goBackToMenu, randomBackground, beepHertzArray, yCloud, xCloud, cloudSize, xStar, yStar, starSize
    
    pattern = [] # To store the pattern in
    patternArray = [] # To play the pattern
    brightColours = ["#FF0000", "#0000FF", "#00FF00", "#FFFF00"]
    dimColours = ["#550000", "#000055", "#005500", "#555500"]
    xTile1 = [150, 400, 150, 400]
    yTile1 = [150, 150, 400, 400]
    xTile2 = [400, 650, 400, 650]
    yTile2 = [400, 400, 650, 650]
    beepHertz = [554, 659, 494, 739] # For the tiles' pitches
    randomBackground = choice([1, 2]) # Generate one of two backgrounds randomly
    beepHertzArray = []
    xPattern1 = []
    xPattern2 = []
    yPattern1 = []
    yPattern2 = []
    xStar = []
    yStar = []
    xCloud = []
    yCloud = []
    cloudSize = []
    starSize = []
    numOfColors = 0
    score = 0
    lives = 3
    gamemode = ""
    roundNumber = 1
    gameRunning = False
    patternPlay = True
    proceedToNextRound = True
    canClick = False
    restartPattern = False
    goBackToMenu = False
    instructions = False
    gameover = False


#------------------------------------------------------------------------------------------- Background ------------------------------------------------------------------------------------------------#

# Draw the background
def drawBackground():
    global randomBackground
    
    # For the space background
    if randomBackground == 1:
        R1 = 6
        G1 = 38
        B1 = 80

        R2 = 0
        G2 = 0
        B2 = 0

        R3 = 180
        G3 = 0
        B3 = 255

        R4 = 233
        G4 = 0
        B4 = 255

        R5 = 0
        G5 = 237
        B5 = 255

        R6 = 0
        G6 = 184
        B6 = 255

        deltaR2 = (R4-R3)/255
        deltaG2 = (G4-G3)/255
        deltaB2 = (B4-B3)/255

        deltaR3 = (R6-R5)/255
        deltaG3 = (G6-G5)/255
        deltaB3 = (B6-B5)/255
        
        planRadius1 = 40
        planRadius2 = 50

    # For the dawn background  
    else:
        R1 = 00
        G1 = 37
        B1 = 127

        R2 = 243
        G2 = 144
        B2 = 100

        R3 = 253
        G3 = 197
        B3 = 0

        R4 = 253
        G4 = 32
        B4 = 0

        deltaR2 = (R4-R3)/255
        deltaG2 = (G4-G3)/255
        deltaB2 = (B4-B3)/255

        sunRadius = 20
        
    deltaR = (R2-R1)/255
    deltaG = (G2-G1)/255
    deltaB = (B2-B1)/255
    deltaY = 800/255
    y = 0
    
    for i in range(0, 256):
        r = round(R1 + i*deltaR)
        b = round(B1 + i*deltaB)
        g = round(G1 + i*deltaG)
        c = getPythonColor(r, g, b)
        screen.create_rectangle(0, y, 800, y + deltaY, fill = c, outline = c)
        y = y + deltaY
        
    if randomBackground == 2: # For the dawn background
        
        for i in range(100): # Draw the stars
            xStar.append(randint(0, 800))
            yStar.append(randint(0, 500))
            starSize.append(randint(3, 5))
            stars = screen.create_oval(xStar[i], yStar[i], xStar[i] + starSize[i], yStar[i] + starSize[i], fill = "white", outline = "white")
            
        for i in range(256): # Draw the sun with the gradient
            sun1 = round(R3 + i*deltaR2)
            sun2 = round(G3 + i*deltaG2)
            sun3 = round(B3 + i*deltaB2)
            s = getPythonColor(sun1, sun2, sun3)
            screen.create_oval(200-sunRadius, 750-sunRadius, 600+ sunRadius, 1150 + sunRadius, fill = s, outline = s)
            sunRadius -= 1
            
        # Draw the moon
        screen.create_oval(-110, -110, 140, 140, fill = "grey", outline = "grey")
        screen.create_oval(90, 90, 100, 100, fill = "grey40", outline = "grey40", width = 3)
        screen.create_oval(40, 40, 80, 80, fill = "grey40", outline = "grey40", width = 3)
        screen.create_oval(100, 10, 80, 30, fill = "grey40", outline = "grey40", width = 3)
        screen.create_oval(10, 100, 40, 130, fill = "grey40", outline = "grey40", width = 3)
        screen.create_oval(0, 5, 40, 45, fill = "grey40", outline = "grey40", width = 3)
        
    else: # For the space background
        
        for i in range(100): # Draw the stars
            xStar.append(randint(0, 800))
            yStar.append(randint(0, 800))
            starSize.append(randint(1, 3))
            screen.create_oval(xStar[i], yStar[i], xStar[i] + starSize[i], yStar[i] + starSize[i], fill = "white", outline = "white")
            
        for i in range(256): # Draw the planets with the gradients
            planet1 = round(R3 + i*deltaR2)
            planet2 = round(G3 + i*deltaG2)
            planet3 = round(B3 + i*deltaB2)
            planet4 = round(R5 + i*deltaR3)
            planet5 = round(G5 + i*deltaG3)
            planet6 = round(B5 + i*deltaB3)
            p = getPythonColor(planet1, planet2, planet3)
            p2 = getPythonColor(planet4, planet5, planet6)
            screen.create_oval(700-planRadius1, 0-planRadius1, 800+planRadius1, 100+planRadius1, fill = p, outline = p)
            screen.create_oval(0-planRadius2, 700-planRadius2, 100+planRadius2, 800+planRadius2, fill = p2, outline = p2)
            planRadius1 -= (40/256)
            planRadius2 -= (30/256)
            
        # Draw the ring around the planet
        screen.create_line(600, 0, 875, 100, fill = "orange", width = 12)

#--------------------------------------------------------------------------------------- Main Screen -----------------------------------------------------------------------------------------------------#
    
# Detect clicks     
def mouseClickHandler(event):
    global xMouse, yMouse, patternPlay, numOfColors, proceedToNextRound, roundNumber, patternArray, canClick, restartPattern
    global lives, score, gameover, gameRunning
    
    xMouse = event.x
    yMouse = event.y

    # If player is still on the intro screen
    if gameRunning == False:
        detectIntroScreenClick()
        
    # If player starts playing the game
    else:
        
        # Let you click only when the pattern is done playing
        if canClick == True:
            insideTile = tileClicked() # Call function tileClicked() to check if player is playing the pattern back correctly
            
            # If player plays pattern back correctly
            if insideTile == True:
                
                if len(patternArray) == 0: # If nothing is left in the array, then the player played the pattern back correctly
                    restorePattern() # Call function restorePattern() to restore the pattern, so it's played again in the next round
                    proceedToNextRound = True
                    patternPlay = True
                    canClick = False
                    restartPattern = False
                    roundNumber += 1
                    
                    if roundNumber % 6 == 0: # 500 extra points every 5 rounds (modulo 6 because round 1 is technically round 0)
                        score = score + 500
                        
                    else:
                        score = score + 100
                        
            # If player messes up
            elif insideTile == False:
                score = score - 50
                lives = lives - 1
                restartPattern = True
                patternPlay = True
                proceedToNextRound = False
                canClick = False
                
    # To return back to the main screen after losing
    if gameover == True:
        if 300 <= xMouse <= 500 and 575 <= yMouse <= 675:
            deleteGameOver() # Call deleteGameOver() to delete everything on the screen
            gameRunning = False
            gameover = False
            mainMenu() # Call mainMenu() to go back to the main screen
        
            

# Draw the intro screen
def drawIntroScreen():
    global box1, box2, box3, text1, text2, text3, text4, goBackToMenu
    
    box1 = screen.create_rectangle(100, 200, 700, 400, fill = "grey20", outline = "grey", width = 7)
    text1 = screen.create_text(300, 300, text = "Flashy", font = "fixedsys 50", fill = "red")
    text2 = screen.create_text(535, 300, text = "Four", font = "fixedsys 50", fill = "yellow")
    box2 = screen.create_rectangle(150, 500, 350, 600, fill = "grey20", outline = "grey", width = 7)
    box3 = screen.create_rectangle(450, 500, 650, 600, fill = "grey20", outline = "grey", width = 7)
    text3 = screen.create_text(250, 550, text = "Play", font = "fixedsys 20", fill = "green")
    text4 = screen.create_text(550, 550, text = "Instructions", font = "fixedsys 20", fill = "blue")



# Draw instruction screen
def instructionScreen():
    global box1, box2, box3, box4, box9, text1, text2, text3, text4, text5, text10, text11, text12, text13
    global text14, text15, text16, text17, text18, text19, text20, text21, text22, text23, text24

    # Delete main screen
    screen.delete(box1, box2, box3, text1, text2, text3, text4)
    
    box4 = screen.create_rectangle(300, 600, 500, 700, fill = "grey20", outline = "grey", width = 7)
    text5 = screen.create_text(400, 650, text = "Go Back", font = "fixedsys 20", fill = "green")
    box9 = screen.create_rectangle(100, 100, 700, 555, fill = "grey20", outline = "grey", width = 7)
    text10 = screen.create_text(400, 140, text = "You start with 3 lives and a score of 0. There are four tiles of", font = "fixedsys 10", fill = "white")
    text11 = screen.create_text(400, 165, text = "of different colors and pitches. A random pattern will be played", font = "fixedsys 10", fill = "white")
    text12 = screen.create_text(400, 190, text = "by lighting up its corresponding color, and your job is to play", font = "fixedsys 10", fill = "white")
    text13 = screen.create_text(400, 215, text = "it back correctly by clicking, depending on the gamemode you choose.", font = "fixedsys 10", fill = "white")
    text14 = screen.create_text(400, 240, text = "If you mess up, the pattern will be repeated, and you will lose a life", font = "fixedsys 10", fill = "white")
    text15 = screen.create_text(400, 265, text = "and 50 points. If you lose all 3 lives, it’s game over. If you progress", font = "fixedsys 10", fill = "white")
    text16 = screen.create_text(400, 290, text = "to the next round, you will gain 100 points. The number of colors in", font = "fixedsys 10", fill = "white")
    text17 = screen.create_text(400, 315, text = "the pattern increases by one each round. Every 5 rounds, you get", font = "fixedsys 10", fill = "white")
    text18 = screen.create_text(400, 340, text = "500 extra points to reward you for your amazing mental skills.", font = "fixedsys 10", fill = "white")
    text19 = screen.create_text(400, 365, text = "Your objective is to beat your highest score and most importantly:", font = "fixedsys 10", fill = "white")
    text20 = screen.create_text(400, 390, text = "to have fun!", font = "fixedsys 10", fill = "white")
    text21 = screen.create_text(400, 435, text = "Normal - The pattern is played, and you have to play it back correctly", font = "fixedsys 10", fill = "yellow")
    text22 = screen.create_text(265, 460, text = "in the SAME order.", font = "fixedsys 10", fill = "yellow")
    text23 = screen.create_text(400, 495, text = "Insane - The pattern is played, and you have to play it back correctly", font = "fixedsys 10", fill = "red")
    text24 = screen.create_text(265, 520, text = "in REVERSE order.", font = "fixedsys 10", fill = "red")


    
# Draw the play screen with the difficulties
def playScreen():
    global xMouse2, yMouse2, box2, box3, text3, text4, box5, box6, box7, box8, text6, text7, text8, text9, goBackToMenu

    # Delete main screen
    screen.delete(box2, box3, text3, text4)
    
    box5 = screen.create_rectangle(200, 450, 600, 550, fill = "grey20", outline = "grey", width = 7)
    box6 = screen.create_rectangle(50, 600, 250, 700, fill = "grey20", outline = "grey", width = 7)
    box7 = screen.create_rectangle(550, 600, 750, 700, fill = "grey20", outline = "grey", width = 7)
    box8 = screen.create_rectangle(300, 600, 500, 700, fill = "grey20", outline = "grey", width = 7)
    text6 = screen.create_text(400, 500, text = "Choose Difficulty", font = "fixedsys 20", fill = "blue")
    text7 = screen.create_text(150, 650, text = "Normal", font = "fixedsys 20", fill = "Green")
    text8 = screen.create_text(650, 650, text = "Insane", font = "fixedsys 20", fill = "Green")
    text9 = screen.create_text(400, 650, text = "Go Back", font = "fixedsys 20", fill = "Green")


# Detect clicks on main screen
def detectIntroScreenClick():
    global goBackToMenu, instructions, gameRunning, gamemode

    if goBackToMenu == False:
        if instructions == False:
            if 450 <= xMouse <= 650 and 500 <= yMouse <= 600: 
                instructionScreen() # Call instructionScreen() to draw the instruction screen
                goBackToMenu = True
                instructions = True
            elif 150 <= xMouse <= 350 and 500 <= yMouse <= 600:
                playScreen() # Call playScreen() to draw the play screen with the difficulties
                goBackToMenu = True
                instructions = False
                
    else:    
         if instructions == True:
            if 300 <= xMouse <= 500 and 600 <= yMouse <= 700:
                deleteInstructionScreen() # Delete everything on the instruction screen
                drawIntroScreen() # Go back to the main screen
                goBackToMenu = False
                instructions = False
         else:
            if 50 <= xMouse <= 250 and 600 <= yMouse <= 700:
                gamemode = "normal" # Set gamemode to normal
                gameRunning = True
                deletePlayScreen() # Delete everything on the play screen
                runGame() # Call runGame() to start the game
            elif 550 <= xMouse <= 750 and 600 <= yMouse <= 700:
                gamemode = "insane" # Set gamemode to insane
                gameRunning = True
                deletePlayScreen()  # Delete everything on the play screen
                runGame() # Call runGame() to start the game
            elif 300 <= xMouse <= 500 and 600 <= yMouse <= 700:
                deletePlayScreen() # Delete everything on the play screen
                drawIntroScreen() # Go back to the main screen
                goBackToMenu = False
                instructions = False

                
#------------------------------------------------------------------------------------------- Game Functions ------------------------------------------------------------------------------------------------#    

# Draw the four tiles
def drawTiles():
    global xTile1, xTile2, yTile1, yTile2, dimColours
    
    for i in range(4):
        screen.create_rectangle(xTile1[i], yTile1[i], xTile2[i], yTile2[i], fill = dimColours[i], width = 10)

# Generate a random pattern
def checkPattern():
    global pattern, patternArray, numOfColors, brightColours, xTile1, xTile2, xPattern1, xPattern2, yTile1, yTile2
    global yPattern1, yPattern2
    
    for i in range(1):
        pattern.append(choice(["#FF0000", "#0000FF", "#00FF00", "#FFFF00"]))
        patternArray.append(pattern[-1])
        for x in range(len(brightColours)):
            if patternArray[-1] == brightColours[x]:
                xPattern1.append(xTile1[x])
                xPattern2.append(xTile2[x])
                yPattern1.append(yTile1[x])
                yPattern2.append(yTile2[x])
                beepHertzArray.append(beepHertz[x])
        numOfColors += 1 # To keep track of the number of colors in the pattern
            

# Play the pattern
def playPattern():
    global xPattern1, xPattern2, yPattern1, yPattern2, patternPlay, beepHertzArray
    
    if patternPlay == True:
        
        for i in range(len(patternArray)):
            p = screen.create_rectangle(xPattern1[i], yPattern1[i], xPattern2[i], yPattern2[i], fill = patternArray[i])
            screen.update()
            winsound.Beep(beepHertzArray[i], 100)
            screen.delete(p) 
            screen.update()
            sleep(0.5) # Sleep for a flashing effect
            
        patternPlay = False
    
        
        
# Detect which tile player clicked and whether it's right or not      
def tileClicked():
    global xMouse, yMouse, xTile1, xTile2, yTile1, yTile2, patternArray
    global beepHertz, patternPlay, gamemode
    
    for i in range(0,4): # Go through all of the tile coordinates to find which one was clicked
        if xTile1[i] <= xMouse <= xTile2[i] and yTile1[i] <= yMouse <= yTile2[i]:
            click = screen.create_rectangle(xTile1[i], yTile1[i], xTile2[i], yTile2[i], fill = brightColours[i]) # Draw the tile clicked
            screen.update()
            winsound.Beep(beepHertz[i], 300) # Generate the corresponding pitch
            screen.delete(click)
            
            if len(patternArray) != 0:
                if gamemode == "insane": # If gamemode is insane
                    if brightColours[i] == patternArray[-1]: # Detect if the tile clicked by the player is the last item in the pattern array
                        patternArray.pop(-1) # Remove the last item in the array
                        return True
                
                    else: # If pattern played back is wrong
                        for i in range(len(patternArray)):
                            patternArray.remove(patternArray[0]) # Remove everything from the array
                        return False
                    
                elif gamemode == "normal": # If gamemode is normal
                    if brightColours[i] == patternArray[0]: # Detect if the tile clicked by the player is the first item in the pattern array
                        patternArray.pop(0) # Remove the first item in the array
                        return True
                
                    else: # If pattern played back is wrong
                        for i in range(len(patternArray)):
                            patternArray.remove(patternArray[0]) # Remove everything from the array
                        return False


# Restore pattern after one round is over
def restorePattern():
    global pattern, patternArray
    
    for i in range(len(pattern)):
        patternArray.append(pattern[i])


#-------------------------------------------------------------------------------------------- Game Statistics --------------------------------------------------------------------------------------------------# 

# Display the number of lives left
def displayLives():
    global lives, life
    
    if lives == 3:
        life = screen.create_text(220, 100, text = "Lives: " + str(lives), font = "fixedsys 30", fill = "#fefefe")
    if lives == 2:
        life = screen.create_text(220, 100, text = "Lives: " + str(lives), font = "fixedsys 30", fill = "#fefe00")
    if lives == 1:
        life = screen.create_text(220, 100, text = "Lives: " + str(lives), font = "fixedsys 30", fill = "#fe0000")
    if lives == 0:
        life = screen.create_text(220, 100, text = "\u2620", font = "fixedsys 30", fill = "#ff0000")

# Display the score
def displayScore():
    global score, sc
    
    sc = screen.create_text(600, 100, text = "Score: " + str(score), font = "fixedsys 30", fill = "#fefefe")

# Display the number of the round
def displayRoundNumber():
    global roundNumber, rd
    
    rd = screen.create_text(400, 50, text = "Round: " + str(roundNumber), font = "fixedsys 30", fill = "#FF5100")


#------------------------------------------------------------------------------------------ Delete Functions ----------------------------------------------------------------------------------------------------#

# Delete everything on the play screen
def deletePlayScreen():
    global box1, box5, box6, box7, box8, text1, text2, text6, text7, text8, text9
    
    screen.delete(box1, box5, box6, box7, box8, text1, text2, text6, text7, text8, text9)

# Delete everything on the instruction screen
def deleteInstructionScreen():
    global box1, box4, box9, text1, text2, text5, text10, text11, text12, text13, text14, text15, text16, text17, text18, text19, text20, text21, text22, text23, text24
    
    screen.delete(box1, box4, box9, text1, text2, text5, text10, text11, text12, text13, text14, text15, text16, text17, text18, text19, text20, text21, text22, text23, text24)

# Delete everything on the screen when player hits "Play Again"
def deleteGameOver():
    screen.delete("all")



#---------------------------------------------------------------------------------------------- Game Over ----------------------------------------------------------------------------------------------------# 
        
# For when player loses
def gameOver():
    global score, overRec, overText, gameover
    
    for i in range(60): # Animation for black circle
        circle = screen.create_oval(400-(i*10), 400-(i*10), 400 + (i*10), 400 + (i*10), fill = "black")
        go = screen.create_text(400, 350, text = "GAME OVER", font = "fixedsys 70", fill = "#FF0000")
        
        if i >= 40: # Show after a certain period of time
            sc = screen.create_text(400, 475, text = "Your score is: " + str(score), font = "fixedsys 30", fill = "#FF0000")
        screen.update()
        sleep(0.01)
        
        if i < 59: # So it doesn't delete after animation is over
            screen.delete(circle, go)
            
    gameover = True
    # Draw the play again option after animation is over
    overRec = screen.create_rectangle(300, 575, 500, 675, fill = "grey20", outline = "grey", width = 7)
    overText = screen.create_text(400, 625, text = "Play Again", font = "fixedsys 20", fill = "green")
    

#------------------------------------------------------------------------------------------- Main Functions ----------------------------------------------------------------------------------------------------# 
            
# Run the game     
def runGame():
    global numOfColors, patternPlay, roundNumber, proceedToNextRound, canClick, restartPattern, lives, life, sc, rd
    
    # Draw the tiles and game statstics
    drawTiles()
    displayLives()
    displayScore()
    displayRoundNumber()
    while lives != 0:
        while patternPlay == True and canClick == False:
            
            # Only when player proceeds to the next round
            if restartPattern == False:
                while numOfColors < (2 + roundNumber): # One more color every round
                    checkPattern()
                    
            # If player messes up 
            else:
                restorePattern()
                proceedToNextRound = False
                restartPattern = False
            playPattern()
        canClick = True # Become False when player messes up or proceeds to the next round, which repeats the loop
        screen.update()
        sleep(0.2)
        screen.delete(life, sc, rd)
        displayLives() # Update number of lives
        displayScore() # Update score
        displayRoundNumber() # Update round number
        
    gameOver() # When player runs out of lives
    

# Main screen
def mainMenu():
    setInitialValues()
    drawBackground()
    drawIntroScreen()


root.after( 1000, mainMenu)
screen.bind( "<Button-1>", mouseClickHandler )
screen.focus_set()
root.mainloop()