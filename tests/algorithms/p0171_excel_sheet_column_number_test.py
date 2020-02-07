import unittest
from leetcode.algorithms.p0171_excel_sheet_column_number import Solution


class TestExcelSheetColumnNumber(unittest.TestCase):
    def test_excel_sheet_column_number(self):
        solution = Solution()

        self.assertEqual(1, solution.titleToNumber('A'))
        self.assertEqual(28, solution.titleToNumber('AB'))
        self.assertEqual(701, solution.titleToNumber('ZY'))
