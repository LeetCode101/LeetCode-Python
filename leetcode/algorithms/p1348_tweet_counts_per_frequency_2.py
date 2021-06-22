import bisect
import collections
from typing import List


class TweetCounts:
    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                   startTime: int, endTime: int) -> List[int]:
        delta = 1

        if freq == 'minute':
            delta = 60
        elif freq == 'hour':
            delta = 60 * 60
        elif freq == 'day':
            delta = 60 * 60 * 24

        size = (endTime - startTime) // delta + 1
        counts = [0] * size

        for time in self.tweets[tweetName]:
            if startTime <= time <= endTime:
                index = (time - startTime) // delta
                counts[index] += 1

        return counts
