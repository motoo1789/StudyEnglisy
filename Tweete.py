def tweete(twitter):
    url_tweete = "https://api.twitter.com/1.1/statuses/update.json"

    print("文字を入力")
    tweetString = input(">> ")
    print("*****************************")

    params = {"status" : tweetString}

    res = twitter.post(url_tweete,params = params)

    if(res.status_code == 200):
        print("Success")
    else:
        print("Failed. : %d" % res.status_code)
