import unittest
from leetcode.algorithms.p0702_search_in_a_sorted_array_of_unknown_size_1 \
    import Solution, ArrayReader


class TestSearchInASortedArrayOfUnknownSize(unittest.TestCase):
    def test_search_in_a_sorted_array_of_unknown_size(self):
        solution = Solution()
        array_reader = ArrayReader()

        self.assertEqual(4, solution.search(array_reader, 9))
        self.assertEqual(-1, solution.search(array_reader, 2))
