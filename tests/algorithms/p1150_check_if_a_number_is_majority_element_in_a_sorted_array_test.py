import unittest
from leetcode.algorithms \
    .p1150_check_if_a_number_is_majority_element_in_a_sorted_array \
    import Solution


class TestCheckIfANumberIsMajorityElementInASortedArray(unittest.TestCase):
    def test_check_if_a_number_is_majority_element_in_a_sorted_array(self):
        solution = Solution()

        self.assertFalse(solution.isMajorityElement([1], 2))
        self.assertFalse(solution.isMajorityElement([1, 2, 2], 1))
        self.assertTrue(solution.isMajorityElement(
            [2, 4, 5, 5, 5, 5, 5, 6, 6], 5))
        self.assertFalse(solution.isMajorityElement([10, 100, 101, 101], 101))
