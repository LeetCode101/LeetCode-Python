class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for index, value in enumerate(nums):
            if target - value in mapping:
                return (mapping[target - value], index)
            else:
                mapping[value] = index
