import re


def hapax(filepath):
    file = open(filepath, encoding="utf8")
    words = re.findall('\w+', file.read().lower()) #'\w+' find the first alphanumeric character 
                                                    #and then check the next character and if it is alphanumeric 
                                                    # then include it in the match 
    freqs = {key: 0 for key in words}
    for word in words:
        freqs[word] += 1
    for word in freqs:
        if freqs[word] == 1:
            print(word)

hapax('Gutenberg.txt')