import unittest
from leetcode.algorithms.p0249_group_shifted_strings import Solution


class TestGroupShiftedStrings(unittest.TestCase):
    def test_group_shifted_strings(self):
        solution = Solution()

        self.assertListEqual(
            sorted([['acef'], ['a', 'z'],
                    ['abc', 'bcd', 'xyz'], ['az', 'ba']]),
            sorted(solution.groupStrings(['abc', 'bcd', 'acef',
                                          'xyz', 'az', 'ba', 'a', 'z'])))
