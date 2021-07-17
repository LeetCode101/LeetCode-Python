import sys
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_window_length = len(cardPoints) - k
        start, end = 0, 0
        min_score = sys.maxsize
        sum_so_far = 0
        total_sum = sum(cardPoints)

        if max_window_length <= 0:
            return total_sum

        for end in range(len(cardPoints)):
            sum_so_far += cardPoints[end]
            current_window_length = end - start + 1

            if current_window_length < max_window_length:
                continue
            elif current_window_length > max_window_length:
                sum_so_far -= cardPoints[start]
                start += 1

            min_score = min(min_score, sum_so_far)

        return total_sum - min_score
