import re

def avgword(file):
    file = open(file, encoding="utf8")
    words = re.findall('\w+', file.read()) #get all wprds from the files
    avg = sum([len(word) for word in words]) / len(words) #calculate the average length of words
    print("The average word length is", "{:.2f}".format(avg)) #format it to 2 decimal places

avgword('Gutenberg.txt')