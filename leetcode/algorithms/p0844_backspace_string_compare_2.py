class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        count1, count2 = 0, 0

        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == '#' or count1 > 0):
                count1 = count1 + 1 if S[i] == '#' else count1 - 1
                i -= 1

            while j >= 0 and (T[j] == '#' or count2 > 0):
                count2 = count2 + 1 if T[j] == '#' else count2 - 1
                j -= 1

            if i < 0 or j < 0:
                return i == j

            if S[i] != T[j]:
                return False

            i -= 1
            j -= 1

        return i == j
