from tkinter import*
from time import*
from random import*
from math import*

root = Tk()
screen = Canvas(root, width=1000, height=800, background="#FFD27F")
screen.pack()

#Creating Images


def importImages():
    global CPU, Evil, Electron, intro, inst

    #PLAYER
    CPU = PhotoImage(file="Images\\CPU.gif")

    #ENEMIES
    Evil = PhotoImage(file="Images\\Enemy.gif")

    #ATTACK
    Electron = PhotoImage(file= "Images\\Electron.gif")

    #INTRODUCTION SCREEN
    intro = PhotoImage(file = "Images\\Intro Page.gif")

    #INSTRUCTION SCREENS
    instructions1 = PhotoImage(file = "Images\\instructions9.gif")
    instructions2 = PhotoImage(file = "Images\\instructions8.gif")
    instructions3 = PhotoImage(file = "Images\\instructions7.gif")
    instructions4 = PhotoImage(file = "Images\\instructions6.gif")
    instructions5 = PhotoImage(file = "Images\\instructions5.gif")
    instructions6 = PhotoImage(file = "Images\\instructions4.gif")
    instructions7 = PhotoImage(file = "Images\\instructions3.gif")
    instructions8 = PhotoImage(file = "Images\\instructions2.gif")
    instructions9 = PhotoImage(file = "Images\\instructions1.gif")
    instructions10 = PhotoImage(file = "Images\\instructions.gif")
    inst = [instructions1, instructions2, instructions3, instructions4, instructions5, instructions6, instructions7, instructions8, instructions9, instructions10]   

def initialValues():
    global playerX, playerY, xSpeed, ySpeed, playerHealth, sped
    global roundNum, exp, roundStart, freeze, click
    global numEnemies, healthMin, healthMax, enemies, enemiesX, enemiesY, enemiesSpeedX, enemiesSpeedY, enemiesAlive, enemiesHealth, enemiesHealthNum, drawEnemiesHealth, enemiesDamage
    global attackSpeedX,attackSpeedY, attack, attackX, attackY, attackPower, ASPEED
    global attackPowerCost, healthCost, playerSpeedCost, attackSpeedCost
    global AP, H, MS, AS, stats, drawExp

    #PLAYER VALUES
    playerX = 400
    playerY = 400
    xSpeed = 0
    ySpeed = 0
    playerHealth = 30
    sped = 3

    #ENEMIE VALUES
    numEnemies = 1
    healthMax = 2
    enemies = []
    enemiesX = []
    enemiesY = []
    enemiesSpeedX = []
    enemiesSpeedY = []
    enemiesAlive = []
    enemiesHealth = []
    enemiesHealthNum = []
    drawEnemiesHealth = []
    enemiesDamage = 1

    
    roundNum = 0
    exp = 0
    roundStart = False
    freeze = False
    click = True

    #ATTACK VALUES
    attackSpeedX = []
    attackSpeedY = []
    attack = []
    attackX = []
    attackY = []
    attackPower = 0.5
    ASPEED = 40

    #UPGRADE COST VALUE
    attackPowerCost = 10
    healthCost = 10
    playerSpeedCost = 10
    attackSpeedCost = 10

    #DRAWING STATS
    AP = ""
    H = ""
    MS = ""
    AS = ""
    stats = ""
    drawExp = ""
       
def createBackground():

    #DRAWING BACKGROUND
    screen.create_rectangle(-10,-10,1010,810, fill = "#F2C571")
    screen.create_rectangle(0,0, 50,800, fill = "#F2C571", outline = "#F2C571", width = 5 )
    screen.create_rectangle(750,0, 800,800, fill = "#F2C571", outline = "#F2C571", width = 5)
    screen.create_rectangle(50,0, 750,50, fill = "#F2C571", outline = "#F2C571", width = 5)
    screen.create_rectangle(50,750, 750,800, fill = "#F2C571", outline = "#F2C571", width = 5)
    screen.create_rectangle(50,50,750,750, fill = "#FFD27F", outline = "#F7C362", width = 5)
    screen.create_rectangle(50,50, 750,70, fill = "#F7C362", outline = "#F7C362", width = 5)
    screen.create_rectangle(53,70, 747,76, fill = "#EAB146", outline = "#EAB146")
    screen.create_rectangle(350,650, 450,750, fill = "red")
    
def keyDownHandler(event):
    
    global xSpeed, ySpeed
    global playerHealth, attackPower, sped, ASPEED, exp
    global freeze, click

    #PLAYER MOVEMENT
    if event.keysym == "Up":
        ySpeed = -sped
        
    elif event.keysym == "Down":
        ySpeed = sped
        
    if event.keysym == "Right":
        xSpeed = sped
        
    elif event.keysym == "Left":
        xSpeed = -sped

    #ATTACK DIRECTION
    if event.keysym == "W" or  event.keysym == "w":
        createAttack("UP")
    elif event.keysym == "A" or  event.keysym == "a":
        createAttack("LEFT")
    elif event.keysym == "S" or  event.keysym == "s":
        createAttack("DOWN")
    elif event.keysym == "D" or  event.keysym == "d":
        createAttack("RIGHT")

    #UPGRADE BUTTONS

    #HEALTH UPGRADE
    if event.keysym == "1":
        if exp >= healthCost:
            playerHealth = playerHealth + 20
            exp = exp - healthCost

    #ATTACK POWER UPGRADE
    elif event.keysym == "2":
        if exp >= attackPowerCost:
            attackPower = attackPower + 1
            exp = exp - attackPowerCost

    #PLAYER MOVEMENT SPEED UPGRADE
    elif event.keysym == "3":
        if exp >= playerSpeedCost:
            sped = sped + 1
            exp = exp - playerSpeedCost

    #ATTACK SPEED UPGRADE
    elif event.keysym == "4":
        if exp >= attackSpeedCost:
            ASPEED = ASPEED + 2
            exp = exp - attackSpeedCost

    if event.keysym == "G":
        playerHealth = 999
        sped = 50
        ASPEED = 90
        attackPower = 50

    #QUIT
    if event.keysym == "q":
        click = True
        freeze = True
        introScreen()
    

def keyUpHandler(event):
    global xSpeed, ySpeed

    #STOP MOVEMENT
    xSpeed = 0
    ySpeed = 0
    
def mouseClick(event):
    global start, click
    xMouse = event.x
    yMouse = event.y
##    if click == True:
    
    #PLAY BUTTON
    if xMouse in range(250,760) and yMouse in range(45, 230):
        root.after(0,runGame())
        click = False

    #INSTRUCTION BUTTON
    if xMouse in range(250,760) and yMouse in range(290, 455):
        instructions()
        click = False

    #QUIT GAME BUTTON
    if xMouse in range(250,760) and yMouse in range(500, 660):
        root.destroy()
        click = False
            
def drawPlayer():
    global player, health, playerHealth

    #DRAWING PLAYER
    player = screen.create_image(playerX, playerY, image=CPU)
    
def updatePlayer():
    
    global playerX, playerY, xSpeed, ySpeed

    #WALL DETECTION
    if playerX - 34 <= 56:
        playerX = 56 + 34
             
    if playerX + 34 >= 744:
        playerX = 744 - 34

    if playerY - 34 <= 75:
        playerY = 75 + 34

    if playerY + 34 >= 744:
        playerY = 744 - 34

    #RESPAWN LOCATION DETECTION
    if 390 >= playerX +34 >= 350 and 620 <= playerY <= 790:
        playerX = 350 - 34

    if 450 >= playerX  - 34 >= 410 and 630 <= playerY <= 770:
        playerX = 450 + 34

    if 699 >= playerY  + 34 >= 650 and 330 <= playerX <= 470:
        playerY = 650 - 34        

    #UPDATE PLAYER LOCATION 
    playerX = playerX + xSpeed
    playerY = playerY + ySpeed
    
def createEnemies():
    global enemies, roundStart, numEnemies, enemiesX, enemiesY, healthMax, enemiesSpeedX, enemiesSpeedY, enemiesHealth, enemiesHealthNum, drawEnemiesHealth, roundNum
    if roundStart == True:

        #INCREASE ROUND NUM
        roundNum = roundNum + 1

        #INCREASE NUMBER OF ENEMIES PER ROUND
        newEnemies = choice([1,1,1,1,2])
        
        for i in range(newEnemies):
            #CREATING NEW ENEMIE STARTING VALUES
            enemies.append("")
            drawEnemiesHealth.append("")
            enemiesX.append(randint(100,700))
            enemiesY.append(randint(130,550))
            enemiesSpeedX.append(randint(1,3))
            enemiesSpeedY.append(randint(1,3))
            enemiesAlive.append(True)
            enemiesHealth.append(0)
            enemiesHealthNum.append(0)
            
        for i in range(len(enemies)):
            enemiesAlive[i] = True
            enemiesHealth[i] = randint(1,healthMax)
            enemiesHealthNum[i] = enemiesHealth[i]

        #STOP CREATING NEW ENEMIES
        roundStart = False

def drawEnemies():
    
    global enemies, numEnemies, enemeiesHealthNum, drawEnemiesHealth
    for f in range(len(enemies)):

        #CHECKING IF ALL ENEMIES ARE ALIVE
        if enemiesAlive[f] == True:

            #DRAWING ENEMIES
            enemies[f] = screen.create_image(enemiesX[f], enemiesY[f], image = Evil)

            #DRAWING ENEMY HEALTH
            drawEnemiesHealth[f] = screen.create_text(enemiesX[f], enemiesY[f] - 50, text = str(enemiesHealthNum[f]), font = "ariel 20")
            
def updateEnemies():
    global enemiesX, enemiesY, enemiesSpeedX, enemiesSpeedY, enemeiesHealthNum

    for w in range(len(enemies)):

        #CHECK ENEMIES ALIVE
        if enemiesAlive[w] == True:

            #BOUNCE ENEMIES OFF WALLS
            if enemiesX[w] >= 715:
                enemiesSpeedX[w] = enemiesSpeedX[w] *-1
            elif enemiesX[w] <= 90:
                
                enemiesSpeedX[w] = enemiesSpeedX[w] *-1 

            if enemiesY[w] >= 715:
                enemiesSpeedY[w] = enemiesSpeedY[w] *-1
                
            elif enemiesY[w] <= 120:
                enemiesSpeedY[w] = enemiesSpeedY[w] *-1

            #BOUNCE ENEMIES OFF RESPAWN LOCATION
            if 390 >= enemiesX[w] +34 >= 350 and 620 <= enemiesY[w] <= 790:
                enemiesX[w] = 350 - 34
                enemiesSpeedX[w] = enemiesSpeedX[w] *-1

            if 450 >= enemiesX[w]  - 34 >= 410 and 630 <= enemiesY[w] <= 770:
                enemiesX[w] = 450 + 34
                enemiesSpeedX[w] = enemiesSpeedX[w] *-1

            if 699 >= enemiesY[w]  + 34 >= 650 and 330 <= enemiesX[w] <= 470:
                enemiesY[w] = 650 - 34
                enemiesSpeedY[w] = enemiesSpeedY[w] *-1

    for m in range(len(enemies)):
        if enemiesAlive[m] == True:

            #UPDATING ENEMIES LOCATION
            enemiesX[m] = enemiesX[m] + enemiesSpeedX[m]
            enemiesY[m] = enemiesY[m] + enemiesSpeedY[m]
            enemiesHealthNum[m] = enemiesHealth[m]

def deleteEnemies():
    for d in range(len(enemies)):

        #DELETING ENEMY AND HEALTH
        screen.delete(enemies[d], drawEnemiesHealth[d])

def removeEnemies():
    global attack, attackX, attackY, attackSpeedX, attackSpeedY, enemiesHealth, exp
    global enemies, enemiesX, enemiesY, enemiesSpeedX, enemiesSpeedY

    #FOR ALL ATTACK
    for e in range(len(attack)):

        #FOR ALL ENEMIES
        for f in range(len(enemies)):

            #CHECK IF ENEMIES ARE ALIVE
            if enemiesAlive[f]== True:

                #CHECK DISTANCE BETWEEN ATTACK AND ENEMY
                dist = sqrt((attackX[e]-enemiesX[f])**2 + (attackY[e] - enemiesY[f])**2)

                #IF DISTANCE IS LESS THEN 40 
                if dist < 40:

                    #LESS HEALTH
                    enemiesHealth[f] = enemiesHealth[f] - attackPower
                    if enemiesHealth[f] <= 0:

                        #GAIN EXP WHEN HEALTH == 0
                        exp =exp + choice([1,1,1,1,1,1,1,2,2,2,2,2,3])
                        enemiesAlive[f] = False

def createAttack(Direction):
    global attackSpeedX, attackSpeedY, attack, attackX, attackY

    #CREATE ONLY ONE ATTACK
    if len(attack) <1:

        #DO NOT CREATE ATTACK IF PLAYER IS IN RESPAWN LOCATION
        if playerX in range(350,450) and playerY in range(650,750):
            noAttack = 0
            
        else:

            #CSET ATTACK SPEED
            if Direction == "UP":
                attackSpeedY.append(-ASPEED)
                attackSpeedX.append(0)
            elif Direction == "DOWN":
                attackSpeedY.append(ASPEED)
                attackSpeedX.append(0)
            elif Direction == "RIGHT":
                attackSpeedX.append(ASPEED)
                attackSpeedY.append(0)
            elif Direction == "LEFT":
                attackSpeedX.append(-ASPEED)
                attackSpeedY.append(0)

            #START ATTACK AT PLAYER LOCATION
            attackX.append(playerX)
            attackY.append(playerY)

            #CREATE ATTACK
            attack.append("")
    
def drawAttack():
    
    global attack, attackX, attackY, attackSpeedX, attackSpeedY 
    for f in range(len(attack)):
        
        #DRAW ATTACK
        attack[f] = screen.create_image(attackX[f], attackY[f], image = Electron)
        
def updateAttack():
    
    global attackX, attackY, attack, attackSpeedX, attackSpeedY
    for f in range(len(attack)):

        #UPDATE ATTACK LOCATION
        attackX[f] = attackX[f] + attackSpeedX[f]
        attackY[f] = attackY[f] + attackSpeedY[f]
        
def deleteAttack():
    
    global attack, attackX, attackY, attackSpeedX, attackSpeedY
    
    for f in range(len(attack)):

        #DELETE ATTACK
        screen.delete(attack[f])

        #DELETE ATTACK IF IT HITS WALL
        if attackX[f] < 60 or attackX[f] > 740 or attackY[f] < 80 or attackY[f] > 745:
            attack.remove(attack[f])
            attackX.remove(attackX[f])
            attackY.remove(attackY[f])
            attackSpeedX.remove(attackSpeedX[f])
            attackSpeedY.remove(attackSpeedY[f])
            
        elif 400 >= attackX[f] +34 >= 380 and 620 <= attackY[f] <= 790:
            attack.remove(attack[f])
            attackX.remove(attackX[f])
            attackY.remove(attackY[f])
            attackSpeedX.remove(attackSpeedX[f])
            attackSpeedY.remove(attackSpeedY[f])
            
        elif 450 >= attackX[f] - 34 >= 410 and 630 <= attackY[f] <= 770:
            attack.remove(attack[f])
            attackX.remove(attackX[f])
            attackY.remove(attackY[f])
            attackSpeedX.remove(attackSpeedX[f])
            attackSpeedY.remove(attackSpeedY[f])
            
        elif 699 >= attackY[f]  + 34 >= 650 and 330 <= attackX[f] <= 470:
            attack.remove(attack[f])
            attackX.remove(attackX[f])
            attackY.remove(attackY[f])
            attackSpeedX.remove(attackSpeedX[f])
            attackSpeedY.remove(attackSpeedY[f])

def lossHealth():
    
    global playerHealth, playerX, playerY

    #IF THERE ARE ENEMIES
    if len(enemies) > 0: 
        for f in range(len(enemies)):

            #IF ENEMY ARE ALIVE
            if enemiesAlive[f] == True:

                #CHECK DISTANCE BETWEEN PLAYER AND ENEMY
                dist = sqrt((playerX-enemiesX[f])**2 + (playerY - enemiesY[f])**2)

                #IF DISTANCE IS LESS THEN 80
                if dist < 80:

                    #LOWER PLAYER HEALTH IF ENEMY MAKES CONTACT
                    playerHealth = playerHealth - enemiesDamage

                    #TELEPORT PLAYER TO OPPOSITE CORNER IF ENEMY MAKE CONTACT
                    if playerX < 400 and playerY < 400:
                        playerX = 700
                        playerY = 700
                        
                    elif playerX < 400 and playerY > 400:
                        playerX = 700
                        playerY = 100
                        
                    elif playerX > 400 and playerY < 400:
                        playerX = 100
                        playerY = 700
                        
                    elif playerX > 400 and playerY > 400:
                        playerX = 100
                        playerY = 100

def drawRound():
    
    global numRound

    #DRAW ROUND NUMBER
    numRound = screen.create_text(400, 40, text = "Round " +str(roundNum), font = "ariel 40", fill = "brown")

def newRound():
    
    global roundStart, roundNum, healthMax, enemiesDamage, playerX, playerY

    #IF ALL ENEMIES ARE CRASHED
    if True not in enemiesAlive:

        #START NEXT ROUND        
        roundStart = True

        #INCREASE ENMEY HEALTH
        healthMax = healthMax + randint(0,1)

        #INCREASE ENEMY DAMAGE
        enemiesDamage = enemiesDamage + randint(0,1)

        #PUT PLAYER BACK TO RESPAWN LOCATION
        playerX = 400
        playerY = 700
        
def crash():
    
    global freeze, playerHealth, click

    #CHECK PLAYER HEALTH
    if playerHealth <= 0:

        playerHealth = 0

        #DRAW LOSE SCREEN
        screen.create_text(400,400, text = "YOU LOSE", font = "ariel 100", fill = "red")
        screen.update()
        sleep(2)
        click = True

        #FREEZE GAME
        freeze = True

        #GO BACK TO INTRODUCTION SCREEN
        introScreen()

def drawStore():
    
    global option1text, option2text, option3text, option4text, option1Cost, option2Cost, option3Cost, option4Cost

    #DRAW UPGRADE TEXT
    option1text = screen.create_text(900,30, text = "HEALTH = 1", font = "ariel 17", fill = "green")
    
    option2text = screen.create_text(900,130,  text = "ATTACK = 2", font = "ariel 17", fill = "red")
    
    option3text = screen.create_text(900,230, text = "PLAYER SPEED = 3", font = "ariel 15", fill = "blue")
    
    option4text = screen.create_text(900,330, text = "ATTACK SPEED = 4", font = "ariel 15", fill = "purple")
    
    #DRAW COST OF UPGRADES
    option1Cost = screen.create_text(900,70, text = "Cost = " + str(healthCost), font = "ariel 17", fill = "green")
    
    option2Cost = screen.create_text(900,170, text = "Cost = " + str(attackPowerCost), font = "ariel 17", fill = "red")
    
    option3Cost = screen.create_text(900,270, text = "Cost = " + str(playerSpeedCost), font = "ariel 17", fill = "blue")
    
    option4Cost = screen.create_text(900,370, text = "Cost = " + str(attackSpeedCost), font = "ariel 17", fill = "purple")

def drawStats():
    
    global AP, H, MS, AS, stats, drawExp

    #DRAW STATS
    H = screen.create_text(900, 530, text = "Player Health = " + str(playerHealth), font = "ariel 17", fill = "green")
    
    AP = screen.create_text(900, 580, text = "Attack Power = " + str(attackPower), font = "ariel 17", fill = "red")
   
    MS = screen.create_text(900, 630, text = "Player Speed = " + str(sped), font = "ariel 17", fill = "blue")
    
    AS = screen.create_text(900, 680, text = "Attack Speed = " + str(ASPEED), font = "ariel 17", fill = "purple")

    stats = screen.create_text(900, 480, text = "Stats", font = "ariel 30", fill = "black")

    #DRAW UPGRADES
    drawExp = screen.create_text(700,40,text = "Exp = " + str(exp), font = "ariel 25", fill = "black")
    
def deleteStore():

    #DELETE STATS
    screen.delete( AP, H, MS, AS, stats, drawExp)

def introScreen():
    
    global drawIntro, click

    #CREATE INTRODUCTION SCREEN
    click = True
    drawIntro = screen.create_image(500,400, image = intro)

def deleteIntroScreen():
    
    global drawIntro

    #DELETE INTRODUCTION SCREEN
    screen.delete(drawIntro)

def instructions():
    
    global click

    #CREATE INSTRUCTIONS 
    for i in range(len(inst)):
        current = screen.create_image(500,400, image = inst[i])
        screen.update()
        sleep(1)
        screen.delete(current)
    sleep(3)
    click  = True

    #GO BACK TO INTRODUCTION SCREEN
    introScreen()

#BIND KEYS AND MOUSE
screen.bind("<Button 1>", mouseClick)
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)


importImages()
introScreen()

#START GAME 
def runGame():
    initialValues()
    createBackground()
    drawStore()
    deleteStore()
    while freeze == False:    
        createEnemies()
        drawPlayer()
        drawEnemies()
        drawAttack()
        drawRound()
        updatePlayer()
        updateEnemies()
        updateAttack()
        screen.update()
        sleep(0.03)
        deleteEnemies()
        deleteAttack()
        removeEnemies()
        lossHealth()
        screen.delete(player, numRound, drawExp)
        newRound()
        deleteStore()
        drawStats()
        crash()
screen.pack()
screen.focus_set()
root.mainloop()

