#USER INPUT
side = input('Enter size of side of the num square: ')

#VARIABLES
offset = 0
num = 1

#PROCESSING USER INPUT

#processing size of side
if side == '':
    side = 5
else:
    side = int(side)

matrix = [[0 for i in range(side)] for i in range(side)]

#FUNCTIONS

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j % side == 0:
                print()
            if matrix[i][j] <= 9:
                print(matrix[i][j], end = '  ')
            else:
                print(matrix[i][j], end = ' ')

def fillTop():
    global num
    global offset
    for i in range(offset, side - offset):
        matrix[offset][i] = num
        num += 1
    offset += 1

def fillRight():
    global num
    for i in range(offset, side - offset + 1):
        matrix[i][side - offset] = num
        num += 1

def fillBottom():
    global num
    for i in range(side - offset - 1, offset - 2, -1):
        matrix[side - offset][i] = num
        num += 1

def fillLeft():
    global num
    for i in range(side - offset - 1, offset - 1, -1):
        matrix[i][offset - 1] = num
        num += 1

while offset <= side // 2:
    fillTop()
    fillRight()
    fillBottom()
    fillLeft()

printMatrix(matrix)

