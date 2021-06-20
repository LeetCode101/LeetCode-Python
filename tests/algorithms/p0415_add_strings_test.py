import unittest
from leetcode.algorithms.p0415_add_strings import Solution


class TestAddStrings(unittest.TestCase):
    def test_add_strings(self):
        solution = Solution()

        self.assertEqual('533', solution.addStrings('456', '77'))
