import glob
import codecs as cd
import os
from chardet.universaldetector import UniversalDetector


def readexe():
    filepaths = readFilePath()

    return readFileLine()


def readFilePath():
    filepaths = glob.glob("./Apex/*.txt")
    return filepaths

def detect_char(directory):
    
    # detector.feed: バイト列を読みこませるメソッド
    # detector.done: 信頼度がある閾値を超えるとTrue となる、終了判定のためのプロパティ
    # detector.result: 結果が格納されたプロパティ
    # detector.reset: オブジェクトを初期化するメソッド

    files_code = {}
    detector = UniversalDetector()

    for file in readFilePath():
        with open(file,"rb") as f:
            detector.reset()
            for line in f.readlines():
                detector.feed(line)
                if detector.done:
                    break

            detector.close()
            files_code[file] = detector.result["encoding"]

    return files_code

def readFileLine():
    dictFileInfo = {}
    for file in readFilePath():
        with  open(file,"r",encoding='UTF-8',errors="replace") as f:
            tweetcontens = f.readlines()
            filename = splitFileName(file)
            dictFileInfo[filename] = tweetcontens

    return dictFileInfo


def splitFileName(targetFilePath):
    splitresult = os.path.splitext(os.path.basename(targetFilePath))[0]
    return splitresult
