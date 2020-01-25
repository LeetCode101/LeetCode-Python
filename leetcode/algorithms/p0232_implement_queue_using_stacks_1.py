class MyQueue:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        return self.queue.pop(0)

    def peek(self) -> int:
        if self.empty():
            raise Exception('queue is empty')

        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
