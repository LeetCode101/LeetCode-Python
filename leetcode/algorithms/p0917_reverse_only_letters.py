class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = list(s)
        low, high = 0, len(result) - 1

        while low < high:
            while low < high and not result[low].isalpha():
                low += 1

            while low < high and not result[high].isalpha():
                high -= 1

            result[low], result[high] = result[high], result[low]
            low += 1
            high -= 1

        return ''.join(result)
