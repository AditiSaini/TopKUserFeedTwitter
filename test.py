#This file has test cases to evaluate the code

import unittest
import main
from expectedAnswersTest import *

class Test(unittest.TestCase):
    def setUp(self):
        #Processed raw data
        users, tweets, follows = main.processRawData()
        self.users = users
        self.tweets = tweets
        self.follows = follows       

    def test1_topFiveFeeds_ZeroFollowing_userSteveYegge(self):
        user_id = 429567341
        topK = 5
        all_tweets = main.getTopKFeedsFormatted(self.users, self.tweets, self.follows, user_id, topK)
        self.assertListEqual(all_tweets, expected_answer1)
    
    def test2_topFiveFeeds_ZeroFeedAvailable_userBaptisteWicht(self):
        user_id = 113309454
        topK = 5
        all_tweets = main.getTopKFeedsFormatted(self.users, self.tweets, self.follows, user_id, topK)
        self.assertListEqual(all_tweets, expected_answer2) 

    def test3_topFourFeeds_success_userEvanJones(self):
        user_id = 989489610
        topK = 4
        all_tweets = main.getTopKFeedsFormatted(self.users, self.tweets, self.follows, user_id, topK)
        self.assertListEqual(all_tweets, expected_answer3)
    
    def test4_topTwoFeeds_success_userCMUDatabaseGroup(self):
        user_id = 2252942868
        topK = 2
        all_tweets = main.getTopKFeedsFormatted(self.users, self.tweets, self.follows, user_id, topK)
        self.assertListEqual(all_tweets, expected_answer4)

    def test5_topHunderedFeeds_onlyTopNinetyNineFeedsAvailable_userGarryJones(self):
        user_id = 2732562482
        topK = 100
        all_tweets = main.getTopKFeedsFormatted(self.users, self.tweets, self.follows, user_id, topK)
        self.assertListEqual(all_tweets, expected_answer5)
    
if __name__ == "__main__":
    unittest.main()