import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        max_length = 0
        counter = collections.defaultdict(int)

        for end, c in enumerate(s):
            counter[c] += 1

            if end - start + 1 - max(counter.values()) > k:
                counter[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
