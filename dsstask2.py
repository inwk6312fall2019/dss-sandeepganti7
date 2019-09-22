def stringManipulationPG(file):
    '''
    Goes to the beginning of a Project Gutenberg book and tokenizes text into words, removing punctuation and making lowercase. 
    Returns a list of 'word,value' pairs for each instance of a token output to the file 'output.txt.' 
    Sorts list in preparation for reducing step
    '''

    startBook = False
    totalWords = 0
    fullArray = []
    output = ''
    file = open(file)
    for line in file.readlines():
        if line.find("*** START OF THIS PROJECT GUTENBERG EBOOK") != -1:
            startBook = True
        elif line.find("*** END OF THIS PROJECT GUTENBERG EBOOK") != -1: #reached end of ebook, so stop adding lines
            startBook = False       
        elif startBook and line.find("*** START OF THIS PROJECT GUTENBERG EBOOK") == -1 and len(line) > 1:
            cleanedLine = line.strip()
            words = cleanedLine.split()
            modifiedWords = []
            for word in words:
                word = word.translate(string.maketrans("",""), string.punctuation).lower()
                if word != "":
                    modifiedWords = modifiedWords + [word]
                    totalWords = totalWords + 1
            fullArray = fullArray + modifiedWords
    for element in sorted(fullArray):
        output = output + element+",1\n"
    with open('words.txt', 'w') as f:  
        f.write(output)
    return 'output.txt'
