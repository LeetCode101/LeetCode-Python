import unittest
from leetcode.algorithms.p0744_find_smallest_letter_greater_than_target \
    import Solution


class TestFindSmallestLetterGreaterThanTarget(unittest.TestCase):
    def test_p0744_find_smallest_letter_greater_than_target(self):
        solution = Solution()

        self.assertEqual('c', solution.nextGreatestLetter(
            ['c', 'f', 'j'], 'a'))
        self.assertEqual('c', solution.nextGreatestLetter(
            ['c', 'f', 'j'], 'k'))
