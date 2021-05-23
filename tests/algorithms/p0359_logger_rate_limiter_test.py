import unittest
from leetcode.algorithms.p0359_logger_rate_limiter import Logger


class TestLoggerRateLimiter(unittest.TestCase):
    def test_logger_rate_limiter(self):
        logger = Logger()

        self.assertTrue(logger.shouldPrintMessage(1, 'foo'))
        self.assertTrue(logger.shouldPrintMessage(2, 'bar'))
        self.assertFalse(logger.shouldPrintMessage(3, 'foo'))
        self.assertFalse(logger.shouldPrintMessage(8, 'bar'))
        self.assertFalse(logger.shouldPrintMessage(10, 'foo'))
        self.assertTrue(logger.shouldPrintMessage(11, 'foo'))
