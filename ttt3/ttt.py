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

        #self.best_move  # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        #self.moves_to_end  # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        #self.final_state   # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

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

def GetBestMove(layout):
    layout_info = AllBoards[layout]
    print(layout)
    print(layout_info.children)

    if len(layout_info.children) == 0:
        return layout_info.endState

    for child in layout_info.children:
        returned = GetBestMove(child)
        if returned == 'x':
            print('\nthe chosen one:')
            return child





CreateAllBoards('_________',None)
#print(AllBoards)
move = GetBestMove('x_ox_o___')
print('le chosen move: \n' + move)
