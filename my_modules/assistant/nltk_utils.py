import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
nltk.download("punkt")


def tokenize(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    pass


a = "What does sonar do?"
a = tokenize(a)
print(a)