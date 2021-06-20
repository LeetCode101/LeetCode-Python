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
        prev_interval = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]

            if prev_interval[1] < interval[0]:
                free_time.append(Interval(prev_interval[1], interval[0]))

            prev_end = prev_interval[1] if prev_interval[1] > interval[1] else interval[1]
            prev_interval = (interval[0], prev_end)

        return free_time
