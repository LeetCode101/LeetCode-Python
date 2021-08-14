import unittest
from leetcode.algorithms.p0031_next_permutation import Solution


class TestNextPermutation(unittest.TestCase):
    def test_next_permutation(self):
        solution = Solution()
        list1 = [1, 2, 3]
        list2 = [3, 2, 1]

        solution.nextPermutation(list1)
        solution.nextPermutation(list2)

        self.assertListEqual([1, 3, 2], list1)
        self.assertListEqual([1, 2, 3], list2)
