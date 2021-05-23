import sys
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapping = {}
        both_likes = []
        min_sum = sys.maxsize

        for i, restaurant in enumerate(list1):
            mapping[restaurant] = i

        for i, restaurant in enumerate(list2):
            if restaurant in mapping:
                score = mapping[restaurant] + i

                if score == min_sum:
                    both_likes.append(restaurant)
                elif score < min_sum:
                    min_sum = score
                    both_likes = [restaurant]

        return both_likes
