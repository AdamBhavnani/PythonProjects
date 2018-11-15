import random #random number generation library

#while the input is not valid, keep pestering user for valid input
validLength = False
while validLength == False:
    try:
        sideLength = float((input("Enter a number for the square's side length: "))) #int() truncates toward 0, so use round()
        sideLength = int(round(sideLength)) #round to nearest integer
        validLength = True
    except ValueError:
        print("This is not an number!")

#initialize 2D list (array)
mapGrid = []
#loop through columns
for i in range(sideLength):
    mapGrid.append([])
    #loop through rows
    for j in range(sideLength):
        mapGrid[i].append(1)
#        randomCell = random.randint(0,1) #0 == path, 1 = you shall not path
#        mapGrid[i].append(randomCell)

#select random starting tile from bounds
nBound = (sideLength-1)
randomRow = random.randrange(0,nBound)
if randomRow == 0 or randomRow == nBound:#if northmost or southmost row
    randomCol = random.randrange(0,nBound)#take any element
    print("North or south")
    print(randomRow)
else:#some middle row
    randomCol = random.choice([0,nBound])#westmost or eastmost column
    print("East or west")
    print(randomCol)

#store indices of each path tile 
pathTiles = []
#index of randomly selected start of pathway
pathCurrentTile = [randomRow,randomCol]
mapGrid[randomRow][randomCol] = 0
pathTiles.append(pathCurrentTile)

#populate list of possible adjacent indices for random selection. Indices will later be used to select path on mapGrid
pathNextTiles = []

while len(pathTiles)<round(sideLength*1.5):
    up, right, left, down = [], [], [], []
    #check if corner
    if (randomRow == 0 and randomCol == 0):## NW
        right = [0,1]
        down = [1,0]
    elif (randomRow == 0 and randomCol == nBound):## NE boiii
        left = [0,nBound-1]
        down = [1,nBound]
    elif (randomRow == nBound and randomCol == 0):## SW
        up = [nBound-1,0]
        right = [nBound,1]
    elif (randomRow == nBound and randomCol == nBound):## SE
        left = [nBound,nBound-1]
        up = [nBound-1,nBound]
    #check if edge aka 3-way
    elif randomRow == 0:## north row
        right = [0,randomCol+1]
        left = [0,randomCol-1]
        down = [1,randomCol]
    elif randomRow == nBound:## south row
        right = [nBound,randomCol+1]
        left = [nBound,randomCol-1]
        up = [nBound-1,randomCol]
    elif randomCol == 0:## west col
        right = [randomRow,1]
        up = [randomRow+1,0]
        down = [randomRow-1,0]
    elif randomCol == nBound:## east col
        left = [randomRow,nBound-1]
        up = [randomRow+1,nBound]
        down = [randomRow-1,nBound]
    #else 4-way
    else:
        up = [randomRow+1,randomCol]
        right = [randomRow,randomCol+1]
        down = [randomCol-1,randomCol]
        left = [randomRow,randomCol-1]

    #check if any of these tiles have been previously visited
    #assume previous tiles have not been visited until proof is found
    previousUp = False
    previousRight = False
    previousLeft = False
    previousDown = False
    for i in range(len(pathTiles)):
        if (up and pathTiles[i] == up):
            previousUp = True
        if (right and pathTiles[i] == right):
            previousRight = True
        if (left and pathTiles[i] == left):
            previousLeft = True
        if (down and pathTiles[i] == down):
            previousDown = True
    #if no match has been found, append to index of possible next tiles
    if up and previousUp == False:
        pathNextTiles.append(up)
    if right and previousRight == False:
        pathNextTiles.append(right)
    if left and previousLeft == False:
        pathNextTiles.append(left)
    if down and previousDown == False:
        pathNextTiles.append(down)

    #check for available paths, i.e., at least one of the possible movements on mapGrid == 0
    availablePath = False
    for i in range(len(pathNextTiles)):
        x = pathNextTiles[i][0] ##getting x & y could be a function call when refactoring this
        y = pathNextTiles[i][1]
        if mapGrid[x][y] == 0:
            availablePath = True
   
    #if there is an available path (mapGrid index == 0), randomly select from pathNextTiles until it is chosen
#    if availablePath == True:
#        selectedTile = False
#        while selectedTile == False:
#            try:
#                nextTile = random.choice(pathNextTiles)
#            except:
#                break
#            x = nextTile[0]
#            y = nextTile[1]
#            if mapGrid[x][y] == 0:
#                selectedTile = True
    #if there are no available paths (mapGrid index == 1), randomly select from pathNextTiles and set mapGrid to 0
#    else:
    try:
        nextTile = random.choice(pathNextTiles)
    except:
        break
        print("Out of Index, plz fix")
    x = nextTile[0]
    y = nextTile[1]
    mapGrid[x][y] = 0
    #append the tile, set randomRow & randomCol as current cell, clear nextTiles
    pathTiles.append(nextTile)
    randomRow = nextTile[0]
    randomCol = nextTile[1]
    pathNextTiles = []

## end while

print("path is ready")
print(pathTiles)
for i in range(len(mapGrid)):
    print(mapGrid[i])