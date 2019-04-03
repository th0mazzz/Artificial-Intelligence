#!/usr/bin/python3

import sys
from itertools import permutations

neighborsDict = {}

wordlistfile = open('dictall.txt', 'rU')
wordset = list(wordlistfile.read().split('\n'))
wordlistfile.close()




def dropone(inputfilename):
    #Opens files that need to be read
    #inputfile = open(inputfilename, 'rU')
    #inputwords = inputfile.read().split('\n')
    #inputfile.close()
    
    #if inputwords[len(inputwords) - 1] == '':
    #    inputwords.removes('')

    inputwords = []
    
    for each in wordset:
        if len(each) == 5:
            inputwords.append(each)

    #print(inputwords)
    #print(wordset)

    le_permutations = []

    winner_word = None
    winner_anagrams = []
    
    for word in inputwords:
        print(word)
        index = len(word)
        while index > 0:
            perms = permutations(list(word),index)
            le_permutations.extend(perms)
            index = index - 1

        le_permutations_words = []
            
        #print(le_permutations)
        for tupple in le_permutations:
            yum = ''
            for letter in tupple:
                yum = yum + letter

            le_permutations_words.append(yum)

        #print(le_permutations_words)

        final = set()
        
        for permmy in le_permutations_words:
            if permmy in wordset:
                final.add(permmy)

        le_permutations = []
        #print(final)
        #print('\n')

        if len(winner_anagrams) <= len(final):
            winner_word = word
            winner_anagrams = final

    return (winner_word, winner_anagrams, len(winner_anagrams))

    

print(dropone(sys.argv[1]))
