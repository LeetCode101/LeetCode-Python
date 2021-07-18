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

            if len(chars) > k:
                while start < len(s) and len(chars) > k:
                    counter[s[start]] -= 1

                    if counter[s[start]] == 0:
                        chars.remove(s[start])

                    start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
