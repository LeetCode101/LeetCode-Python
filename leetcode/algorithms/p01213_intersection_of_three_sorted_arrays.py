from typing import List


class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int],
                           arr3: List[int]) -> List[int]:
        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)

        return sorted(list(filter(lambda x: x in set2 and x in set3, set1)))
