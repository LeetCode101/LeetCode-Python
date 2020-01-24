from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sums = []

        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break

            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            low, high = i + 1, len(nums) - 1

            while low < high:
                if nums[low] + nums[high] == target:
                    sums.append([-target, nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1

                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target:
                    low += 1
                else:
                    high -= 1

        return sums
