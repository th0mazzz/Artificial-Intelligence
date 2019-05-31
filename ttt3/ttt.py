''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

import functools

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None if this board is not final
        self.children = [] # all layouts that can be reached with a single move

        self.best_move = None # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end = None # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.final_state = None  # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        #print ('parents:',self.parents)
        print ('children:',self.children)

def endStateChecker(layout):
    for combo in Wins:
        if layout[combo[0]] == layout[combo[1]] and layout[combo[0]] == layout[combo[2]] and layout[combo[0]] != '_':
            return layout[combo[0]]
        else:
            if '_' not in layout:
                return 'd'
    return None

def CreateAllBoards(layout, parent):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary

    global AllBoards

    node = BoardNode(layout)
    #if parent != None:
        #node.parents.append(parent)

    node.endState = endStateChecker(layout)
    #node.print_me()
    AllBoards[layout] = node

    if node.endState != None:
        return None

    symbol = 'x'

    if layout.count('x') > layout.count('o'):
        symbol = 'o'

    for index in range(9):
        if layout[index] == '_':
            newlayout = [x for x in layout]
            newlayout[index] = symbol
            thenewlayout = functools.reduce(lambda a, b: a + b, newlayout)

            node.children.append(thenewlayout)
            CreateAllBoards(thenewlayout, layout)



def NextBestMove(layout, path, wins=[], draws=[], losses=[]):
    current = AllBoards[layout]

    symbol = 'x'
    if layout.count('x') > layout.count('o'):
        symbol = 'o'

    if current.endState == symbol:
        wins.append((layout, len(path)))
        return
    elif current.endState == 'd':
        draws.append((layout, len(path)))
        return

    sojourn = list(path)
    frontier = []

    print('path thus far: ' + str(sojourn))
    print('curr board: ' + str(layout))
    print('curr children: ' + str(current.children))
    print('----\n')

    for child in current.children:
        frontier.append(child)
        sojourn.append(child)
        return NextBestMove(child, sojourn)
        sojourn.pop()

    #wins = [(layout, path_len), (layout, path_len)]
    # if len(wins) > 0:
    #     best = wins[0][1]
    #     for eachwin in wins:
    #         if eachwin[1] < best:
    #             best = eachwin[1]
    #     return best
    # if len(draws) > 0:
    #     best = draws[0][1]
    #     for eachdraw in draws:
    #         if eachdraw[1] < best:
    #             best = eachdraw[1]
    #     return best



CreateAllBoards('_________',None)
#print(AllBoards)
move = NextBestMove('x_ox_o___', [])
print('le chosen move: \n' + str(move))
