class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_a, stack_b = [], []

        for c in S:
            if c == '#':
                if stack_a:
                    stack_a.pop()
            else:
                stack_a.append(c)

        for c in T:
            if c == '#':
                if stack_b:
                    stack_b.pop()
            else:
                stack_b.append(c)

        if len(stack_a) != len(stack_b):
            return False

        while stack_a:
            a, b = stack_a.pop(), stack_b.pop()

            if a != b:
                return False

        return True
