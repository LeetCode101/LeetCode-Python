import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        k = 2
        counter = collections.defaultdict(int)
        start = 0
        max_length = 0

        for end in range(len(s)):
            c = s[end]
            counter[c] += 1

            if len(counter) > k:
                while start < len(s) and len(counter) > k:
                    counter[s[start]] -= 1

                    if counter[s[start]] == 0:
                        counter.pop(s[start])

                    start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
