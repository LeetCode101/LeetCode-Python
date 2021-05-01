import unittest
from leetcode.algorithms.p0241_different_ways_to_add_parentheses \
    import Solution


class TestDifferentWaysToAddParentheses(unittest.TestCase):
    def test_different_ways_to_add_parentheses(self):
        solution = Solution()

        self.assertEqual([2], solution.diffWaysToCompute('1+1'))
        self.assertListEqual(sorted([-34, -14, -10, -10, 10]),
                             sorted(solution.diffWaysToCompute('2*3-4*5')))
