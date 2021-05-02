import unittest
from leetcode.algorithms.p0271_encode_and_decode_strings import Codec


class TestEncodeAndDecodeStrings(unittest.TestCase):
    def test_encode_and_decode_strings(self):
        codec = Codec()

        self.assertListEqual(['Hello', 'World'],
                             codec.decode(codec.encode(['Hello', 'World'])))
