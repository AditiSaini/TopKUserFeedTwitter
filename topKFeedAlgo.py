#This file has an algorithm to compute the top K feed of a user

import heapq 

def getTopKFeedsOfAUser(user_feeds, topK):
    results = []
    topKResults = []
    #Load all the values with highest timestamp from each user
    for userid in user_feeds.keys():
        if len(user_feeds[userid])>0:
            value = heapq.heappop(user_feeds[userid])
            heapq.heappush(results, (value[0], value[1], userid))
    #Choose the highest of the highest values to get the feed
    while len(topKResults)<topK:
        if len(results)==0:
            break
        popped = heapq.heappop(results)
        topKResults.append(popped)
        if len(user_feeds[popped[2]])>0:
            value = heapq.heappop(user_feeds[popped[2]])
            heapq.heappush(results, (value[0], value[1], popped[2]))
    return topKResults