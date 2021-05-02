import unittest
from leetcode.algorithms.p0880_decoded_string_at_index_2 import Solution


class TestDecodedStringAtIndex(unittest.TestCase):
    def test_decoded_string_at_index(self):
        solution = Solution()

        self.assertEqual('o', solution.decodeAtIndex('leet2code3', 10))
        self.assertEqual('h', solution.decodeAtIndex('ha22', 5))
