import sys
import string

def stringManipulation():
    '''
    Tokenizes a set of text into each word, removing punctuation and making lowercase
    Returns an array with all instances of words
    '''

    file = open("words.txt")
    modifiedWords = []    #variable used to store all of the stripped tokens
    for line in file.readlines():
        cleanedLine = line.strip()  #remove whitespace
        words = cleanedLine.split()  #split each line into a list of individual strings
        for word in words:
            word = word.translate(string.maketrans("",""), string.punctuation).lower()
            modifiedWords = modifiedWords + [word]  #concat arrays to create one big array of all words
    return modifiedWords    #return array of all words

stringManipulation()
