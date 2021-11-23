import nltk
import re
import emoji
import string
import demoji

from nltk.corpus import stopwords
from OutputFile import outputTFResult




def nltkStart(dictFileInfo):
    nltktargetList = []
    toNLPString = ""
    stop_words = stopwords.words("english")

    for readlines in dictFileInfo.values():
        for string in readlines:
            toNLPString += clearn(string)

    print("ライバロリ") 
    
    morph = nltk.word_tokenize(toNLPString)
    nlp = [word for word in morph if word not in stop_words]

    nltktargetList.append(nlp)
    print(nltktargetList)
    collectionTuple = getCollectionTerms(nltktargetList)

    calc_TF(nltktargetList,*collectionTuple)

# for readlines in dictFileInfo.values():
#         for string in readlines:
#             nltktargetList += clearn(string)
#             morph = nltktargetList.append(nltk.word_tokenize(nlp))
#             nlp = [word for word in morph if word not in stop_words]

#         nltktargetList.append(nlp)

#     collectionTuple = getCollectionTerms(nltktargetList)

#     calc_TF(nltktargetList,*collectionTuple)

#　クリーニング
def clearn(text):
    text = re.sub(r',', '', text)
    text = re.sub(r'\.', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'　', ' ', text)
    text = re.sub('(@[A-Za-z0-9_]+)', '',text)
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = demoji.replace(string=text,repl="")
    return text

def remove_emoji(src_str):
    return ''.join(c for c in src_str if c not in emoji.UNICODE_EMOJI)


#　コレクションとtermを取得
def getCollectionTerms(nltktargetList):

    collection = nltk.TextCollection(nltktargetList)
    terms = list(set(collection))

    print(terms)
    return (collection,terms)

#　TF-IDFの計算
def calc_TF(nltktargetList,collection,terms):
    outputtext = ""
    for word in nltktargetList:
        for term in terms:
            outputtext += term + ":" + str(collection.tf(term,word))
            outputtext += "\n"
            #print("%s : %f" % (term, collection.tf(term,word)))
            #print("%s : %f" % (term, collection.idf(term)))
            #print("%s : %f" % (term, collection.tf_idf(term,word)))
        #print("==============================")
    outputTFResult(outputtext)
    

############################################################
######事前に用意したやつ######

# s = "Natural language processing (NLP) is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data."
# additm = ["Natural","language","language"]

# nlp = clearn(s)

# stop_words = stopwords.words("english")

# morph = nltk.word_tokenize(nlp)
# nlp = [word for word in morph if word not in stop_words]

# pos = nltk.pos_tag(morph)
# print(nlp)
# print()

# #TF-IDF計算の前処理
# target = []
# target.append(nlp)
# target.append(additm)
# print(target)

# # TF-IDFを計算
# collection = nltk.TextCollection(target)
# print(collection)
# terms = list(set(collection))
# print(terms)

# for word in target :
#     for term in terms:
#         # print("%s : %f" % (term, collection.tf(term,word)))
#          print("%s : %f" % (term, collection.idf(term)))
#         # print("%s : %f" % (term, collection.tf_idf(term,word)))
#     print("==============================")





