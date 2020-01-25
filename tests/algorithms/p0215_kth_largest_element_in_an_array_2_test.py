import unittest
from leetcode.algorithms.p0215_kth_largest_element_in_an_array_2 \
    import Solution


class TestKthLargestElementInAnArray(unittest.TestCase):
    def test_kth_largest_element_in_an_array(self):
        solution = Solution()

        self.assertEqual(5, solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(
            4, solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
