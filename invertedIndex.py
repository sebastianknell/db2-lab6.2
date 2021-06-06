import nltk
# nltk.download("punkt")
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.util import pr

files = ["libro{}.txt".format(i) for i in range(1, 7)]

# stoplist.txt tiene tildes
stoplist = stopwords.words('spanish')
stoplist += ['.','?','-','«', '»', ',']

with open("docs/{}".format(files[0])) as file:
    lines = file.readlines()
    text = ""
    for line in lines:
        text += line.lower().strip()

words = nltk.word_tokenize(text)
for token in words:
    if token in stoplist:
        words.remove(token)

# print(words)
stemmer = SnowballStemmer('spanish')
for i in range(len(words)):
    words[i] = stemmer.stem(words[i])

print(words)