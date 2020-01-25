from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

        for i in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        if self.empty():
            raise Exception('stack is empty')

        return self.stack.popleft()

    def top(self) -> int:
        if self.empty():
            raise Exception('stack is empty')

        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
