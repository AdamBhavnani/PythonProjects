#import libraries/modules
import RMv2_Func as RMv2
#PILlow library (python image library) for creating & loading images
import PIL
from PIL import Image
#colour picker for image colours
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

#get input for Random Walk algorithm parameters
mapLength = RMv2.inputValidInt("Map Length: ")
mapWidth = RMv2.inputValidInt("Map Width: ")
maxTunnels = RMv2.inputValidInt("Max Tunnel Count: ")
maxLength = RMv2.inputValidInt("Maximum Tunnel Length: ")
maxTreasure = RMv2.inputValidInt("Maximum Amount of Treasure: ")

#initialize mapGrid object: 2D array of "walls" (1 == u shall not pass)
mapGrid = RMv2.mapGrid(mapLength,mapWidth,1,maxTunnels,maxLength)

#get random starting position
currentRow, currentCol = RMv2.randomStart(mapGrid)

#set max # of tunnels
maxTunnels = mapGrid.maxTunnels
#previous direction = currently empty
lastDirection = []
#get next turn direction
nextDirection = RMv2.randomDirection()
#loop while maxTunnels > 0
while maxTunnels > 0:
    #"dig" a tunnel of random length in this direction
    randomLength = RMv2.random.randrange(1,mapGrid.maxLength,1)
    currentTunnelLength = 0
    while (currentTunnelLength < randomLength):
        nextRow = currentRow + nextDirection[0]
        nextCol = currentCol + nextDirection[1]     
        #if result of function is True, then this statement will execute - ***is this bad practice?
        #if moving in current direction would put you beyond bounds
        #decrement max # of tunnels, then end current tunnel by breaking loop
        if (RMv2.outBounds(nextRow,nextCol,mapGrid)):
            #ensure created tunnel is at least length 1 
            #before counting it as a tunnel against the tally of maxTunnels
            if(currentTunnelLength>0):
                maxTunnels -= 1
            break
        #else, clear a path by setting mapGrid at this index to 0, increment currentTunnelLength 
        else:
            if mapGrid.mapGrid[currentRow][currentCol] != 3:
                mapGrid.mapGrid[currentRow][currentCol] = 0 #*** in python, is it good practice to have public accessor functions?
            currentRow += nextDirection[0]
            currentCol += nextDirection[1]
            currentTunnelLength += 1
    
    #when above loop is complete, ensure created tunnel is at least length 1
    #before counting it as a tunnel against the tally of maxTunnels
    if(currentTunnelLength>0):
        maxTunnels-=1
        #also add a monster at the end of the tunnel on a 1
        monsterChance = RMv2.random.randint(1,20)
        if monsterChance <= 5:
            mapGrid.mapGrid[currentRow][currentCol] = 3
    #then set lastDirection and get a new nextDirection
    lastDirection = nextDirection
    nextDirection = RMv2.randomDirection()
  
    #do-while loop until 
    while True:
        #two conditions to ensure not overwriting or making two tunnels back-to-back (***confirm this)
        #if either condition is true, select a new direction
        #next direction is not opposite of previous i.e., not going back where you just were
        condition1 = (nextDirection[0] == -lastDirection[0] and nextDirection[1] == -lastDirection[1])
        #next direction is not same as previous i.e., not going in the same direction
        condition2 = (nextDirection[0] == lastDirection[0] and nextDirection[1] == lastDirection[1])
        if condition1 == True or condition2 == True:
            nextDirection = RMv2.randomDirection()
        else:
            break

#print grid
#RMv2.displayGrid(mapGrid)

#get input for map style parameters
wallColor = askcolor(color = (222,184,135), title="Color of Wall")
pathColor = askcolor(color = (0,191,235), title="Color of Path")
treasureColor = askcolor(color = (255,225,0), title="Color of Treasure")
monsterColor = askcolor(color = (255,0,0), title="Color of Monster")

#generate treasure at "end" of paths
#no other paths adjacent, i.e. at least 6 adjacent walls
#break if maxTreasure reached
for i in range(mapGrid.x):
    for j in range(mapGrid.y):
        if maxTreasure > 0:
            if RMv2.treasureCheck(i,j,mapGrid)==True and mapGrid.mapGrid[i][j] == 0:
                treasureChance = RMv2.random.randint(1,20)
                if treasureChance == 20:
                    mapGrid.mapGrid[i][j] = 2
                    maxTreasure -= 1
        else:
            break

#create an image of black pixels
img = Image.new('RGB',(mapGrid.x,mapGrid.y),wallColor[0])
for i in range(mapGrid.x):
    for j in range(mapGrid.y):
        if mapGrid.mapGrid[i][j] == 0:# *** is it possible to make a friend function where i only have to say mapGrid[i][j] to access array?
            img.putpixel((i,j),pathColor[0])
        if mapGrid.mapGrid[i][j] == 2:
            img.putpixel((i,j),treasureColor[0])
        if mapGrid.mapGrid[i][j] == 3:
            img.putpixel((i,j),monsterColor[0])
img.show()