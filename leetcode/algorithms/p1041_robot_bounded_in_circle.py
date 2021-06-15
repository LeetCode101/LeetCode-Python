class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx, dy = 0, 1
        x = y = 0

        for instruction in instructions:
            if instruction == 'G':
                x, y = x + dx, y + dy
            elif instruction == 'L':
                dx, dy = -dy, dx
            elif instruction == 'R':
                dx, dy = dy, -dx

        return (dx, dy) != (0, 1) or (x == 0 and y == 0)
