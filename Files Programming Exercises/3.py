import re

def avgword(file):
    file = open(file, encoding="utf8")
    words = re.findall('\w+', file.read())
    avg = sum([len(word) for word in words]) / len(words)
    print("The average word length is", "{:.2f}".format(avg))

avgword('Gutenberg.txt')