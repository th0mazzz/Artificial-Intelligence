#! /usr/bin/python3

"""WordLadder

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E7i3ZhzIClKrFKNZJP18DVSCF3REwqZ6
"""

class PriorityQueue:
    
    def compare(first, second):
        if first < second:
            return -1
        
        elif first == second:
            return 0
        
        else:
            return 1
    
    def __init__(self, comparison = compare):
        self.heap = [None]
        self.compareTo = comparison
        self.filledTo = 0
    
    def __str__(self):
        words = [str(item) for item in self.heap]
        words = words[1: self.filledTo + 1]
        
        return '{%s}' % ', '.join(words)
    
    def getParent(self, index):
        return index // 2
    
    def getFirst(self, index):
        return 2 * index
    
    def getSecond(self, index):
        return 2 * index + 1
    
    def length(self):
        return self.filledTo
    
    def push(self, element):
        #article = Node(element)
        self.filledTo += 1
        #print(self.filledTo)
        
        if self.filledTo < len(self.heap):
            self.heap[self.filledTo] = element
            #print('space')
        
        else:
            #print('full')
            self.heap.append(element)
            
        if self.filledTo > 1:
            index = self.filledTo
            parent = self.getParent(index)
            
            while parent >= 1 and self.compareTo(element, self.heap[parent]) < 0:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                
                index = parent
                parent = self.getParent(index)
                
                #print(self.list)
    
    def pop(self):
        if self.filledTo == 0:
            #print('sad')
            return None
        
        element = self.heap[1]
        
        if self.filledTo == 1:
            self.filledTo = 0
            return element
        
        self.heap[1] = self.heap[self.filledTo]
        
        #self.heap.remove(self.heap[len(self.heap) - 1])
        self.filledTo -= 1
        current = 1
        
        '''
        while self.getFirst(current) < self.filledTo and self.compareTo(self.heap[current], self.heap[self.getFirst(current)]) > 0 or self.getSecond(current) < self.filledTo and self.compareTo(self.heap[current], self.heap[self.getSecond(current)]) > 0:
            if not self.getSecond(current) < self.filledTo and self.compareTo(self.heap[current], self.heap[self.getFirst(current)]) > 0:
                self.heap[current], self.heap[self.getFirst(current)] = self.heap[self.getFirst(current)], self.heap[current]
                current = self.getFirst(current)
            
            elif self.getFirst(current) < self.filledTo and self.getSecond(current) < self.filledTo:
                if self.compareTo(self.heap[self.getFirst(current)], self.heap[self.getSecond(current)]) < 0:
                    self.heap[current], self.heap[self.getFirst(current)] = self.heap[self.getFirst(current)], self.heap[current]
                    current = self.getFirst(current)
                
                else:
                    self.heap[current], self.heap[self.getSecond(current)] = self.heap[self.getSecond(current)], self.heap[current]
                    current = self.getSecond(current)
            
            else:
                break     
        '''
        
        while self.getFirst(current) <= self.filledTo:
            firstChild = self.getFirst(current)
            secondChild = self.getSecond(current)
            
            #Has one child.
            if secondChild > self.filledTo:
                if self.compareTo(self.heap[current], self.heap[firstChild]) > 0:
                    self.heap[current], self.heap[firstChild] = self.heap[firstChild], self.heap[current]
                    print(current)
                    current = firstChild
                    
                else:
                    break
                
            #Has two children.
            else:
                if self.compareTo(self.heap[firstChild], self.heap[secondChild]) <= 0:
                    if self.compareTo(self.heap[current], self.heap[firstChild]) > 0:
                        self.heap[current], self.heap[firstChild] = self.heap[firstChild], self.heap[current]
                        current = firstChild
                    
                    else:
                        break
                    
                
                else:
                    if self.compareTo(self.heap[current], self.heap[secondChild]) > 0:
                        self.heap[current], self.heap[secondChild] = self.heap[secondChild], self.heap[current]
                        current = secondChild
                    
                    else:
                        break
        
        return element

    def peek(self):
        return self.heap[1]
    
    def toList(self):
        answer = []
        
        while self.filledTo > 0:
            answer.append(self.pop())
            #print(answer)
        
        #self.heap.clear()
        
        return answer

    def toString(self):
        words = [str(item) for item in self.heap]
        words = words[1: self.filledTo + 1]
        
        return ','.join(words)

'''
A = PriorityQueue()
A.push(2)
A.push(12412)
A.push(0)
A.push(3)
print(A)
print(A.pop())
print(A)
print(A.pop())
print(A)
A.push(342)
A.pop()
print(A)
'''

class Node:
    
    def __init__(self, data, a, b, way):
        self.word = data
        self.traveled = a
        self.different = b
        self.cost = a + b
        self.path = way
        
        #self.previous = back
        #self.neighbors = []
        #self.commonLetters = 0
    
    def __str__(self):
        return self.word

import sys

a = open('dictall.txt', 'r')
n = open(sys.argv[1], 'r')
#n = open('TestInput.txt', 'r')

b = a.read().strip().split('\n')
o = n.read().strip().split('\n')

a.close()
n.close()

lexicon = []
prompts = ','.join(o).split(',')

size = len(prompts[0])

for word in b:
    if len(word) == size:
        lexicon.append(word.strip())

#print(lexicon)

def diffLetters(first, second):
    counter = 0
    index = 0

    while index < len(first):
        if first[index] != second[index]:
            counter = counter + 1
        index = index + 1
    
    return counter

#writeFile = open(sys.argv[2], 'w')
vocabulary = {}

#for index in range(len(prompts)):
#    if index % 2 == 0:
for element in lexicon:
    #print("Element: " + element)
    values = []
    
    for term in lexicon:
        #print("Term: " + term)
        if diffLetters(element, term) == 1:
            values.append(term)
    
    vocabulary[element] = values
    #writeFile.write(element + ',' + str(len(values)) + '\n')
#writeFile.write(element + ',' + str(len(values)) + '\n')

#print(vocabulary['heal'])

def contrast(first, second):
    return first.cost - second.cost

frontier = PriorityQueue(contrast)
checked = set()

writeFile = open(sys.argv[2], 'w')
#writeFile = open('TestOutput.txt', 'w')

for number in range(len(prompts)):
    if number % 2 == 0:
        #print('start')
        
        frontier.push(Node(prompts[number], 0, diffLetters(prompts[number], prompts[number + 1]), [prompts[number]]))
        closest = None
        
        while frontier.length() > 0:
            closest = frontier.pop()
            print(closest)
            print('FRONTIER: ' + frontier.toString())
            
            if closest.word == prompts[number + 1]:
                #print('happy')
                
                result = ','.join(closest.path)
                writeFile.write(result + '\n')
                
                checked.clear()                
                frontier.toList()
                #print(frontier)
                
                break
                
            else:
                #print('sad')
                neighbors = vocabulary.get(closest.word)
                #print('neighbors of %s are %s' % (closest.word, str(neighbors)))
                
                if neighbors:
                    for instance in neighbors:
                        if instance not in checked:
                            #print('there')
                            path_copy = closest.path[:] + [instance]
                            print(path_copy)
                            frontier.push(Node(instance, closest.traveled + 1, diffLetters(instance, prompts[number + 1]), path_copy))
                            #print(path_copy)
                
                checked.add(closest.word)
            #print("here")
        
        if closest.path[-1] != prompts[number + 1]:
            writeFile.write(prompts[number] + ',' + prompts[number + 1] + '\n')
        
writeFile.close()