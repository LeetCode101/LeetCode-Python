import collections
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        min_window = ''
        min_window_length = sys.maxsize
        start = 0
        count = len(t)

        for end, c in enumerate(s):
            if c not in counter:
                continue

            counter[c] -= 1

            if counter[c] >= 0:
                count -= 1

            while count == 0:
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    min_window = s[start:end + 1]

                if s[start] in counter:
                    counter[s[start]] += 1

                    if counter[s[start]] > 0:
                        count += 1

                start += 1

        return min_window
