import re
def splitter(file):
    file = open(file, encoding="utf8")
    f = file.read()
    sentences = re.sub(r'\n','', f)  #remove newlines that were already there
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)  #add a new line after each period only of that period is not
                                                                                    #preceded by Mr, Mrs, Dr and is not followed by a space and an uppercase letter

    sentences = re.sub(r'!\s', '!\n', sentences) # add new line after every !
    sentences = re.sub(r'\?\s', '?\n', sentences) # add new line after every ?
    print(sentences)

splitter('text.txt')