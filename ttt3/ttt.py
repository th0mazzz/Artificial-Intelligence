#!/usr/bin/python3

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

import functools, sys

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None if this board is not final
        self.children = [] # all layouts that can be reached with a single move

        self.best_move = None # cell position (0-8) of the best move from this layout, or -1 if this is a final layout
        self.moves_to_end = None # how many moves until the end of the game, if played perfectly.  0 if this is a final layout
        self.total_moves_to_end = None
        self.final_state = None  # expected final state ('x' if 'x' wins, 'o' if 'o' wins, else 'd' for a draw)

    def print_me(self):
        print ('         layout:',self.layout, 'endState:',self.endState)
        #print ('parents:',self.parents)
        print ('         children:',self.children)
        print ('         bestmove:',self.best_move, "total_moves_to_end:", self.total_moves_to_end)
        print ('         movestoend:', self.moves_to_end)
        print ('         expectedfinal:', self.final_state)

def endStateChecker(layout):
    for combo in Wins:
        if layout[combo[0]] == layout[combo[1]] and layout[combo[0]] == layout[combo[2]] and layout[combo[0]] != '_':
            return layout[combo[0]]
        else:
            if '_' not in layout:
                return 'd'
    return None

def CreateAllBoards(layout, parent, num_moves):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary

    # print('iteration ', layout)

    global AllBoards

    if layout in AllBoards: #base case number 1
        return

    node = BoardNode(layout)
    node.endState = endStateChecker(layout)

    if node.endState != None: #base case number 2 -- if it has endstate, return
        node.total_moves_to_end = num_moves
        node.moves_to_end = 0
        node.final_state = node.endState
        node.best_move = None
        AllBoards[layout] = node

        # print('         made it   ', layout)
        # node.print_me()
        # print('\n')
        return

    symbol = 'x' #calculates current node's player symbol
    if layout.count('x') > layout.count('o'):
        symbol = 'o'

    for index in range(9): #recurses to children
        if layout[index] == '_':
            newlayout = [x for x in layout]
            newlayout[index] = symbol
            thenewlayout = functools.reduce(lambda a, b: a + b, newlayout)

            node.children.append(thenewlayout)
            CreateAllBoards(thenewlayout, layout, num_moves + 1)



    wins = []
    draws = []
    losses = []
    for child in node.children:
        if AllBoards[child].final_state == symbol:
            wins.append(child)
        elif AllBoards[child].final_state == 'd':
            draws.append(child)
        else:
            losses.append(child)

    if len(wins) > 0:
        one_win_layout = wins[0]
        for win in wins:
            if AllBoards[win].moves_to_end < AllBoards[one_win_layout].moves_to_end:
                one_win_layout = win
        node.total_moves_to_end = AllBoards[one_win_layout].total_moves_to_end
        node.moves_to_end = node.total_moves_to_end - num_moves
        node.final_state = symbol
        node.best_move = one_win_layout
    elif len(draws) > 0:
        one_draw_layout = draws[0]
        for draw in draws:
            if AllBoards[draw].moves_to_end > AllBoards[one_draw_layout].moves_to_end:
                one_draw_layout = draw
        node.total_moves_to_end = AllBoards[one_draw_layout].total_moves_to_end
        node.moves_to_end = node.total_moves_to_end - num_moves
        node.final_state = 'd'
        node.best_move = one_draw_layout
    elif len(losses) > 0:
        one_loss_layout = losses[0]
        for loss in losses:
            if AllBoards[loss].moves_to_end < AllBoards[one_loss_layout].moves_to_end:
                one_loss_layout = loss
        node.total_moves_to_end = AllBoards[one_loss_layout].total_moves_to_end
        node.moves_to_end = node.total_moves_to_end - num_moves
        node.final_state = AllBoards[one_loss_layout].final_state
        node.best_move = one_loss_layout


    AllBoards[layout] = node

    # print('         made it   ', layout)
    # node.print_me()
    # print('\n')

    return

def ProcureBestMove(layout):
    global AllBoards
    CreateAllBoards('_________',None,0)
    node = AllBoards[layout]
    #print('layout: ', layout)
    #print('nextmove', node.best_move)

    indexofmove = None
    for i in range(9):
        if layout[i] != node.best_move[i]:
            indexofmove = i

    translations = {0:'upper-left', 1:'upper-middle', 2:'upper-right', 3:'middle-left', 4:'center', 5:'middle-right', 6:'lower-left', 7:'lower-middle', 8:'lower-right'}

    print('move=' + str(indexofmove))
    print('best move is',translations[indexofmove])

    bestmovenode = AllBoards[node.best_move]
    if bestmovenode.final_state == 'd':
        print('draw in', node.moves_to_end)
    else:
        if node.moves_to_end == 1:
            print(bestmovenode.final_state, 'wins in', node.moves_to_end, 'moves')
        else:
            print(bestmovenode.final_state, 'wins in', node.moves_to_end, 'moves')

ProcureBestMove(sys.argv[1])
