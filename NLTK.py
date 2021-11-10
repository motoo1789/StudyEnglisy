import nltk
import re

from nltk.corpus import stopwords


# s = "Hi, I'm Yamazaki I woke up 10pm"
s = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."

##　クリーニング
def clearn(text):
    text = re.sub(r',', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    return text

nlp = clearn(s)

stop_words = stopwords.words("english")

morph = nltk.word_tokenize(nlp)
nlp = [word for word in morph if word not in stop_words]

# pos = nltk.pos_tag(morph)

print(nlp)

