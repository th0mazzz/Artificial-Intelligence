#!/usr/bin/python3

import sys

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def neighbors(inputted, output):
    #Opens files that need to be read
    wordlistfile = open('dictall.txt', 'rU')
    wordset = set(wordlistfile.read().split('\n'))
    wordlistfile.close()

    inputfile = open(inputted, 'rU')
    inputwords = inputfile.read().split('\n')
    inputfile.close()

    #Gets rid of empty strings at end in case there is one
    if inputwords[len(inputwords) - 1]  == '' and len(inputwords) > 0:
        inputwords.remove('')

    #Establishes what the length of words in input file are
    wordlength = len(inputwords[0])

    #Instantiates the dictionary of <wordlength>-character long words
    neighborsDict = {}

    #For each <wordlength>-character long word in wordset,
    #figure out its neighbors and see if they are valid by checking if they are in wordset.
    #If they are, add them to neighbors, if not, ignore.
    #Once done for current word, create key, value pair with word as key and neighbors as value.
    #Sets and lists are to ensure duplicates do not appear.
    #Also checks if the word itself is in neighbors; if it is, remove.
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

    #Puts all the inputwords and the number of "neighboring" words into one string
    writeinfo = ''
    for each in inputwords:
        writeinfo = writeinfo + each + ',' + str(len(neighborsDict[each])) + '\n'
            
    #Writes said string to output file
    outputfile = open(output, 'w')
    outputfile.write(writeinfo)
    outputfile.close()

neighbors(sys.argv[1], sys.argv[2])
