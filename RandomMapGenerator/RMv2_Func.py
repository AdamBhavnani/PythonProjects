import random #random number library

############################
### Function Definitions ###
############################

### inputValidInt ###
#prompts the user for inputString
#returns a valid integer
def inputValidInt(inputString):
    #get user input
    testNum = input(inputString)
    #initiate do-while loop, iterating until valid input obtained
    validInput = False
    while validInput == False:
        try:
            testNum = int(round(float(testNum))) #***is there a better way to do this?
            if testNum <= 2:
                print("This value is too small.")
                testNum = input("Try again. " + inputString)
            else:    
                validInput = True
        except ValueError:
            print("This is not a number!")
            testNum = input("Try again. " + inputString)
        except TypeError:
            print("This is not a number!")
            testNum = input("Try again. " + inputString)
    return testNum
###

### initializeGrid ###
#takes dimensions
#returns 2D array filled with specified values
def initializeGrid(x,y,n):
    mapGrid = []
    for i in range(x):
        mapGrid.append([])#list == row
        for j in range(y):
            mapGrid[i].append(n)#list element == column
    return mapGrid
###

### randomStart ###
#takes grid
#returns index of start position
def randomStart(mapGrid):
    randRow = random.randrange(0,(mapGrid.x-1))
    randCol = random.randrange(0,(mapGrid.y-1))
    return randRow, randCol
###

### randomDirection ###
#returns random direction
def randomDirection():
    #directions = up, down, left, right
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    return random.choice(directions)
###

### outBounds ###
#takes a [row,col] index and checks if it is beyond bounds [len,wid] of grid
#returns True if beyond bounds, else False
def outBounds(row,col,mapGrid):
    if (row < 0) or (row > (mapGrid.x-1)) or (col < 0) or (col > (mapGrid.y-1)):
        return True
    else:
        return False
###

### treasureCheck ###
#takes current [row,col] and mapGrid object, then checks adjacent directions for validity
#returns true if 7 adjacent cells are walls, else returns false or if current cell is bounds
def treasureCheck(row,col,mapGrid):
    #directions =   up    down  left right    NW    NE     SW      SE
    directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,1],[1,1],[-1,-1],[1,-1]]
    if (row == 0) or (row == (mapGrid.x-1)) or (col == 0) or (col == (mapGrid.y-1)):
        return False
    else:
        #if the cell is a path, check adjacent directions
        if mapGrid.mapGrid[row][col]==0:
            wallCount = 0
            #check each direction
            for k in range(len(directions)):
                x = row+directions[k][0]
                y = col+directions[k][1]
                try:
                    #if a wall, increment wallCount
                    if mapGrid.mapGrid[x][y] == 1:
                        wallCount+=1
                except IndexError:
                    break
                #if wallCount reaches 6, this is a relatively isolated portion of path
                if wallCount >= 6:
                    #print("yay")
                    return True
        else:
            return False
###

### displayGrid ###
#takes a 2D array
#displays each row on its own line
def displayGrid(mapGrid):
    for i in range(len(mapGrid.mapGrid)):
        print(*mapGrid.mapGrid[i],sep=' ')
###

#########################
### Class Definitions ###
#########################
class mapGrid:
    #initialize
    def __init__(self, x, y, n, maxTunnels, maxLength):
        self.x = x
        self.y = y
        self.n = n
        self.maxTunnels = maxTunnels
        self.maxLength = maxLength
        self.mapGrid = initializeGrid(x,y,n)
###