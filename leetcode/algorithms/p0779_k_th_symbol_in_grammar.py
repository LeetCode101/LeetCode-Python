# Time Limit Exceeded!
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = self._get_nth_row(n)

        return int(row[k - 1])

    def _get_nth_row(self, n):
        if n == 1:
            return '0'

        return ''.join(['01' if x == '0' else '10'
                        for x in self._get_nth_row(n - 1)])
