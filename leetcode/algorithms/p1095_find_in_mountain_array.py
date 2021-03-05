# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)


class Solution:
    def findInMountainArray(self, target: int,
                            mountain_arr: 'MountainArray') -> int:
        peak = self._find_peak(0, mountain_arr.length() - 1, mountain_arr)

        if mountain_arr.get(peak) == target:
            return peak

        left = self.binary_search(0, peak - 1, mountain_arr, target, True)

        return left if left != -1 else self.binary_search(
            peak + 1, mountain_arr.length() - 1, mountain_arr, target, False)

    def _find_peak(self, low, high, mountain_arr: 'MountainArray'):
        while low < high:
            middle = low + (high - low) // 2

            if mountain_arr.get(middle) < mountain_arr.get(middle + 1):
                low = middle + 1
            else:
                high = middle

        return low

    def binary_search(self, low, high, mountain_arr: 'MountainArray',
                      target, increasing):
        while low <= high:
            middle = low + (high - low) // 2
            value = mountain_arr.get(middle)

            if value == target:
                return middle
            elif (value > target and increasing) \
                    or (value < target and not increasing):
                high = middle - 1
            else:
                low = middle + 1

        return -1
