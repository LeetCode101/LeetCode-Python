import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = set()
        counter = collections.defaultdict(int)
        start = 0
        max_length = 0

        for end in range(len(s)):
            c = s[end]
            chars.add(c)
            counter[c] += 1

            if len(chars) <= k:
                max_length = max(max_length, end - start + 1)
            else:
                while counter[c] > 0:
                    if s[start] == c:
                        counter[c] -= 1

                    start += 1

                chars.remove(c)

        return max_length
