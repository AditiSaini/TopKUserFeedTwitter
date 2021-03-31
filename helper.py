#This file contains helper functions to get the topK feed

import heapq

def getFollowingIdsForAUser(userId, follows):
    return list(set(follows[follows['srcUserId']==int(userId)]["destUserId"]))

def getFeedForAUserId(userId, tweets):
    return tweets[tweets['authorId']==str(userId)]

def processFeedForEachUser(userId, tweets):
    userId_feed = getFeedForAUserId(userId, tweets)
    feed_tuple = list(userId_feed[['timestamp', 'tweetId']].itertuples(index=False, name=None))
    processed_feed = [(-1*int(x[0]), x[1]) for x in feed_tuple]
    heapq.heapify(processed_feed)
    return processed_feed

def processFeedForAllUsers(list_userIds, tweets):
    user_feeds = {}
    for userid in list_userIds:
        user_feeds[userid] = processFeedForEachUser(userid, tweets)
    return user_feeds