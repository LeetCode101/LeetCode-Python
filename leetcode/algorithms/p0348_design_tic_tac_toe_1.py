class TicTacToe:
    def __init__(self, n: int):
        self.board = [['' for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = 'X' if player == 1 else 'O'

        result = 0

        if player == 1:
            result = 1 if self._is_player_win(1, row, col) else 0
        elif player == 2:
            result = 2 if self._is_player_win(2, row, col) else 0

        return result

    def _is_player_win(self, player: int, row: int, column: int) -> bool:
        mark = 'X' if player == 1 else 'O'
        n = len(self.board)

        if all(x == mark for x in [self.board[row][i] for i in range(n)]):
            return True

        if all(x == mark for x in [self.board[i][column] for i in range(n)]):
            return True

        if row == column and \
                all(x == mark for x in [self.board[i][i] for i in range(n)]):
            return True

        if row + column == n - 1 and \
                all(x == mark for x in
                    [self.board[i][n - 1 - i] for i in range(n)]):
            return True

        return False
