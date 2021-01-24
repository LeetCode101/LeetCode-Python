import unittest
from leetcode.algorithms.p1095_find_in_mountain_array \
    import Solution, MountainArray


class TestFindInMountainArray(unittest.TestCase):
    def test_find_in_mountain_array(self):
        solution = Solution()

        self.assertEqual(2, solution.findInMountainArray(
            2, MountainArray([0, 1, 2, 1])))
        self.assertEqual(2, solution.findInMountainArray(
            3, MountainArray([1, 2, 3, 4, 5, 3, 1])))
        self.assertEqual(-1, solution.findInMountainArray(
            3, MountainArray([0, 1, 2, 4, 2, 1])))
