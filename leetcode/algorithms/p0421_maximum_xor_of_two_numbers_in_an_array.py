import sys
from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        self.value = 0


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        max_xor = -sys.maxsize

        for n in nums:
            bits = (bin(n)[2:]).zfill(31)

            self._insert(root, bits, n)

            max_xor = max(max_xor, self._search(root, bits, n))

        return max_xor

    def _insert(self, root, bits, value):
        current = root

        for bit in bits:
            if bit not in current.children:
                current.children[bit] = TrieNode()

            current = current.children[bit]

        current.end_of_word = True
        current.value = value

    def _search(self, root, bits, target):
        current = root

        for bit in bits:
            if bit == '1' and '0' in current.children:
                current = current.children['0']
            elif bit == '0' and '1' in current.children:
                current = current.children['1']
            elif bit in current.children:
                current = current.children[bit]
            else:
                break

        return target ^ current.value
