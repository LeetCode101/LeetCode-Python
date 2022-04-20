import unittest
from leetcode.algorithms.p2140_solving_questions_with_brainpower \
    import Solution


class TestSolvingQuestionsWithBrainpower(unittest.TestCase):
    def test_solving_questions_with_brainpower(self):
        solution = Solution()

        self.assertEqual(5, solution.mostPoints(
            [[3, 2], [4, 3], [4, 4], [2, 5]]))
        self.assertEqual(7, solution.mostPoints(
            [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))
