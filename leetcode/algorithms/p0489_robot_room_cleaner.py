class Robot:
    def __init__(self, grid, row, column):
        self.grid = grid
        self.row = row
        self.column = column
        self.direction_x = 0
        self.direction_y = 1
        self.uncleaned = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.uncleaned.add((i, j))

    def move(self):
        """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and
       robot stays in the current cell.
       :rtype bool
       """
        next_row = self.row + self.direction_y
        next_column = self.column + self.direction_x

        if 0 <= next_row < len(self.grid) \
                and 0 <= next_column < len(self.grid[0]) \
                and self.grid[next_row][next_column] == 1:
            self.row = next_row
            self.column = next_column

            return True
        else:
            return False

    def turnLeft(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
        self.direction_x, self.direction_y = \
            -self.direction_y, self.direction_x

    def turnRight(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
        self.direction_x, self.direction_y = \
            self.direction_y, -self.direction_x

    def clean(self):
        """
       Clean the current cell.
       :rtype void
       """
        if self.grid[self.row][self.column] == 1:
            self.uncleaned.remove((self.row, self.column))

    def room_cleaned(self):
        return len(self.uncleaned) == 0


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self._dfs(robot, 0, 0, 0, 1, set())

    def _dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        for _ in range(4):
            neighbour_x = x + direction_x
            neighbour_y = y + direction_y

            if (neighbour_x, neighbour_y) not in visited and robot.move():
                self._dfs(robot, neighbour_x, neighbour_y,
                          direction_x, direction_y, visited)

                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()

            robot.turnRight()
            direction_x, direction_y = direction_y, -direction_x
