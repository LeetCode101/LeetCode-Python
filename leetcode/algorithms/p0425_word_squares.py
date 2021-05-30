from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        self.word = ''


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words or not words[0]:
            return []

        root = TrieNode()
        result = []

        for word in words:
            self._insert(root, word)

        self._word_squares(root, len(words[0]), [], result)

        return result

    def _insert(self, root, word):
        current = root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end_of_word = True
        current.word = word

    def _search_prefix(self, root, prefix, candidates):
        current = root

        if current.end_of_word:
            candidates.append(current.word)

            return

        for c in prefix:
            if c not in current.children:
                return

            current = current.children[c]

        for child in current.children.values():
            self._search_prefix(child, '', candidates)

    def _word_squares(self, root, size, words, result):
        if len(words) == size:
            result.append(words)

            return

        candidates = []
        prefix = ''.join([word[len(words)] for word in words])

        self._search_prefix(root, prefix, candidates)

        for candidate in candidates:
            self._word_squares(root, size, words + [candidate], result)
