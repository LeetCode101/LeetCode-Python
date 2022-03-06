import unittest
from leetcode.algorithms \
    .p2064_minimized_maximum_of_products_distributed_to_any_store \
    import Solution


class TestMinimizedMaximumOfProductsDistributedToAnyStore(unittest.TestCase):
    def test_minimized_maximum_of_products_distributed_to_any_store(self):
        solution = Solution()

        self.assertEqual(3, solution.minimizedMaximum(6, [11, 6]))
        self.assertEqual(5, solution.minimizedMaximum(7, [15, 10, 10]))
