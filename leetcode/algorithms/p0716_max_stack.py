class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        max_element = self.stack[-1][1]
        poped = []

        while self.stack and self.stack[-1][0] != max_element:
            poped.append(self.stack.pop()[0])

        self.stack.pop()

        while poped:
            x = poped.pop()

            if not self.stack:
                self.stack.append((x, x))
            else:
                self.stack.append((x, max(x, self.stack[-1][1])))

        return max_element
