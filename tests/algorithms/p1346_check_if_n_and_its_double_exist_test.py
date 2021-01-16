import unittest
from leetcode.algorithms.p1346_check_if_n_and_its_double_exist import Solution


class TestCheckIfNAndItsDoubleExist(unittest.TestCase):
    def test_check_if_n_and_its_double_exist(self):
        solution = Solution()

        self.assertTrue(solution.checkIfExist([10, 2, 5, 3]))
        self.assertFalse(solution.checkIfExist([3, 1, 7, 11]))
