import unittest
from leetcode.algorithms.p0378_kth_smallest_element_in_a_sorted_matrix_1 \
    import Solution


class TestKthSmallestElementInASortedMatrix(unittest.TestCase):
    def test_kth_smallest_element_in_a_sorted_matrix(self):
        solution = Solution()

        self.assertEqual(13, solution.kthSmallest(
            [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
