import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        count = 0
        visited = set()

        for key in counter.keys():
            while counter[key] > 0 and counter[key] in visited:
                counter[key] -= 1
                count += 1

            visited.add(counter[key])

        return count
