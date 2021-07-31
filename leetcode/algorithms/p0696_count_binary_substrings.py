class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_count = 0
        current_count = 1
        count = 0

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                count += min(prev_count, current_count)
                prev_count, current_count = current_count, 1
            else:
                current_count += 1

        count += min(prev_count, current_count)

        return count
