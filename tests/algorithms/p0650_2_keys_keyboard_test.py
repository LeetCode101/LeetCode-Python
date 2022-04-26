import unittest
from leetcode.algorithms.p0650_2_keys_keyboard import Solution


class Test2KeysKeyboard(unittest.TestCase):
    def test_2_keys_keyboard(self):
        solution = Solution()

        self.assertEqual(3, solution.minSteps(3))
        self.assertEqual(4, solution.minSteps(4))
        self.assertEqual(0, solution.minSteps(1))
