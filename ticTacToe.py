import ticBotAi
baseBoard = [
    
    '1'   ,'empt','wall','empt','2'   ,'empt','wall','empt','3'   ,
    'empt','empt','wall','empt','empt','empt','wall','empt','empt', 
    'wall','wall','wall','wall','wall','wall','wall','wall','wall',
    'empt','empt','wall','empt','empt','empt','wall','empt','empt', 
    '4'   ,'empt','wall','empt','5'   ,'empt','wall','empt','6'   ,
    'empt','empt','wall','empt','empt','empt','wall','empt','empt', 
    'wall','wall','wall','wall','wall','wall','wall','wall','wall',
    'empt','empt','wall','empt','empt','empt','wall','empt','empt',
    '7'   ,'empt','wall','empt','8'   ,'empt','wall','empt','9'   ,
]

progressBoard = baseBoard.copy()

#yoink
#ticEmoji = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
def buildBoard(base):
    newBoard = ''
    count = 0
    newPart = ''
    for x in base:
        newPart = mazeRef(x)
        count += 1
        if count == 9:
            newPart += '\n'
            count = 0
        newBoard += str(newPart)
    return newBoard

def mazeRef(argument):
    switcher = {
        'wall': ':purple_square:',
        'empt': ':black_large_square:',
        'p1'  : ':green_circle:',
        'bot' : ':red_circle:',
        'a'   : '🇦',
        'b'   : '🇧',
        'c'   : '🇨',
        '1'   : '1️⃣',
        '2'   : '2️⃣',
        '3'   : '3️⃣',
        '4'   : '4️⃣',
        '5'   : '5️⃣',
        '6'   : '6️⃣',
        '7'   : '7️⃣',
        '8'   : '8️⃣',
        '9'   : '9️⃣'
    }
    # Returns what matches up with the input
    return switcher.get(argument)


xEmoji = ['🇦','🇧','🇨']
yEmoji = ['1️⃣','2️⃣','3️⃣']

def playerMove (reaction):
    print('PlayerMove')
    arrayLoc = {
        '1️⃣':0 ,
        '2️⃣':4,
        '3️⃣':8,
        '4️⃣':36,
        '5️⃣':40,
        '6️⃣':44,
        '7️⃣':72,
        '8️⃣':76,
        '9️⃣':80
        }
    progressBoard[arrayLoc.get(reaction)] = str('p1')
    return buildBoard(progressBoard)

def botMove():
    possibleLocs = [0,4,8,36,40,44,72,76,80]
    boardState = [None,None,None,None,None,None,None,None,None,]
    #Shrinks game board down to 3x3 for easier calcs
    for x in possibleLocs:
        if progressBoard[x] == 'bot':
            boardState[possibleLocs.index(x)] = 'bot'
        elif progressBoard[x] == 'p1':
            boardState[possibleLocs.index(x)] = 'p1'
        else:
            boardState[possibleLocs.index(x)] = 'empt'
    print(boardState)
    progressBoard[ticBotAi.bestMove(boardState)] = str('bot')
    return buildBoard(progressBoard)

def reset(board):
    movePoints = [5,1,6,4,9,2,8,3,7]
    possibleLocs = [0,4,8,36,40,44,72,76,80]
    for x in possibleLocs:
        progressBoard[x] = str(possibleLocs.index(x)+1)