class Robot:
    def __init__(self, grid, row, column):
        self.grid = grid
        self.row = row
        self.column = column

    def move(self):
        """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and
       robot stays in the current cell.
       :rtype bool
       """
        pass

    def turnLeft(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
        pass

    def turnRight(self):
        """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
        pass

    def clean(self):
        """
       Clean the current cell.
       :rtype void
       """
        pass


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self._dfs(robot, 0, 0, 0, 1, set())

    def _dfs(self, robot, x, y, direction_x, direction_y, visited):
        if (x, y) in visited:
            return

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
