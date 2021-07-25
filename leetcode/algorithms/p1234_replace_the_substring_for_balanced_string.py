import collections


class Solution:
    def balancedString(self, s: str) -> int:
        counter = collections.Counter(s)
        n = len(s)
        count = n
        start = 0

        for end, c in enumerate(s):
            counter[c] -= 1

            while start < n and all(n // 4 >= counter[c] for c in 'QWER'):
                count = min(count, end - start + 1)
                counter[s[start]] += 1
                start += 1

        return count
