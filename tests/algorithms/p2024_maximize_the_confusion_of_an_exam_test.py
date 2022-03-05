import unittest
from leetcode.algorithms.p2024_maximize_the_confusion_of_an_exam \
    import Solution


class TestMaximizeTheConfusionOfAnExam(unittest.TestCase):
    def test_maximize_the_confusion_of_an_exam(self):
        solution = Solution()

        self.assertEqual(4, solution.maxConsecutiveAnswers('TTFF', 2))
        self.assertEqual(3, solution.maxConsecutiveAnswers('TFFT', 1))
        self.assertEqual(5, solution.maxConsecutiveAnswers('TTFTTFTT', 1))
