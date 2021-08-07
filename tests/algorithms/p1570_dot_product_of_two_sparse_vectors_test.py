import unittest
from leetcode.algorithms.p1570_dot_product_of_two_sparse_vectors \
    import SparseVector


class TestDotProductOfTwoSparseVectors(unittest.TestCase):
    def test_dot_product_of_two_sparse_vectors(self):
        self.assertEqual(8, SparseVector([1, 0, 0, 2, 3]).dotProduct(
            SparseVector([0, 3, 0, 4, 0])))
        self.assertEqual(6, SparseVector([0, 1, 0, 0, 2, 0, 0]).dotProduct(
            SparseVector([1, 0, 0, 0, 3, 0, 4])))
