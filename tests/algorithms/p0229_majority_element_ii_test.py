import unittest
from leetcode.algorithms.p0229_majority_element_ii import Solution


class TestMajorityElement(unittest.TestCase):
    def test_majority_element(self):
        solution = Solution()

        self.assertListEqual([3], solution.majorityElement([3, 2, 3]))
        self.assertListEqual([1, 2], solution.majorityElement([1, 2]))
