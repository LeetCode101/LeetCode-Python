from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            middle = low + (high - low) // 2

            if nums[middle] == target:
                return True
            elif nums[middle] > nums[low]:
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
            elif nums[middle] < nums[low]:
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
            else:
                low += 1

        return False
