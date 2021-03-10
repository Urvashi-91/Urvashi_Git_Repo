'''
Time Complexity: O(nlogn)
Space Complexity: O(1)
'''
def findKthLargest(nums,k):
    nums.sort(reverse=True)
    return nums[k-1]

'''
Method2: QuickSelect
Time Complexity:
Space Complexity:
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[len(nums) // 2]

        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]

        L, M = len(left), len(mid)

        if k <= L:  # that is kth largest element in left side
            return self.findKthLargest(left, k)
        elif k > (L + M):  # that kth element is in the right side hence k-L+M
            return self.findKthLargest(right, k - (L + M))
        else:
            return mid[0]
