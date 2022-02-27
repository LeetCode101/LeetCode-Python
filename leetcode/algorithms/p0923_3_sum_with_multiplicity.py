import collections
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = collections.defaultdict(int)
        result = 0
        mod = 1000000007

        for i, n in enumerate(arr):
            result = (result + counter[target - n]) % mod

            for j in range(i):
                two_sum = n + arr[j]
                counter[two_sum] += 1

        return result
