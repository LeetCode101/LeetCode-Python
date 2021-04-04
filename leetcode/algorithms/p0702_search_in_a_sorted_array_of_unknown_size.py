# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def get(self, index: int) -> int:
        array = [-1, 0, 3, 5, 9, 12]

        return array[index] if 0 <= index < len(array) else 2147483647


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        low, high = 0, 10000

        while low <= high:
            middle = low + (high - low) // 2
            current = reader.get(middle)

            if current == 2147483647 or current > target:
                high = middle - 1
            elif current < target:
                low = middle + 1
            else:
                return middle

        return -1
