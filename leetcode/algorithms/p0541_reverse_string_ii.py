class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)

        for i in range(0, len(chars), 2 * k):
            low, high = i, min(i + k - 1, len(chars) - 1)

            while low < high:
                chars[low], chars[high] = chars[high], chars[low]

                low += 1
                high -= 1

        return ''.join(chars)
