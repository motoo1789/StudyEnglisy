import json
from OutputFile import outputTweetsFile

def getTimeline(twitter):
    url_timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    acount = {
        "ImperialHal",
        "Snip3down",
        "sweetdreamsh1",
        "TSM_Albralelie",
        "TSM_Reps",
        "iiTzTimmy",
        "nafengg",
        "TTrebb",   # Rogue
    }

    for userID in acount:
        
        params = {
            "screen_name":userID,
            "count" : 500,
            "include_entities": True,   #  動画や画像を含まない
            "exclude_replies": True,    #　リプライは含まない
            "include_rts" : False,       #　リツイートは含まない
            # "trim_user" : False
            
        }
        res = twitter.get(url_timeline,params = params)

        if res.status_code  == 200:
            timelines = json.loads(res.text)
            count = 1
            for line in timelines:
                outputTweetsFile(count,line)
                print(line["user"]["name"] + "::" + line["text"])
                print(line["created_at"])
                print("****************************************************")
                count += 1

        else:
            print("Failed:%d" % res.status_code )