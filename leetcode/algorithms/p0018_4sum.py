from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        sums = []

        for i in range(len(nums) - 3):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j - 1 >= i + 1 and nums[j] == nums[j - 1]:
                    continue

                k = target - nums[i] - nums[j]
                low, high = j + 1, len(nums) - 1

                while low < high:
                    if nums[low] + nums[high] == k:
                        sums.append([nums[i], nums[j], nums[low], nums[high]])

                        while low < high and nums[low] == nums[low + 1]:
                            low += 1

                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1

                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < k:
                        low += 1
                    else:
                        high -= 1

        return sums
