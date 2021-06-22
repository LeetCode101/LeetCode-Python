import bisect
import collections
from bisect import bisect_left
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

        start = startTime
        counts = []

        while start <= endTime:
            end = min(start + delta, endTime + 1)
            count = bisect_left(self.tweets[tweetName], end) \
                - bisect_left(self.tweets[tweetName], start)
            counts.append(count)
            start += delta

        return counts
