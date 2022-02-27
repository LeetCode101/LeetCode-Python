import unittest
from leetcode.algorithms.p0917_reverse_only_letters import Solution


class TestReverseOnlyLetters(unittest.TestCase):
    def test_reverse_only_letters(self):
        solution = Solution()

        self.assertEqual('Qedo1ct-eeLg=ntse-T!',
                         solution.reverseOnlyLetters('Test1ng-Leet=code-Q!'))
