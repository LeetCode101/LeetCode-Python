import unittest
from leetcode.algorithms.p0953_verifying_an_alien_dictionary import Solution


class TestVerifyingAnAlienDictionary(unittest.TestCase):
    def test_verifying_an_alien_dictionary(self):
        solution = Solution()

        self.assertFalse(solution.isAlienSorted(
            ['leetcode', 'hello'], 'hlabcdefgijkmnopqrstuvwxyz'))
        self.assertTrue(solution.isAlienSorted(
            ['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'))
        self.assertFalse(solution.isAlienSorted(
            ['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz'))
