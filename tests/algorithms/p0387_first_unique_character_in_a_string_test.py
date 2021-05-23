import unittest
from leetcode.algorithms.p0387_first_unique_character_in_a_string \
    import Solution


class TestFirstUniqueCharacterInAString(unittest.TestCase):
    def test_first_unique_character_in_a_string(self):
        solution = Solution()

        self.assertEqual(0, solution.firstUniqChar('leetcode'))
        self.assertEqual(2, solution.firstUniqChar('loveleetcode'))
        self.assertEqual(-1, solution.firstUniqChar('aabb'))
        self.assertEqual(0, solution.firstUniqChar('abc'))
