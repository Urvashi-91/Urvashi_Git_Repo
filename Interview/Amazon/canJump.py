'''
Method: Greedy (Most optimised)
Time Complexity: O(n)
Space Complexity: O(1)
'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxJump = 0

        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
        return True


'''
Methid:'''