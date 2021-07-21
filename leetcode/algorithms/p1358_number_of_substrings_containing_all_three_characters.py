import collections


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return self._at_most_k(s, 3) - self._at_most_k(s, 2)

    def _at_most_k(self, nums, k):
        counter = collections.defaultdict(int)
        count = 0
        start = 0

        for end, n in enumerate(nums):
            counter[n] += 1

            while len(counter) > k:
                counter[nums[start]] -= 1

                if counter[nums[start]] == 0:
                    counter.pop(nums[start])

                start += 1

            count += end - start + 1

        return count
