from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        count = [0] * (num + 1)

        for i in range(1, num + 1):
            if i & 1 == 1:
                count[i] = count[i - 1] + 1
            else:
                count[i] = count[i // 2]

        return count
