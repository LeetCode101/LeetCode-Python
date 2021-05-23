import unittest
from leetcode.algorithms.p0771_jewels_and_stones import Solution


class TestJewelsAndStones(unittest.TestCase):
    def test_jewels_and_stones(self):
        solution = Solution()

        self.assertEqual(3, solution.numJewelsInStones('aA', 'aAAbbbb'))
        self.assertEqual(0, solution.numJewelsInStones('z', 'ZZ'))
