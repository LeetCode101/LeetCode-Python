import unittest
from leetcode.algorithms.p0315_count_of_smaller_numbers_after_self_1 \
    import Solution


class TestCountOfSmallerNumbersAfterSelf(unittest.TestCase):
    def test_count_of_smaller_numbers_after_self(self):
        solution = Solution()

        self.assertListEqual([], solution.countSmaller([]))
        self.assertListEqual([2, 1, 1, 0],
                             solution.countSmaller([5, 2, 6, 1]))
