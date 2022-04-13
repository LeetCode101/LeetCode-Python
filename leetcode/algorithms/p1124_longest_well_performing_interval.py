from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_length = 0
        score = 0
        seen_scores = {}

        for i, hour in enumerate(hours):
            if hour > 8:
                score += 1
            else:
                score -= 1

            if score > 0:
                max_length = i + 1

            if score not in seen_scores:
                seen_scores[score] = i

            if score - 1 in seen_scores:
                max_length = max(max_length, i - seen_scores[score - 1])

        return max_length
