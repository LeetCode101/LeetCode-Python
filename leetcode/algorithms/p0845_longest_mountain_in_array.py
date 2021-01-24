from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_length = 0
        length = len(arr)
        i = 0

        while i < length:
            start, top, end = i, i, i

            while top + 1 < length:
                if arr[top + 1] <= arr[top]:
                    break

                top += 1

            end = top

            while end + 1 < length:
                if arr[end + 1] >= arr[end]:
                    break

                end += 1

            if start != top and top != end:
                max_length = max(max_length, end - start + 1)

            i = end + 1 if top == end else end

        return max_length
