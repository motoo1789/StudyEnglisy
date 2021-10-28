import glob
import codecs as cd
import os
from chardet.universaldetector import UniversalDetector



def readexe():
    filepaths = readFilePath()
    files_code = detect_char(filepaths)
    readFileLine(files_code)

def readFilePath():
    filepaths = glob.glob("./Apex/*.txt")
    return filepaths

def readFileLine(files_code):
    for file in readFilePath():
        with  open(file,"r",encoding=files_code[file],errors="replace") as f:
            lists = f.readlines()
            for line in lists:
                print(line)

            
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