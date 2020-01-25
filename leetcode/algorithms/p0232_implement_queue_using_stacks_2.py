class MyQueue:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        for _ in range(len(self.queue1)):
            self.queue2.append(self.queue1.pop())

        self.queue1.append(x)

        for _ in range(len(self.queue2)):
            self.queue1.append(self.queue2.pop())

    def pop(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        return self.queue1.pop()

    def peek(self) -> int:
        return self.queue1[-1]

    def empty(self) -> bool:
        return len(self.queue1) == 0
