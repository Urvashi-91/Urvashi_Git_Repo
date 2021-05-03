'''
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements.
Amplitude is the range of the array (basically difference between largest and smallest element).
Example1:
Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

Example2:
Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10
'''
'''
Method1: Sliding Window
TC: O(nlogn)
SC: O(n)
'''
def minAplitude(nums):
    n = len(nums)
    if n <= 4:
        return 0
    nums.sort()
    ans = float('inf')
    for i in range(4):
        ans = min(ans, nums[i+n-4]-nums[i])
    print(ans)


minAplitude([-1,3,-1,8,5,4])
minAplitude([10,10,3,4,10])


'''
Method2: Two Heap
TC: nlogn
SC: n
'''
import heapq


def minDifference(self, nums: List[int]) -> int:
    if len(nums) < 5:
        return 0

    small = heapq.nsmallest(4, nums)
    big = heapq.nlargest(4, nums)

    return min(big[3] - small[0], big[2] - small[1], big[1] - small[2], big[0] - small[3])
