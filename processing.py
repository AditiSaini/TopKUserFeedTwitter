#This file handles processing of data in the csv file

import pandas as pd

def processUsersFile():
    raw_users = pd.read_csv("Data/users.csv", sep='\n', header=None)
    users = raw_users[0].str.split(pat=',', n=2, expand=True).rename(columns={0: 'userId', 1: "twitterScreenName", 2:"fullDisplayName"})
    return users

def processTweetsFile():
    raw_tweets = pd.read_csv("Data/tweets.csv", sep='\n', header=None)
    tweets = raw_tweets[0].str.split(pat=',', n=3, expand=True).rename(columns={0: 'tweetId', 1: "authorId", 2: "timestamp", 3: "text"})
    return tweets

def processFollowsFile():
    follows = pd.read_csv("Data/follows.csv", header=None).rename(columns={0: 'srcUserId', 1: "destUserId"})
    return follows
