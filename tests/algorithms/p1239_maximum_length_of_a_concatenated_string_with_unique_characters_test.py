import unittest
from leetcode.algorithms\
    .p1239_maximum_length_of_a_concatenated_string_with_unique_characters \
    import Solution


class TestMaximumLengthOfAConcatenatedStringWithUniqueCharacters(
        unittest.TestCase):
    def test_maximum_length_of_a_concatenated_string_with_unique_characters(
            self):
        solution = Solution()

        self.assertEqual(
            16, solution.maxLength(['jnfbyktlrqumowxd', 'mvhgcpxnjzrdei']))
        self.assertEqual(4, solution.maxLength(['un', 'iq', 'ue']))
        self.assertEqual(6, solution.maxLength(['cha', 'r', 'act', 'ers']))
        self.assertEqual(
            26, solution.maxLength(['abcdefghijklmnopqrstuvwxyz']))
