class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)

        for i in range(0, len(l), 2 * k):
            low, high = i, min(i + k - 1, len(l) - 1)

            while low < high:
                l[low], l[high] = l[high], l[low]

                low += 1
                high -= 1

        return ''.join(l)
