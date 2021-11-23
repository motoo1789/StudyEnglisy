############################################################
######事前に用意したやつ######
import nltk
import re
from nltk.corpus import stopwords

def clearn(text):
    text = re.sub(r',', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'　', ' ', text)
    text = re.sub(r'@[w/:%#$&?()~.=+-…]+', '',text)
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
    return text

s = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."
additm = ["Natural","language","language"]


stop_words = stopwords.words("english")

nlp = clearn(s)

morph = nltk.word_tokenize(nlp)
nlp = [word for word in morph if word not in stop_words]

pos = nltk.pos_tag(morph)
print(nlp)
print()

#TF-IDF計算の前処理
target = []
target.append(nlp)
target.append(additm)
print(target)

# TF-IDFを計算
collection = nltk.TextCollection(target)
print(collection)
terms = list(set(collection))
print(terms)

for word in target :
    for term in terms:
        print("%s : %f" % (term, collection.tf(term,word)))
        #print("%s : %f" % (term, collection.idf(term)))
        # print("%s : %f" % (term, collection.tf_idf(term,word)))
    print("==============================")

