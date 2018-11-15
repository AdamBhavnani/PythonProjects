#import libraries
import TetrisFunctions as tetf

#initialize grid 10x24 filled with blanks
gameGrid = tetf.initializeGrid(10,24,'')

#initialize shapes in their default positions
shapes = []

# Box
# xx
# xx
box = tetf.initializeGrid(2,2,'x')
shapes.append(box)

# S
# ___
# _xx
# xx_
s = tetf.initializeGrid(3,3,'')
s[1][1] = s[1][2] = s[2][0] = s[2][1] = 'x'
shapes.append(s)

# T
# ___
# _x_
# xxx
t = tetf.initializeGrid(3,3,'')
t[1][1] = t[2][0] = t[2][1] = t[2][2] = 'x'
shapes.append(t)

# J
# ___
# x__
# xxx
j = tetf.initializeGrid(3,3,'')
j[1][0] = j[2][0] = j[2][1] = j[2][2] = 'x'
shapes.append(j)

# line
# _x__
# _x__
# _x__
# _x__
line = tetf.initializeGrid(4,4,'')
line[0][1] = line[1][1] = line[2][1] = line[3][1] = 'x'
shapes.append(line)

