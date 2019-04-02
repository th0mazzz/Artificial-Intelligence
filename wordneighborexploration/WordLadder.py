#!/usr/bin/python3

import sys
from itertools import permutations

neighborsDict = {}

wordlistfile = open('dictall.txt', 'rU')
wordset = list(wordlistfile.read().split('\n'))
wordlistfile.close()


def dropone(inputfilename):
    #Opens files that need to be read
    inputfile = open(inputfilename, 'rU')
    inputwords = inputfile.read().split('\n')
    inputfile.close()
    
    if inputwords[len(inputwords) - 1] == '':
        inputwords.remove('')

    #print(inputwords)
    #print(wordset)

    le_permutations = []
    
    for word in inputwords:
        index = len(word)
        while index > 0:
            perms = permutations(list(word),index)
            le_permutations.extend(perms)
            index = index - 1

        le_permutations_words = []
            
        #print(le_permutations)
        for tupple in le_permutations:
            word = ''
            for letter in tupple:
                word = word + letter

            le_permutations_words.append(word)

        #print(le_permutations_words)

        final = []
        
        for permmy in le_permutations_words:
            if permmy in wordset:
                final.append(permmy)

        le_permutations = []
        print(final)

    

dropone(sys.argv[1])
