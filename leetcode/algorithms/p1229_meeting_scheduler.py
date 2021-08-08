from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]],
                             slots2: List[List[int]], duration: int) \
            -> List[int]:
        i = j = 0
        sorted_slots1 = sorted(slots1, key=lambda x: x[0])
        sorted_slots2 = sorted(slots2, key=lambda x: x[0])

        while i < len(sorted_slots1) and j < len(sorted_slots2):
            a_start, a_end = sorted_slots1[i]
            b_start, b_end = sorted_slots2[j]

            if a_start < b_end and b_start < a_end \
                    and min(a_end, b_end) - max(a_start, b_start) >= duration:
                start = max(a_start, b_start)

                return [start, start + duration]

            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return []
