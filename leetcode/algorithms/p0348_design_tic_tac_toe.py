# Time Limit Exceeded!
class TicTacToe:
    def __init__(self, n: int):
        self.board = [['' for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = 'X' if player == 1 else 'O'

        result = 0

        if player == 1:
            result = 1 if self.is_player_win(1) else 0
        elif player == 2:
            result = 2 if self.is_player_win(2) else 0

        return result

    def is_player_win(self, player: int) -> bool:
        mark = 'X' if player == 1 else 'O'
        n = len(self.board)

        for i in range(n):
            if all(x == mark for x in self.board[i]):
                return True

        for i in range(n):
            if all(x == mark for x in [self.board[j][i] for j in range(n)]):
                return True

        if all(x == mark for x in [self.board[i][i] for i in range(n)]):
            return True

        if all(x == mark for x in
               [self.board[i][n - 1 - i] for i in range(n)]):
            return True

        return False
