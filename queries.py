indexFile = "invertedIndex.txt"

def parseLine(line):
    word = ""
    docs = []
    i = 0
    while(i < len(line) and line[i] != ':'):
        word += line[i]
        i += 1
    i += 1
    temp = ""
    while(i < len(line) and line[i] != '\n'):
        if (line[i] == ','):
            docs.append(int(temp))
            temp = ""
        else:
            temp += line[i]
        i += 1
    docs.append(int(temp))
    return (word, docs)


def readIndex(index = indexFile):
    invertedIndex = {}
    with open(index) as file:
        for line in file:
            item = parseLine(line.strip())
            invertedIndex[item[0]] = item[1]
    
    for key, value in invertedIndex.items():
        print(key, ':', str(value))

readIndex()