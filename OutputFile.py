def outputTweetsFile(countFileNum,tweetline):
    tweetOutputFile = open(("./Apex/" + userID + str(countFileNum) + ".txt"), "w", encoding="utf-8")
    tweetOutputFile.write(tweetline["text"])
    tweetOutputFile.close()

def outputTFResult(outputtext):
    tfOutputFile = open("./Result/TF_Result.txt","w",encoding="utf-8")
    tfOutputFile.write(outputtext)
    tfOutputFile.close()
    print("tfの出力完了")


