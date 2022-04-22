import unittest
from leetcode.algorithms.p0583_delete_operation_for_two_strings import Solution


class TestDeleteOperationForTwoStrings(unittest.TestCase):
    def test_delete_operation_for_two_strings(self):
        solution = Solution()

        self.assertEqual(2, solution.minDistance('sea', 'eat'))
        self.assertEqual(4, solution.minDistance('leetcode', 'etco'))
