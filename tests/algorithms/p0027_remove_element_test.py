import unittest
from leetcode.algorithms.p0027_remove_element import Solution


class TestRemoveElement(unittest.TestCase):
    def test_remove_element(self):
        solution = Solution()

        self.assertEqual(2, solution.removeElement([3, 2, 2, 3], 3))
