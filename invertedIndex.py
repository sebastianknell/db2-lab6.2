from typing import Sequence
import nltk
nltk.download("punkt")

text = "hola. me llamo sebastian"
words = nltk.word_tokenize(text)

print(words)