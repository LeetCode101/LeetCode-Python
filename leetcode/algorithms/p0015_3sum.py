from typing import List


# Time Limit Exceeded!
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lists = []

        for i, value in enumerate(nums):
            two_sums = self.two_sum(nums, i, -value)

            if two_sums:
                three_sums = []

                for two_sum in two_sums:
                    three_sums.append([nums[j] for j in sorted([i] + two_sum)])

                for three_sum in three_sums:
                    if not self.has_three_sum(lists, three_sum):
                        lists.append(three_sum)

        return lists

    def two_sum(self, nums: List[int], current_index: int, target: int) \
            -> List[List[int]]:
        mapping = {}
        two_sums = []

        for i, value in enumerate(nums):
            if i == current_index:
                continue

            if target - value in mapping:
                two_sums.append([mapping[target - value], i])
            else:
                mapping[value] = i

        return two_sums

    def has_three_sum(
            self, three_sums: List[List[int]], three_sum: List[int]) -> bool:
        for sum in three_sums:
            if sorted(sum) == sorted(three_sum):
                return True

        return False
