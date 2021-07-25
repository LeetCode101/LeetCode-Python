import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = collections.defaultdict(int)
        start = 0
        max_count = 0

        for end, n in enumerate(fruits):
            counter[n] += 1

            while len(counter) > 2:
                counter[fruits[start]] -= 1

                if counter[fruits[start]] == 0:
                    counter.pop(fruits[start])

                start += 1

            max_count = max(max_count, end - start + 1)

        return max_count
