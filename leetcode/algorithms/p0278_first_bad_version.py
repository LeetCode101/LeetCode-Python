def isBadVersion(version):
    return version >= 4


class Solution:
    def firstBadVersion(self, n):
        low, high = 1, n

        while low < high:
            middle = low + (high - low) // 2

            if not isBadVersion(middle):
                low = middle + 1
            else:
                high = middle

        return low
