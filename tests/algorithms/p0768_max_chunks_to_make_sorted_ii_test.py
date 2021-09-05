import unittest
from leetcode.algorithms.p0768_max_chunks_to_make_sorted_ii import Solution


class TestMaxChunksToMakeSorted(unittest.TestCase):
    def test_max_chunks_to_make_sorted(self):
        solution = Solution()

        self.assertEqual(1, solution.maxChunksToSorted([5, 4, 3, 2, 1]))
        self.assertEqual(4, solution.maxChunksToSorted([2, 1, 3, 4, 4]))
