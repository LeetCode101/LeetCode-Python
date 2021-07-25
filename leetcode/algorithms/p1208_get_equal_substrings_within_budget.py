class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        cost_so_far = 0
        max_length = 0

        for end in range(len(s)):
            cost_so_far += abs(ord(s[end]) - ord(t[end]))

            if cost_so_far > maxCost:
                cost_so_far -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length
