class TicTacToe:
    def __init__(self, n: int):
        self.board = [['' for _ in range(n)] for _ in range(n)]
        self.rows = [0] * n
        self.columns = [0] * n
        self.diagonals1 = 0
        self.diagonals2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = 'X' if player == 1 else 'O'
        self.rows[row] += 1 if player == 1 else -1
        self.columns[col] += 1 if player == 1 else -1

        if row == col:
            self.diagonals1 += 1 if player == 1 else -1

        if row + col == len(self.board) - 1:
            self.diagonals2 += 1 if player == 1 else -1

        target = len(self.board) if player == 1 else - len(self.board)

        if self.rows[row] == target or self.columns[col] == target \
                or self.diagonals1 == target or self.diagonals2 == target:
            return player
        else:
            return 0
