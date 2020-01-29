import unittest
from leetcode.algorithms.p0443_string_compression import Solution


class TestStringCompression(unittest.TestCase):
    def test_string_compression(self):
        solution = Solution()
        expected_chars = ['a', '2', 'b', '2', 'c', '3']
        chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
        length = solution.compress(chars)

        self.assertEqual(6, length)
        self.assertListEqual(expected_chars, chars[:length])
