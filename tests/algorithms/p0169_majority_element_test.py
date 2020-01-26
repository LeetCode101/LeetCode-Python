import unittest
from leetcode.algorithms.p0169_majority_element import Solution


class TestMajorityElement(unittest.TestCase):
    def test_majority_element(self):
        solution = Solution()

        self.assertEqual(3, solution.majorityElement([3, 2, 3]))
        self.assertEqual(2, solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
