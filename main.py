#This file uses functions from other files to get the user feed

import display, processing, topKFeedAlgo, helper, input

def processRawData():
    #Import dataframes of users, tweets and follows
    users = processing.processUsersFile()
    tweets = processing.processTweetsFile()
    follows = processing.processFollowsFile()
    return users, tweets, follows

def checkAndGetInput(users):
    while True:
        try:
            #Get the user input
            user_id, topK = input.getInput()
            #Get the name of the user
            name = users[users['userId']==str(user_id)]['fullDisplayName'].values[0]
            break
        except:
            print("Invalid userId. Name not found. Try again") 
    return user_id, topK, name

def getTopKFeedsFormatted(users, tweets, follows, user_id, topK):
    #Get all the user ids that the user follows 
    following_ids = helper.getFollowingIdsForAUser(user_id, follows)
    #Process the feeds of all the feeds that the user follows by putting it in a heap
    user_feeds = helper.processFeedForAllUsers(following_ids, tweets)
    #Get top K feeds of the user
    topKResults = topKFeedAlgo.getTopKFeedsOfAUser(user_feeds, topK)
    #Convert feed into human understandable format
    all_tweets = display.generateTweetFormattableData(topKResults, tweets, users)
    return all_tweets

def printFeed(name, all_tweets):
    #Print all the feeds
    display.printFeed(name, all_tweets)

def main():
    users, tweets, follows = processRawData()
    user_id, topK, name = checkAndGetInput(users)
    all_tweets = getTopKFeedsFormatted(users, tweets, follows, user_id, topK)
    printFeed(name, all_tweets)

if __name__ == "__main__":
    main()


# SAMPLE USER ID AND TOP K VALUE
# user_id = 989489610
# topK = 10