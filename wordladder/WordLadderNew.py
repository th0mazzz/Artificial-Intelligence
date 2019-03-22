#!/usr/bin/python3

import sys

# ---------------------- PRIORITY QUEUE METHODS -------------------------
def NeighborComparison(a,b): # tuple 
    if (a[1] + a[2]) < (b[1] + b[2]): return -1
    if (a[1] + a[2]) == (b[1] + b[2]): return 0
    return 1

class PQueue:
    def OrdinaryComparison(a,b): #ordinary compare_to fxn
        if a < b: return -1
        if a == b: return 0
        return 1
    
    def __init__(self, comparator = OrdinaryComparison): #initializes priority queue / heap
        self.info = []
        self.size = 0
        self.compare_to = comparator
                
    def __str__(self): #the to-string method
        returned = []
        for each in self.info:
            returned.append(each)
        return str(returned)
    
    def push(self, value): #pushs value into heap; sorts it so that parent >= child
        self.info.append(value)
        self.size = self.size + 1

        current = self.size - 1
        parent = int((current - 1) / 2)

        while(self.compare_to(self.info[current], self.info[parent]) == -1 and parent >= 0):
            self.info[current], self.info[parent] = (self.info[parent], self.info[current])

            current = parent
            parent = int((parent - 1) / 2)

    def pop(self): #pops off the top element and returns it; if empty, returns None
        if self.size == 0:
            return None
        
        oldroot = self.info[0]

        self.info[0] = self.info[self.size - 1]
        del self.info[-1]
        self.size = self.size - 1

        current = 0
        leftchild = 2 * current + 1
        rightchild = 2 * current + 2

        if self.size == 2 and self.compare_to(self.info[current], self.info[leftchild]) == 1:
            self.info[current], self.info[leftchild] = (self.info[leftchild], self.info[current])
        
        while(leftchild < self.size and rightchild < self.size and
              (self.compare_to(self.info[current], self.info[leftchild]) == 1 or self.compare_to(self.info[current], self.info[rightchild]) == 1)):

            if self.compare_to(self.info[leftchild], self.info[rightchild]) == 1:
                self.info[current], self.info[rightchild] = (self.info[rightchild], self.info[current])
                current = rightchild
                leftchild = current * 2 + 1
                rightchild = current * 2 + 2
            else:
                self.info[current], self.info[leftchild] = (self.info[leftchild], self.info[current])
                current = leftchild
                leftchild = current * 2 + 1
                rightchild = current * 2 + 2
                
        return oldroot

                
    def peek(self): #returns but does not pop top element; if empty, returns None
        if self.size > 0:
            return self.info[0]
        return None

    def size(self): #returns size of the current priority queue / heap
        return self.size

    def tolist(self):
        returned_list = []
        size = 0
        while size < len(self.info):
            returned_list.append(self.pop())
        return returned_list

    def push_all(self, the_list): #pushs all the elements of the provided list
        for each in the_list:
            self.push(each)

    def internal_list(self): #returns all of the valid elements of your internal list
        return self.info[:self.size]

# ---------------- WORD LADDER ---------------------

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
neighborsDict = {}

wordlistfile = open('dictall.txt', 'rU')
wordset = set(wordlistfile.read().split('\n'))
wordlistfile.close()

def createNeighborsDict(wordlength):
    for word in wordset:
        if len(word) == wordlength:
            index = 0
            neighbors = set()
            while index < wordlength:
                
                for letter in alphabet:
                    new_word = word[:index] + letter + word[index+1: wordlength]
                    if new_word in wordset:
                        neighbors.add(new_word)
                index = index + 1

            if word in neighbors:
                neighbors.remove(word)
                
            neighbors = list(neighbors)
    
            neighborsDict[word] = neighbors

def charDiff(worduno, worddos):
    if not len(worduno) == len(worddos):
        return -1
    index = 0
    numDiff = 0
    while index < len(worduno):
        if not worduno[index] == worddos[index]:
            numDiff = numDiff + 1
        index = index + 1
    return numDiff

def pathfinder(start, target):
    frontier = PQueue(NeighborComparison)
    explored = set()
    
    frontier.push((start, charDiff(start, target), 0, [])) # (word, charDiff, len_of_path, path)

    while frontier.size != 0:
        #print(frontier)
        #print('\n')
        current = frontier.pop()
        if current[0] == target:
            return current[3] + [current[0]]
        else:
            if current[0] not in explored:
                explored.add(current[0])
                current_path = current[3][:]+[current[0]]
                neighbors = neighborsDict[current[0]]
                #print('--------------')
                #print(neighbors)
                #print('--------------')
                for neigh in neighbors:
                    if neigh not in explored:
                        frontier.push((neigh, charDiff(neigh, target), len(current[3]), current_path))
    return [start, target]

def wordladder(inputfilename, outputfilename):
    #Opens files that need to be read
    inputfile = open(inputfilename, 'rU')
    inputwords = inputfile.read().split('\n')
    inputfile.close()

    #Generates key, value for start, end words
    goals = [] # {startWord: endWord}

    wordlen = 0
    
    for pair in inputwords:
        moses = pair.split(',')
        if len(moses) == 2:
            goals.append((moses[0], moses[1]))
            if wordlen == 0:
                wordlen = len(moses[0])

    print(goals)
                
    #Gets rid of empty strings at end in case there is one
    if inputwords[len(inputwords) - 1]  == '' and len(inputwords) > 0:
        inputwords.remove('')

    createNeighborsDict(wordlen)

    pathes = []
    
    for pair in goals:
        print('from ' + pair[0] + ' to ' + pair[1])
        #print(pathfinder(pair[0], pair[1]))
        pathes.append(pathfinder(pair[0], pair[1]))
        print('\n')
    
    
    
    return_string = ''
    print(pathes)
    for path in pathes:
        line = ''
        for word in path:
            line = line + word + ','
        line = line[:len(line)-1] + '\n'
        return_string = return_string + line

    print(return_string)
        
    output = open(outputfilename, 'w')
    output.write(return_string)
    output.close()

    

wordladder(sys.argv[1], sys.argv[2])
