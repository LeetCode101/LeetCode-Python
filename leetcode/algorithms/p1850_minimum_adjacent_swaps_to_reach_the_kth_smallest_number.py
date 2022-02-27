class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        permutation = list(num)

        for _ in range(k):
            self._next_permutation(permutation)

        count = 0

        for i in range(len(num)):
            if num[i] == permutation[i]:
                continue

            j = i

            while num[i] != permutation[j]:
                j += 1

            while j > i:
                permutation[j - 1], permutation[j] = \
                    permutation[j], permutation[j - 1]
                j -= 1
                count += 1

        return count

    def _next_permutation(self, nums) -> None:
        i = len(nums) - 1

        while i - 1 >= 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.reverse()

            return

        j = i

        while j + 1 < len(nums) and nums[j + 1] > nums[i - 1]:
            j += 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
