import unittest
from leetcode.algorithms.p1348_tweet_counts_per_frequency_2 import TweetCounts


class TestTweetCountsPerFrequency(unittest.TestCase):
    def test_tweet_counts_per_frequency(self):
        tweet_counts = TweetCounts()
        tweet_counts.recordTweet('tweet3', 0)
        tweet_counts.recordTweet('tweet3', 60)
        tweet_counts.recordTweet('tweet3', 10)

        self.assertListEqual([2], tweet_counts.getTweetCountsPerFrequency(
            'minute', 'tweet3', 0, 59))
        self.assertListEqual([2, 1], tweet_counts.getTweetCountsPerFrequency(
            'minute', 'tweet3', 0, 60))

        tweet_counts.recordTweet('tweet3', 120)

        self.assertListEqual([4], tweet_counts.getTweetCountsPerFrequency(
            'hour', 'tweet3', 0, 210))
        self.assertListEqual([4], tweet_counts.getTweetCountsPerFrequency(
            'day', 'tweet3', 0, 210))
