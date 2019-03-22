#! /usr/bin/python3
import sys
import heapq

push = heapq.heappush
pop = heapq.heappop

def write_wordLadder():
    inFile = open(sys.argv[1], 'r').read().split()
    outFile = open(sys.argv[2], 'w')
    for start_target in inFile:
        pair = start_target.split(',')
        outFile.write(','.join(wordLadder(pair[0], pair[1])) + '\n')


def wordLadder(start, target):
    '''
    RETURNS A LIST THAT CONTAINS THE SHORTEST ROUTE
    FROM start TO target
    '''

    def masterDict(length):
        '''
        RETURNS A DICTIONARY OF KEYS WITH LEN length
        THAT POINT TO A LIST OF NEIGHBORS OF EACH KEY
        '''
        wordList = open('dictall.txt', 'r').read().split()
        lengthSet = set([x for x in wordList if len(x) == length])
        dict = {}
        for word in lengthSet:
            neighbors = []
            for pos in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neighbor = word[:pos] + c + word[pos + 1:]
                    if neighbor != word and neighbor in lengthSet:
                        neighbors.append(neighbor)
            dict[word] = neighbors
        return dict

    def getCost(start, target):
        '''
        RETURNS THE COST TO CHANGE FROM start TO target
        '''
        cost = 0
        for i in range(len(target)):
            if target[i] != start[i]:
                cost += 1
        return cost

    frontier, explored, path, currNeighbors = [], set(), [], [start]
    dict = (masterDict(len(start)))
    step = 0
    while True:
        # push neighbors onto frontier
        for neighbor in currNeighbors:
            push(frontier, (getCost(neighbor, target) + len(path), neighbor, path) )
            step = step + 1
        # no neighbors means no word ladder for the start -> target
        if len(frontier) == 0:
            return [start, target]
        shortest = pop(frontier)

        print(shortest)
        
        if shortest[1] == target:
            return shortest[2] + [shortest[1]]
        else:
            if shortest[1] not in explored:
                # add to explored words
                explored.add(shortest[1])
                path = shortest[2] + [shortest[1]]
                currNeighbors = [word for word in dict[shortest[1]] if word not in explored]
            else:
                path = []
                currNeighbors = []
        

write_wordLadder()
