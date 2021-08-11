from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) \
            -> List[int]:
        greater_elements = {}
        stack = []
        result = []

        for n in nums2:
            while stack and stack[-1] < n:
                greater_elements[stack.pop()] = n

            stack.append(n)

        for n in nums1:
            result.append(greater_elements.get(n, -1))

        return result
