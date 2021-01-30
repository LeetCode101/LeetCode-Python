from typing import List


# Time Limit Exceeded!
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        for i in range(length):
            if i == length - 1:
                arr[i] = -1

                break

            max_number = arr[i + 1]

            for j in range(i + 2, length):
                max_number = max(max_number, arr[j])

            arr[i] = max_number

        return arr
