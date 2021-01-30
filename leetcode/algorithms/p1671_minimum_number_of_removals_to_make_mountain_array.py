from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        longest_increasing_sequence = [1] * length
        longest_mountain = [1] * length

        for i in range(1, length):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_increasing_sequence[i] = \
                        max(longest_increasing_sequence[i],
                            1 + longest_increasing_sequence[j])

                if nums[j] > nums[i]:
                    if longest_increasing_sequence[j] > 1:
                        longest_mountain[i] = \
                            max(longest_mountain[i],
                                1 + longest_increasing_sequence[j])

                    if longest_mountain[j] > 1:
                        longest_mountain[i] = \
                            max(longest_mountain[i],
                                1 + longest_mountain[j])

        return length - max(longest_mountain)
