from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = {}
        n = len(nums)

        for i in range(n):
            if i in visited:
                continue

            current = i

            while self._is_valid_cycle(i, current, nums):
                visited[current] = i

                current = (current + nums[current]) % n

                if current in visited:
                    if visited[current] == i:
                        return True

                    break

        return False

    def _is_valid_cycle(self, start, current, nums):
        return nums[current] % len(nums) != 0 \
               and ((nums[start] > 0 and nums[current] > 0)
                    or (nums[start] < 0 and nums[current] < 0))
