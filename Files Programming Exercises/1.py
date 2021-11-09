import re

def hapax(file):
    file = open(file, encoding="utf8")
    words = re.findall('\w+', file.read().lower()) # Get all the names from the file and convert it to all lower
                                                    #'\w+' find the first alphanumeric character 
                                                    #and then check the next character and if it is alphanumeric 
                                                    # then include it in the match 
    freqs = {key: 0 for key in words}  #dict for counting the key/word
    for word in words:  
        freqs[word] += 1  # input words into the dict and count it
    for word in freqs:
        if freqs[word] == 1:    # if word is more than 1, it will not be printed as it is not a hapax
            print(word)

hapax('Gutenberg.txt')