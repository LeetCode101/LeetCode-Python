from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n1, n2 = len(v1), len(v2)
        n = min(n1, n2)

        for i in range(n):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1

        if n1 < n2:
            return 0 if self._is_all_zero(v2, n) else -1
        elif n1 > n2:
            return 0 if self._is_all_zero(v1, n) else 1
        else:
            return 0

    def _is_all_zero(self, v: List[str], i: int) -> bool:
        for j in range(i, len(v)):
            if int(v[j]) != 0:
                return False

        return True
