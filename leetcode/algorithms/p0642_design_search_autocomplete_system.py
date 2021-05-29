from typing import List


class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
        self.searched_count = 0


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.current_sentence = ''
        self.root = TrieNode()

        for i, sentence in enumerate(sentences):
            self._insert(sentence, times[i])

    def input(self, c: str) -> List[str]:
        if c == '#':
            self._insert(self.current_sentence, 1)
            self.current_sentence = ''

            return []

        self.current_sentence += c

        return self._search(self.current_sentence)

    def _search(self, sentence):
        current = self.root
        path = ''
        paths = []

        for c in sentence:
            if c not in current.children:
                return []

            path += c
            current = current.children[c]

        self._find_all(current, path, paths)

        paths.sort(key=lambda x: (-x[1], x[0]))

        return [x[0] for x in paths[:3]]

    def _find_all(self, node, path_so_far, paths):
        if node.end_of_word:
            paths.append((path_so_far, node.searched_count))

        for key, child in node.children.items():
            self._find_all(child, path_so_far + key, paths)

    def _insert(self, sentence, count):
        current = self.root

        for c in sentence:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end_of_word = True
        current.searched_count += count
