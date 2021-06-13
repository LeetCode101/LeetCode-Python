import unittest
from leetcode.algorithms.p0251_flatten_2d_vector_2 import Vector2D


class TestFlatten2DVector(unittest.TestCase):
    def test_flatten_2_d_vector(self):
        vector = Vector2D([[1, 2], [3], [4]])

        self.assertEqual(1, vector.next())
        self.assertEqual(2, vector.next())
        self.assertEqual(3, vector.next())
        self.assertTrue(vector.hasNext())
        self.assertEqual(4, vector.next())
        self.assertFalse(vector.hasNext())
