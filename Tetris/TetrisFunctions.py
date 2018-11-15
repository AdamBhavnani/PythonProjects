#import libraries
import pygame, sys, random


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

### rotateBlock ###
#takes a 2D block (list of lists)
#rotates elements in the grid 90 degrees clockwise
#returns a newly rotated 2D list
def rotateBlock(block):
    
    return rotatedBlock
###