import unittest
from leetcode.algorithms.p0503_next_greater_element_ii import Solution


class TestNextGreaterElement(unittest.TestCase):
    def test_next_greater_element(self):
        solution = Solution()

        self.assertListEqual([2, -1, 2], solution.nextGreaterElements(
            [1, 2, 1]))
        self.assertListEqual([2, 3, 4, -1, 4], solution.nextGreaterElements(
            [1, 2, 3, 4, 3]))
