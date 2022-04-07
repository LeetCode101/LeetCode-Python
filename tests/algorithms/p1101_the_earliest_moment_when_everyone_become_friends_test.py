import unittest
from leetcode.algorithms \
    .p1101_the_earliest_moment_when_everyone_become_friends import Solution


class TestTheEarliestMomentWhenEveryoneBecomeFriends(unittest.TestCase):
    def test_the_earliest_moment_when_everyone_become_friends(self):
        solution = Solution()

        self.assertEqual(20190301, solution.earliestAcq(
            [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3],
             [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
             [20190312, 1, 2], [20190322, 4, 5]], 6))
        self.assertEqual(3, solution.earliestAcq(
            [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4))
        self.assertEqual(-1, solution.earliestAcq(
            [[9, 0, 3], [0, 2, 7], [12, 3, 1], [5, 5, 2], [3, 4, 5],
             [1, 5, 0], [6, 2, 4], [2, 5, 3], [7, 7, 3]], 8))
