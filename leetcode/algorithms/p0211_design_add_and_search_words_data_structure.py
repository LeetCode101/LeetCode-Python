class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]

        current.end_of_word = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word, node):
        current = node

        for i, c in enumerate(word):
            child = current.children.get(c, None)

            if c == '.':
                for key, current_child in current.children.items():
                    if self._search(word[i + 1:], current_child):
                        return True

                return False
            elif not child:
                return False
            else:
                current = child

        return current.end_of_word
