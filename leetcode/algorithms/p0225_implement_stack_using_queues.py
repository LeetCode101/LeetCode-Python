from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception('stack is empty')

        return self.stack.pop()

    def top(self) -> int:
        if self.empty():
            raise Exception('stack is empty')

        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
