from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        self.index = -1
        self.positions = []


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []

        root = TrieNode()
        result = []

        for i, word in enumerate(words):
            self._insert(root, word, i)

        for i, word in enumerate(words):
            self._search(root, i, word, result)

        return result

    def _insert(self, root, word, index):
        current = root

        for i in range(len(word) - 1, -1, -1):
            c = word[i]

            if c not in current.children:
                current.children[c] = TrieNode()

            if self._is_palindrome(word, 0, i):
                current.positions.append(index)

            current = current.children[c]

        current.end_of_word = True
        current.index = index
        current.positions.append(index)

    def _search(self, root, index, word, result):
        current = root

        for j, c in enumerate(word):
            if current.end_of_word and current.index != index \
                    and self._is_palindrome(word, j, len(word) - 1):
                result.append([index, current.index])

            if c not in current.children:
                return

            current = current.children[c]

        for j in current.positions:
            if index != j:
                result.append([index, j])

    def _is_palindrome(self, word, low, high):
        while low < high:
            if word[low] != word[high]:
                return False

            low += 1
            high -= 1

        return True
