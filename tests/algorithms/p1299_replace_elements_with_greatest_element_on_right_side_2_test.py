import unittest
from leetcode.algorithms\
    .p1299_replace_elements_with_greatest_element_on_right_side_2 \
    import Solution


class TestReplaceElementsWithGreatestElementOnRightSide(unittest.TestCase):
    def test_replace_elements_with_greatest_element_on_right_side(self):
        solution = Solution()

        self.assertListEqual([18, 6, 6, 6, 1, -1], solution.replaceElements(
            [17, 18, 5, 4, 6, 1]))
