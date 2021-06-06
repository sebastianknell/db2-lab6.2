import nltk
# nltk.download("punkt")
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus.reader import lin
from nltk.stem import SnowballStemmer
from nltk.util import pr

# stoplist.txt tiene tildes
stoplist = stopwords.words('spanish')
stoplist += ['.','?','-','«', '»', ',', '(', ')', ':', ';'] # No quita todas las comas
stemmer = SnowballStemmer('spanish')
index = {}

for i in range(1,7):
    with open("docs/libro{}.txt".format(i)) as file:
        text = ""
        lines = file.readlines()
        for line in lines:
            text += line.lower().strip()
        # Tokenize
        words = nltk.word_tokenize(text)
        # Filter
        for token in words:
            if token in stoplist:
                words.remove(token)
        # Stem
        for j in range(len(words)):
            words[j] = stemmer.stem(words[j])
        # Add to index
        for token in words:
            if token in index.keys():
                index[token].add(i)
            else:
                index[token] = set([i])

# Get 500 most frequent terms
# Sort by document frequency
sortedIndex = {key : val for key, val in sorted(index.items(), key = lambda elem : len(elem[1]), reverse=True)}
mostFrequent = {}
count = 0
for key, val in sortedIndex.items():
    mostFrequent[key] = val
    count += 1
    if (count == 500):
        break

# Sort by key
invertedIndex = {key : val for key, val in sorted(mostFrequent.items(), key = lambda elem : elem[0])}

# Write to file
with open("invertedIndex.txt", 'w') as file:
    for key, value in invertedIndex.items():
        line = key
        line += ':'
        for i in value:
            line += str(i)
            line += ','
        line = line[0:len(line)-1] # Trim last ,
        line += '\n'
        file.writelines(line)