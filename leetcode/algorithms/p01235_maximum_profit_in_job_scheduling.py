from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        jobs = [()] * len(startTime)

        for i in range(len(startTime)):
            jobs[i] = (startTime[i], endTime[i], profit[i])

        jobs.sort(key=lambda x: x[0])

        dp = [0] * len(startTime)
        dp[-1] = jobs[-1][2]

        for i in range(len(jobs) - 2, -1, -1):
            next_job = self._find_next_available_job(i, jobs)
            dp[i] = max(jobs[i][2] + (0 if next_job == -1 else dp[next_job]),
                        dp[i + 1])

        return dp[0]

    def _find_next_available_job(self, start, jobs):
        for i in range(start + 1, len(jobs)):
            if jobs[i][0] >= jobs[start][1]:
                return i

        return -1
