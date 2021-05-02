class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        total_length = 0
        i, length = 0, len(S)

        while i < length:
            c = S[i]
            total_length = total_length * int(c) if c.isdigit() \
                else total_length + 1

            if K <= total_length:
                break

            i += 1

        for j in range(i, -1, -1):
            c = S[j]

            if c.isdigit():
                total_length //= int(c)
                K %= total_length
            else:
                if K == total_length or K == 0:
                    return c

                total_length -= 1
