import collections
import sys


# Time Limit Exceeded!
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = ''
        min_window_length = sys.maxsize

        for start, c in enumerate(s):
            current_counter = collections.Counter(t)
            end = start

            while end < len(s):
                if s[end] in current_counter:
                    current_counter[s[end]] -= 1

                    if current_counter[s[end]] == 0:
                        current_counter.pop(s[end])

                    if len(current_counter) == 0:
                        break

                end += 1

            if len(current_counter) == 0 \
                    and end - start + 1 < min_window_length:
                min_window_length = end - start + 1
                min_window = s[start:end + 1]

        return min_window
