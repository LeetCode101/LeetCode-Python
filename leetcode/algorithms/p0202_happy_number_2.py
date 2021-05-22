class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self._square_sum(n)

        while slow != fast:
            slow = self._square_sum(slow)
            fast = self._square_sum(fast)
            fast = self._square_sum(fast)

        return slow == 1

    def _square_sum(self, n):
        return sum(map(lambda x: int(x) * int(x), str(n)))
