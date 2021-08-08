import unittest
from leetcode.algorithms.p0809_expressive_words import Solution


class TestExpressiveWords(unittest.TestCase):
    def test_expressive_words(self):
        solution = Solution()

        self.assertEqual(0, solution.expressiveWords('abcd', ['abc']))
        self.assertEqual(1, solution.expressiveWords('heeellooo',
                                                     ['hello', 'hi', 'helo']))
        self.assertEqual(3, solution.expressiveWords('zzzzzyyyyy',
                                                     ['zzyy', 'zy', 'zyy']))
