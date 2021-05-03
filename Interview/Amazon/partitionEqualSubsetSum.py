class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        dp = [[-1 for i in range(int(s / 2) + 1)] for j in range(len(nums))]
        return True if self.canPartitionRecursive(dp, nums, s // 2, 0) == 1 else False

    def canPartitionRecursive(self, dp, nums, s, currentIndex):
        if s == 0:
            return 1

        if currentIndex >= len(nums) or len(nums) == 0:
            return 0

        if dp[currentIndex][s] == -1:
            if nums[currentIndex] <= s:
                if self.canPartitionRecursive(dp, nums, s - nums[currentIndex], currentIndex + 1) == 1:
                    dp[currentIndex][s] == 1
                    return 1

            dp[currentIndex][s] = self.canPartitionRecursive(dp, nums, s, currentIndex + 1)
        return dp[currentIndex][s]




