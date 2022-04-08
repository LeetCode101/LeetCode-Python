from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []

        self._search(nums, 0, [], result)

        return result

    def _search(self, nums, start, sequence, result):
        if len(sequence) >= 2:
            result.append(sequence[:])

        if start == len(nums):
            return

        visited = set()

        for i in range(start, len(nums)):
            if (sequence and sequence[-1] > nums[i]) or nums[i] in visited:
                continue

            sequence.append(nums[i])
            visited.add(nums[i])
            self._search(nums, i + 1, sequence, result)
            sequence.pop()
