from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        self._divide(list(enumerate(nums)), result)

        return result

    def _divide(self, nums, result):
        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2
        left = self._divide(nums[:middle], result)
        right = self._divide(nums[middle:], result)

        return self._conquer(left, right, result)

    def _conquer(self, left, right, result):
        sorted_nums = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                sorted_nums.append(left[i])
                result[left[i][0]] += len(right) - j
                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1

        sorted_nums.extend(left[i:] or right[j:])

        return sorted_nums
