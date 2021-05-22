class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            n = sum(map(lambda x: int(x) * int(x), str(n)))

            if n == 1:
                return True
            elif n in visited:
                return False
            else:
                visited.add(n)
