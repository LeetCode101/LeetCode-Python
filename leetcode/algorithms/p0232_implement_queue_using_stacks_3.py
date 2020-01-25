class MyQueue:
    def __init__(self):
        self.front = None
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack1:
            self.front = x

        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        if not self.stack2:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        return self.stack2[-1] if self.stack2 else self.front

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
