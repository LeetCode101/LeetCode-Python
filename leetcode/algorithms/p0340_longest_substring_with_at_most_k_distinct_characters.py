import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        start = 0
        max_length = 0

        for end in range(len(s)):
            c = s[end]
            counter[c] += 1

            while len(counter) > k and start < len(s):
                counter[s[start]] -= 1

                if counter[s[start]] == 0:
                    counter.pop(s[start])

                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
