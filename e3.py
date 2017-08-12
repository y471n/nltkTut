from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythonic", "pythoner", "pythoning", "pythoned", "pythonly"]

# [print(ps.stem(w)) for w in example_words]

new_text = "It is very important to be pythonly while you're pythoning with python. All pythoners " \
           "have pythoned atleast once."

words = word_tokenize(new_text)

[print(ps.stem(w)) for w in words]