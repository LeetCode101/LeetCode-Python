from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            crush = set()

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if j > 1 and board[i][j] != 0 and \
                            board[i][j] == board[i][j - 1] == board[i][j - 2]:
                        crush.add((i, j))
                        crush.add((i, j - 1))
                        crush.add((i, j - 2))

                    if i > 1 and board[i][j] != 0 and \
                            board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        crush.add((i, j))
                        crush.add((i - 1, j))
                        crush.add((i - 2, j))

            if not crush:
                break

            for i, j in crush:
                board[i][j] = 0

            for j in range(len(board[0])):
                k = len(board) - 1

                for i in range(len(board) - 1, -1, -1):
                    if board[i][j] != 0:
                        board[k][j] = board[i][j]
                        k -= 1

                for i in range(k + 1):
                    board[i][j] = 0

        return board
