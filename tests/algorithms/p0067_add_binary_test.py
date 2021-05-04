import unittest
from leetcode.algorithms.p0067_add_binary import Solution


class TestAddBinary(unittest.TestCase):
    def test_add_binary(self):
        solution = Solution()

        self.assertEqual('10101', solution.addBinary('1010', '1011'))
