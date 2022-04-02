import collections
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        flat_nums = []
        counter = collections.defaultdict(int)

        for i, num in enumerate(nums):
            for n in num:
                flat_nums.append((n, i))

        flat_nums.sort(key=lambda x: x[0])
        result = []
        left = 0

        for right, n in enumerate(flat_nums):
            counter[n[1]] += 1

            while len(counter) == k:
                if not result or flat_nums[right][0] - flat_nums[left][0] \
                        < result[1] - result[0]:
                    result = [flat_nums[left][0], flat_nums[right][0]]

                counter[flat_nums[left][1]] -= 1

                if counter[flat_nums[left][1]] == 0:
                    counter.pop(flat_nums[left][1])

                left += 1

        return result
