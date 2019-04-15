#!/bin/usr/python3

#-------- GLOBAL VARS --------
numBack = 0
numTrials = 0
board = []
cliques = [[0,1,2,3,4,5,6,7,8],
         [9,10,11,12,13,14,15,16,17],
         [18,19,20,21,22,23,24,25,26],
         [27,28,29,30,31,32,33,34,35],
         [36,37,38,39,40,41,42,43,44],
         [45,46,47,48,49,50,51,52,53],
         [54,55,56,57,58,59,60,61,62],
         [63,64,65,66,67,68,69,70,71],
         [72,73,74,75,76,77,78,79,80],
         [0,9,18,27,36,45,54,63,72],
         [1,10,19,28,37,46,55,64,73],
         [2,11,20,29,38,47,56,65,74],
         [3,12,21,30,39,48,57,66,75],
         [4,13,22,31,40,49,58,67,76],
         [5,14,23,32,41,50,59,68,77],
         [6,15,24,33,42,51,60,69,78],
         [7,16,25,34,43,52,61,70,79],
         [8,17,26,35,44,53,62,71,80],
         [0,1,2,9,10,11,18,19,20],
         [3,4,5,12,13,14,21,22,23],
         [6,7,8,15,16,17,24,25,26],
         [27,28,29,36,37,38,45,46,47],
         [30,31,32,39,40,41,48,49,50],
         [33,34,35,42,43,44,51,52,53],
         [54,55,56,63,64,65,72,73,74],
         [57,58,59,66,67,68,75,76,77],
         [60,61,62,69,70,71,78,79,80]]

import sys

def createBoard(inputfilename, puzzlename):
    with open(inputfilename) as file:
        content = file.readlines()
        content = [x.strip() for x in content]
    #print(content)

    puzzle = []

    if puzzlename == 'A1-1,Easy-NYTimes,unsolved':
        puzzlenameIndex = content.index('A1-1,Easy-NYTimes,unsolved')
    elif puzzlename == 'A2-1,Medium-NYTimes,unsolved':
        puzzlenameIndex = content.index('A2-1,Medium-NYTimes,unsolved')
    else:
        puzzlenameIndex = content.index('A3-1,Hard-NYTimes,unsolved')

    puzzleTemp = []
    for i in range(9):
        puzzleTemp.append(content[i + 1 + puzzlenameIndex])
    for line in puzzleTemp:
        split = line.split(',')
        board.extend(split)


def printBoard(the_board):
    print(the_board[0:9])
    print(the_board[9:18])
    print(the_board[18:27])
    print(the_board[27:36])
    print(the_board[36:45])
    print(the_board[45:54])
    print(the_board[54:63])
    print(the_board[63:72])
    print(the_board[72:])

    #for i in range(8)

def getNextTile(the_board, the_current):
    if the_current == len(board) - 1:
        #print('getNextTile(): None')
        return None
    else:
        while not the_board[the_current] == '_':
            the_current = the_current + 1
        #print('getNextTile(): ' + str(the_current))
        return the_current

def isValid(the_board, the_current, the_guess):
    importante = set()
    for cliq in cliques:
        if the_current in cliq:
            for each in cliq:
                if not each == the_current:
                    importante.add(each)
    #print(the_board)
    for each in importante:
        if the_board[each] == str(the_guess):
            return False
    return True

def main(inputBoards, outputname, puzzlename):
    createBoard(inputBoards, puzzlename)
    mainHelper(board, 0)

i = 0

def mainHelper(the_board, current_tile):
    global i
    i = i + 1
    print(i)
    global numTrials
    global numBack
    if current_tile == None:
        printBoard(the_board)
        print('numTrials: ' + str(numTrials))
        print('numBacks: ' + str(numBack))
        return the_board

    digits = [1,2,3,4,5,6,7,8,9]
    for guess in digits:
        numTrials = numTrials + 1
        if isValid(the_board, current_tile, guess):
            the_board[current_tile] = str(guess)
            mainHelper(the_board[:], getNextTile(the_board[:], current_tile))

    numBack = numBack + 1




main(sys.argv[1], sys.argv[2], sys.argv[3]) #$python <this file> <input boards> <output name> <which puzzle>
