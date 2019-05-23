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
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.parents = [] # all layouts that can lead to this one, by one move
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('parents:',self.parents)
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
    if parent != None:
        node.parents.append(parent)
    
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
    
    
    
        
    
        
CreateAllBoards('_________',None)
print(len(AllBoards))
