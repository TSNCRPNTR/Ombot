lineTest = []
rowCount = 0

#see notebook for reasoning, corners are better, but middle is best, helps resolve ties
newPoints = [5,1,6,4,9,2,8,3,7]
movePoints = [5,1,6,4,9,2,8,3,7]

def bestMove(boardState):
    ### TO DO ###
    #break it down into rows + columns
    #compare in each to see if a play could be made
    #Point comparer, to find optimal move
    #Return index of best move, change it back in main command.

    global newPoints
    global movePoints

    #row evals, checks each row to see if any have good plays
    rowEvals(boardState)
    columnEvals(boardState)
    diagEvals(boardState)

    global theBestMove
    theBestMove = 4
    

    newPoints = movePoints.copy()
    newPoints.sort()
    print(movePoints)
    print(newPoints)
    for x in newPoints:
        print(boardState[movePoints.index(x)])
        if boardState[movePoints.index(x)] != 'empt' and newPoints.index(x) == newPoints.length:
        if boardState[movePoints.index(x)] == 'empt':
            theBestMove = movePoints.index(x)
            print(theBestMove) 

    print(theBestMove)
    arrayLoc = {
        0:0 ,
        1:4,
        2:8,
        3:36,
        4:40,
        5:44,
        6:72,
        7:76,
        8:80
        }
    movePoints = [5,1,6,4,9,2,8,3,7]
    return arrayLoc.get(theBestMove)



def rowEvals(boardState):
    #3 rows, so 3 times, goes from 0 to 2
    for x in range(0,3):
        #3 spots per row
        lineTest = []
        rowCount = x*3
        for y in range (0,3):
            lineTest.append(boardState[rowCount+y])
        testXLine(lineTest, rowCount)
    rowCount = 0

def columnEvals(boardState):
    #3 columns, second verse, same as the first
    for x in range(0,3):
        #3 spots per column
        lineTest = []
        for y in range (0,3):
            lineTest.append(boardState[x+(y*3)])
        testYLine(lineTest, x)

def diagEvals(boardState):
    for x in range(0,2):
        #3 spots per row
        lineTest = []
        rowCount = x*2
        for y in range (0,3):
            lineTest.append(boardState[((4-rowCount)*y)+rowCount])
        testDiagLine(lineTest, rowCount)
    rowCount = 0

#Checks each set of possible pairs in the array, gives best spot to mark
def testXLine(lineTest, rowCount):
    if lineTest[0] == 'p1' and lineTest[1] == 'p1' or lineTest[0] == 'bot' and lineTest[1] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[rowCount+2] = movePoints[(rowCount+2)] + 9
    if lineTest[0] == 'p1' and lineTest[2] == 'p1' or lineTest[0] == 'bot' and lineTest[2] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[rowCount+1] = movePoints[(rowCount+1)] + 9
    if lineTest[1] == 'p1' and lineTest[2] == 'p1' or lineTest[1] == 'bot' and lineTest[2] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[rowCount] = movePoints[(rowCount)] + 9

def testYLine(lineTest, x):
    if lineTest[0] == 'p1' and lineTest[1] == 'p1' or lineTest[0] == 'bot' and lineTest[1] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[x+6] = movePoints[x+6] + 9
    if lineTest[0] == 'p1' and lineTest[2] == 'p1' or lineTest[0] == 'bot' and lineTest[2] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[x+3] = movePoints[x+3] + 9
    if lineTest[1] == 'p1' and lineTest[2] == 'p1' or lineTest[1] == 'bot' and lineTest[2] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[x] = movePoints[x] + 9

def testDiagLine(lineTest, rowCount):
    if lineTest[0] == 'p1' and lineTest[1] == 'p1' or lineTest[0] == 'bot' and lineTest[1] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[8-rowCount] = movePoints[8-rowCount] + 9
    if lineTest[0] == 'p1' and lineTest[2] == 'p1' or lineTest[0] == 'bot' and lineTest[2] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[4] = movePoints[4] + 9
    if lineTest[1] == 'p1' and lineTest[2] == 'p1' or lineTest[1] == 'bot' and lineTest[2] == 'bot':
        #adds 3 points to the given spot in the row.
        movePoints[rowCount] = movePoints[rowCount] + 9 