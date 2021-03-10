from bisect import *
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1
                if hi < len(nums) and abs(complement - nums[hi]) < abs(diff):
                    diff = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(diff):
                    diff = complement - nums[lo]
            if diff == 0:
                break
        return target - diff
def threeSumClosest(nums,target):
    nums.sort()
    res = sum(nums[:3])

    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left<right:
            comp_sum = nums[i]+nums[left]+nums[right]
            if abs(comp_sum - target) < abs(res - target):
                res = comp_sum
            if comp_sum < target:
                left += 1
            else:
                right += 1
    return res



