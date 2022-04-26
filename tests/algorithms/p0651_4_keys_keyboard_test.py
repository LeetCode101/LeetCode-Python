import unittest
from leetcode.algorithms.p0651_4_keys_keyboard import Solution


class Test4KeysKeyboard(unittest.TestCase):
    def test_4_keys_keyboard(self):
        solution = Solution()

        self.assertEqual(3, solution.maxA(3))
        self.assertEqual(9, solution.maxA(7))
