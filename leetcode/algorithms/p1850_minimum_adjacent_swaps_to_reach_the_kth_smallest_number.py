class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        permutation = list(num)

        for _ in range(k):
            self._next_permutation(permutation)

        count = 0

        for i in range(len(num)):
            j = i

            while num[i] != permutation[i]:
                count += 1
                j += 1
                permutation[i], permutation[j] = permutation[j], permutation[i]

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
