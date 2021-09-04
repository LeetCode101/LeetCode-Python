import unittest
from leetcode.algorithms.p0769_max_chunks_to_make_sorted_1 import Solution


class TestMaxChunksToMakeSorted(unittest.TestCase):
    def test_max_chunks_to_make_sorted(self):
        solution = Solution()

        self.assertEqual(2, solution.maxChunksToSorted([1, 2, 0, 3]))
        self.assertEqual(1, solution.maxChunksToSorted([4, 3, 2, 1, 0]))
        self.assertEqual(4, solution.maxChunksToSorted([1, 0, 2, 3, 4]))
