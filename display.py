#This file handles data to display the feed

from datetime import datetime

def generateTweetFormattableData(topKResults, tweets, users):
    all_tweets = []
    for tweet in topKResults:
        tweetId = tweet[1]
        data = tweets[tweets['tweetId']==tweetId]
        name = users[users['userId']==str(tweet[2])]['fullDisplayName'].values[0]
        creation_time = datetime.fromtimestamp(abs(tweet[0])).isoformat()
        all_tweets.append({'name': name, 'creation_time': creation_time, 'text': data['text'].values[0]})
    return all_tweets

def printFeed(name, all_tweets):
    print('Welcome ' + str(name))
    print('Here is your feed for today!')
    print('------------LETS GO------------')
    for tweet in all_tweets:
        print(tweet['name'])
        print(tweet['creation_time'])
        print(tweet['text'])
        print('------------xxx------------')
    print("Have a great day " + str(name))
    print("That's all for today")
    print('------------THE END------------')