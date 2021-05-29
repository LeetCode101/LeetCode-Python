from typing import List, Set
from leetcode.algorithms.p0208_implement_trie_1 import Trie


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
                self._dfs(row, column, board, '', trie, result, visited)

        return list(result)

    def _dfs(self, row: int, column: int, board: List[List[str]], word: str,
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

        self._dfs(row - 1, column, board, word, trie, result, visited)
        self._dfs(row + 1, column, board, word, trie, result, visited)
        self._dfs(row, column - 1, board, word, trie, result, visited)
        self._dfs(row, column + 1, board, word, trie, result, visited)

        visited[row][column] = False
