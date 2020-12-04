#the base maze, kept in code state, more easily read
baseMaze = [
    'wall','wall','wall','wall','wall','wall','wall','wall','wall',
    'wall','empt','empt','empt','empt','empt','empt','play','wall',
    'wall','empt','wall','wall','wall','wall','wall','wall','wall',
    'wall','empt','wall','empt','empt','empt','wall','empt','wall',
    'wall','empt','wall','wall','wall','empt','wall','empt','wall',
    'wall','empt','empt','empt','wall','empt','empt','empt','wall',
    'wall','empt','wall','empt','wall','empt','wall','empt','wall',
    'wall','empt','wall','empt','empt','empt','wall','empt','wall',
    'wall','wall','wall','wall','wall','wall','wall','empt','wall',
]

progressMaze = baseMaze

#turns maze from code state to player state, but can't go back
def buildMaze(baseMaze):
    newMaze = ''
    count = 0
    newPart = ''
    for x in baseMaze:
        if x == 'wall':
            newPart = ':purple_square:'
        elif x == 'empt':
            newPart = ':black_large_square:'
        elif x == 'play':
            newPart = ':blue_circle:'
        count += 1
        if count == 9:
            newPart += '\n'
            count = 0
        newMaze += newPart
    return newMaze


#swaps the player in a certain direction, using the progress maze, in code state, not player state
#'⬅','⬆','⬇','➡','🔄'
def arraySwap(pos):
    player = progressMaze.index('play')
    if pos == '⬅' and progressMaze[player - 1] == 'empt':
        progressMaze[player], progressMaze[player - 1] = progressMaze[player - 1], progressMaze[player]
        return buildMaze(progressMaze)
    if pos == '⬆' and progressMaze[player - 9] == 'empt':
        progressMaze[player], progressMaze[player - 9] = progressMaze[player - 9], progressMaze[player]
        return buildMaze(progressMaze)
    if pos == '⬇' and progressMaze[player + 9] == 'empt':
        progressMaze[player], progressMaze[player + 9] = progressMaze[player + 9], progressMaze[player]
        return buildMaze(progressMaze)
    if pos == '➡' and progressMaze[player + 1] == 'empt':
        progressMaze[player], progressMaze[player + 1] = progressMaze[player + 1], progressMaze[player]
        return buildMaze(progressMaze)
    if pos == '🔄':
        progressMaze[player], progressMaze[16] = progressMaze[16], progressMaze[player]
        return buildMaze(progressMaze)
