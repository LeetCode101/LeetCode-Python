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
        rows, columns = len(board), len(board[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        for word in words:
            trie.insert(word)

        for row in range(rows):
            for column in range(columns):
                self.dfs(row, column, board, '', trie, result, visited)

        return list(result)

    def dfs(self, row: int, column: int, board: List[List[str]], word: str,
            trie: Trie, result: Set[str],
            visited: List[List[bool]]) -> None:
        if not (0 <= row < len(board) and 0 <= column < len(board[0])):
            return

        if visited[row][column]:
            return

        word += board[row][column]

        if not trie.startsWith(word):
            return

        if trie.search(word):
            result.add(word)

        visited[row][column] = True

        self.dfs(row - 1, column, board, word, trie, result, visited)
        self.dfs(row + 1, column, board, word, trie, result, visited)
        self.dfs(row, column - 1, board, word, trie, result, visited)
        self.dfs(row, column + 1, board, word, trie, result, visited)

        visited[row][column] = False
