from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1

        if letters[-1] <= target:
            return letters[0]

        while low <= high:
            middle = low + (high - low) // 2
            letter = letters[middle]

            if letter <= target:
                low += 1
            else:
                high = middle - 1

        return letters[low]
