import unittest
from leetcode.algorithms.p0093_restore_ip_addresses import Solution


class TestRestoreIPAddresses(unittest.TestCase):
    def test_restore_ip_addresses(self):
        solution = Solution()

        self.assertListEqual(['255.255.11.135', '255.255.111.35'],
                             solution.restoreIpAddresses('25525511135'))
        self.assertListEqual(['0.0.0.0'],
                             solution.restoreIpAddresses('0000'))
        self.assertListEqual(
            ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3'],
            solution.restoreIpAddresses('101023'))
