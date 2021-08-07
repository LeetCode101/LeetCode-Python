import collections
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = collections.defaultdict(int)

        for i, n in enumerate(nums):
            if n != 0:
                self.non_zeros[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0

        for key, value in self.non_zeros.items():
            if key in vec.non_zeros:
                product += value * vec.non_zeros[key]

        return product
