from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]

        self._divide(nums, count)

        return count[0]

    def _divide(self, nums, count):
        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2
        left = self._divide(nums[:middle], count)
        right = self._divide(nums[middle:], count)

        return self._conquer(left, right, count)

    def _conquer(self, left, right, count):
        sorted_nums = []
        i = j = 0

        count[0] += self._count(left, right)

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_nums.append(left[i])
                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1

        sorted_nums.extend(left[i:] or right[j:])

        return sorted_nums

    def _count(self, left, right):
        i = j = 0
        count = 0

        while i < len(left) and j < len(right):
            if left[i] / 2 > right[j]:
                count += len(left) - i
                j += 1
            else:
                i += 1

        return count
