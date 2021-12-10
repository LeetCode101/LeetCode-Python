import unittest
from leetcode.algorithms.p0721_accounts_merge_2 import Solution


class TestAccountsMerge(unittest.TestCase):
    def test_accounts_merge(self):
        solution = Solution()

        self.assertListEqual(
            [['John', 'john00@mail.com', 'john_newyork@mail.com',
              'johnsmith@mail.com'],
             ['John', 'johnnybravo@mail.com'], ['Mary', 'mary@mail.com']],
            sorted(solution.accountsMerge(
                [['John', 'johnsmith@mail.com', 'john_newyork@mail.com'],
                 ['John', 'johnsmith@mail.com', 'john00@mail.com'],
                 ['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com']]),
                key=lambda x: (x[0], x[1])))
