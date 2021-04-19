import unittest
from leetcode.algorithms.p0797_all_paths_from_source_to_target_2 \
    import Solution


class TestAllPathsFromSourceToTarget(unittest.TestCase):
    def test_all_paths_from_source_to_target(self):
        solution = Solution()

        self.assertListEqual([], solution.allPathsSourceTarget([]))
        self.assertListEqual([[0, 1, 3], [0, 2, 3]],
                             sorted(solution.allPathsSourceTarget(
                                 [[1, 2], [3], [3], []])))
        self.assertListEqual(sorted([[0, 4], [0, 3, 4], [0, 1, 3, 4],
                                     [0, 1, 2, 3, 4], [0, 1, 4]]),
                             sorted(solution.allPathsSourceTarget(
                                 [[4, 3, 1], [3, 2, 4], [3], [4], []])))
