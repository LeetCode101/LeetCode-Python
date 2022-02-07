import unittest
from leetcode.algorithms.p1376_time_needed_to_inform_all_employees_3 \
    import Solution


class TestTimeNeededToInformAllEmployees(unittest.TestCase):
    def test_time_needed_to_inform_all_employees(self):
        solution = Solution()

        self.assertEqual(1, solution.numOfMinutes(
            6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
