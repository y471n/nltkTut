from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Smith, how are you doing today ? The weather is good and python is awesome. " \
               "The sky is pink and land is blue."

sentences = sent_tokenize(example_text)
words = word_tokenize(example_text)

print(sentences)
print(words)

print(*sentences, sep='\n')