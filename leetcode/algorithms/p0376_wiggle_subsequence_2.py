from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        postive = [0] * n
        negative = [0] * n
        postive[0] = 1
        negative[0] = 1
        max_length = 1

        for i in range(1, n):
            postive[i] = postive[i - 1]
            negative[i] = negative[i - 1]
            diff = nums[i] - nums[i - 1]

            if diff < 0:
                negative[i] = max(negative[i], 1 + postive[i])
            elif diff > 0:
                postive[i] = max(postive[i], 1 + negative[i])

            max_length = max(postive[i], negative[i], max_length)

        return max_length
