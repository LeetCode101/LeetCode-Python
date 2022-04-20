import collections
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = collections.Counter(tasks).values()

        return -1 if 1 in counter \
            else sum((count + 2) // 3 for count in counter)
