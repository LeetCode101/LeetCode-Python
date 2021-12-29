import collections


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counts = collections.defaultdict(int)

        for c in text:
            counts[c] += 1

        max_length = 0
        start, n = 0, len(text)

        while start < n:
            j = start
            c = text[start]

            while j < n and text[j] == c:
                j += 1

            k = j + 1

            while k < n and text[k] == c:
                k += 1

            current_length = k - start - 1 \
                if k - start - 1 == counts[c] else k - start
            max_length = max(max_length, current_length)
            start = j

        return max_length
