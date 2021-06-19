from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        sum_so_far = 0
        count = 0

        for n in nums:
            sum_so_far += n
            rem = ((sum_so_far % k) + k) % k
            count += counts.get(rem, 0)
            counts[rem] = counts.get(rem, 0) + 1

        return count
