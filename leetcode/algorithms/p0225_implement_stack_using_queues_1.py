from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception('stack is empty')

        return self.queue.pop()

    def top(self) -> int:
        if self.empty():
            raise Exception('stack is empty')

        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
