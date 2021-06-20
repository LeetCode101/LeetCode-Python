import unittest
from leetcode.algorithms.p1396_design_underground_system \
    import UndergroundSystem


class TestDesignUndergroundSystem(unittest.TestCase):
    def test_design_underground_system(self):
        underground_system = UndergroundSystem()
        underground_system.checkIn(45, 'Leyton', 3)
        underground_system.checkIn(32, 'Paradise', 8)
        underground_system.checkIn(27, 'Leyton', 10)
        underground_system.checkOut(45, 'Waterloo', 15)
        underground_system.checkOut(27, 'Waterloo', 20)
        underground_system.checkOut(32, 'Cambridge', 22)

        self.assertEqual(14, underground_system.getAverageTime(
            'Paradise', 'Cambridge'))
        self.assertEqual(11, underground_system.getAverageTime(
            'Leyton', 'Waterloo'))
