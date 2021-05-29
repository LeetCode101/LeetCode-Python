class TrieNode:
    def __init__(self):
        self.count = 0
        self.end = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()

            current = current.children[c]
            current.count += 1

        current.end += 1

    def countWordsEqualTo(self, word: str) -> int:
        current = self.root

        for c in word:
            if c not in current.children:
                return 0

            current = current.children[c]

        return current.end

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.root

        for c in prefix:
            if c not in current.children:
                return 0

            current = current.children[c]

        return current.count

    def erase(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                return

            prev = current
            current = current.children[c]
            current.count -= 1

            if current.count == 0:
                prev.children.pop(c)

        current.end -= 1
