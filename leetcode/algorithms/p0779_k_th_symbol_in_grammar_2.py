class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        elif k == 2:
            return 1

        is_odd = k & 1 == 1
        prev = self.kthGrammar(n - 1, (k - 1) // 2 + 1) if is_odd \
            else self.kthGrammar(n - 1, k // 2)

        if is_odd:
            return 1 if prev == 1 else 0
        else:
            return 0 if prev == 1 else 1
