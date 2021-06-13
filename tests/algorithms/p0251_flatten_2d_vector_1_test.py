import unittest
from leetcode.algorithms.p0251_flatten_2d_vector_1 import Vector2D


class TestFlatten2DVector(unittest.TestCase):
    def test_flatten_2_d_vector(self):
        vector1 = Vector2D([[1, 2], [3], [4]])
        vector2 = Vector2D([[3], []])

        self.assertEqual(1, vector1.next())
        self.assertEqual(2, vector1.next())
        self.assertEqual(3, vector1.next())
        self.assertTrue(vector1.hasNext())
        self.assertEqual(4, vector1.next())
        self.assertFalse(vector1.hasNext())
        self.assertEqual(3, vector2.next())
        self.assertFalse(vector2.hasNext())
