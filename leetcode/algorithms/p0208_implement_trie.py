class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            index = self.get_child_index(c)
            child = current.children[index]

            if not child:
                current.children[index] = TrieNode()

            current = current.children[index]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root

        for c in word:
            index = self.get_child_index(c)
            child = current.children[index]

            if not child:
                return False

            current = current.children[index]

        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for c in prefix:
            index = self.get_child_index(c)
            child = current.children[index]

            if not child:
                return False

            current = current.children[index]

        return True

    def get_child_index(self, c: str) -> int:
        return ord(c) - 97
