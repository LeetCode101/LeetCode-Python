import unittest
from leetcode.algorithms.p0556_next_greater_element_iii import Solution


class TestNextGreaterElement(unittest.TestCase):
    def test_next_greater_element(self):
        solution = Solution()

        self.assertEqual(234161457, solution.nextGreaterElement(234157641))
        self.assertEqual(21, solution.nextGreaterElement(12))
        self.assertEqual(-1, solution.nextGreaterElement(21))
