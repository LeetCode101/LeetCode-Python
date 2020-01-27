from typing import List, Set


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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        result = set()

        for word in words:
            trie.insert(word)

        for row in range(len(board)):
            for column in range(len(board[0])):
                if trie.startsWith(board[row][column]):
                    self.dfs(row, column, board, '', trie.root, result)

        return list(result)

    def dfs(self, row: int, column: int, board: List[List[str]], word: str,
            root: TrieNode, result: Set[str]) -> None:
        word += board[row][column]
        node = root.children[ord(board[row][column]) - 97]

        if node.is_end_of_word:
            result.add(word)

        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        temp, board[row][column] = board[row][column], '@'

        for i in range(4):
            x, y = row + dx[i], column + dy[i]

            if 0 <= x < len(board) and 0 <= y < len(board[0]) \
                    and board[x][y] != '@' \
                    and node.children[ord(board[x][y]) - 97]:
                self.dfs(x, y, board, word, node, result)

        board[row][column] = temp
