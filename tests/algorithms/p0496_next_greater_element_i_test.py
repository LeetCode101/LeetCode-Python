import unittest
from leetcode.algorithms.p0496_next_greater_element_i import Solution


class TestNextGreaterElement(unittest.TestCase):
    def test_next_greater_element(self):
        solution = Solution()

        self.assertListEqual([-1, 3, -1], solution.nextGreaterElement(
            [4, 1, 2], [1, 3, 4, 2]))
        self.assertListEqual([3, -1], solution.nextGreaterElement(
            [2, 4], [1, 2, 3, 4]))
