'''Go backwards from the end.Try both including and excluding
the ith job.Use binary search to find the next possible job'''

import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        schedule = sorted(zip(startTime, endTime, profit))
        starts, ends, profits = zip(*schedule)
        n = len(schedule)

        dp = [0] * (len(schedule) + 1)
        for i in range(len(schedule) - 1, -1, -1):
            dp[i] = max(dp[i + 1], profits[i] + dp[bisect.bisect_left(starts, ends[i])])

        return dp[0]