from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0
        mapping = {0: -1}

        for i, n in enumerate(nums):
            sum += n
            key = sum if k == 0 else sum % k

            if key in mapping:
                if i - mapping[key] >= 2:
                    return True
            else:
                mapping[key] = i

        return False
