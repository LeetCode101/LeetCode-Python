import unittest
from leetcode.algorithms.p0406_queue_reconstruction_by_height import Solution


class TestQueueReconstructionByHeight(unittest.TestCase):
    def test_queue_reconstruction_by_height(self):
        solution = Solution()

        self.assertListEqual(
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
            solution.reconstructQueue(
                [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
