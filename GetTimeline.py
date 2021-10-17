def getTimeline(twitter):
    url_timeline = "https://api.twitter.com/1.1/statuses/user_timeline.json"

    params = {"count" : 5}
    res = twitter.get(url_timeline,params = params)

    if res.status_code  == 200:
        timelines = json.loads(res.text)
        for line in timelines:
            print(line["user"]["name"] + "::" + line["text"])
            print(line["created_at"])
            print("****************************************************")
    else:
        print("Failed:%d" % res.status_code )