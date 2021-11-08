import re

def avgword(file):
    file = open(file, encoding="utf8")
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)

print(avgword('Gutenberg.txt'))