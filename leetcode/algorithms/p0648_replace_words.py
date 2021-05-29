from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        words = []

        for word in dictionary:
            self._insert(root, word)

        for word in sentence.split(' '):
            word_in_dictionary = self._search(root, word)

            if word_in_dictionary:
                words.append(word_in_dictionary)
            else:
                words.append(word)

        return ' '.join(words)

    def _insert(self, root, word: str) -> None:
        current = root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end_of_word = True

    def _search(self, root, word: str) -> str:
        current = root
        path = ''

        for c in word:
            if c not in current.children:
                return ''

            current = current.children[c]
            path += c

            if current.end_of_word:
                break

        return path if current.end_of_word else ''
