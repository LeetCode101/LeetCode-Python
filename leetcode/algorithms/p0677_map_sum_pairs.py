from typing import Tuple


class TrieNode:
    def __init__(self):
        self.path_sum = 0
        self.children = {}
        self.end_of_word = False
        self.word_value = 0


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        current = self.root
        exist, word_value = self._search(key)

        for c in key:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

            if exist:
                current.path_sum = current.path_sum - word_value + val
            else:
                current.path_sum += val

        current.end_of_word = True
        current.word_value = val

    def sum(self, prefix: str) -> int:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return 0

            current = current.children[c]

        return current.path_sum

    def _search(self, key: str) -> Tuple[bool, int]:
        current = self.root

        for c in key:
            if c not in current.children:
                return False, 0

            current = current.children[c]

        return current.end_of_word, current.word_value
