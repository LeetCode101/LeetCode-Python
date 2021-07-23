import collections


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start, count = 0, 0
        counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            counter[c] += 1

            while len(counter) == 3:
                counter[s[start]] -= 1

                if counter[s[start]] == 0:
                    counter.pop(s[start])

                start += 1

            count += start

        return count
