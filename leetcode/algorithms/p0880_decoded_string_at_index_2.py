class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        total_length = 0

        for i, c in enumerate(S):
            if c.isdigit():
                if total_length * int(c) >= K:
                    return self.decodeAtIndex(
                        S[0:i], (K - 1) % total_length + 1)

                total_length *= int(c)
            else:
                total_length += 1

                if total_length == K:
                    return c
