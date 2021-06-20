class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if not schedule:
            return []

        intervals = []
        free_time = []

        for s in schedule:
            for interval in s:
                intervals.append((interval.start, interval.end))

        intervals.sort()
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if prev_end < interval[0]:
                free_time.append(Interval(prev_end, interval[0]))

            prev_end = max(prev_end, interval[1])

        return free_time
