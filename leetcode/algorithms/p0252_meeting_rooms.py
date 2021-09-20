from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        for i, interval in enumerate(sorted_intervals):
            if i + 1 < len(sorted_intervals) \
                    and interval[1] > sorted_intervals[i + 1][0]:
                return False

        return True
