'''
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?
'''
'''
Method1: Binary Search
Time Complexity: O (n^2 log n)
Space Complexity:O(1)

'''
def threeSumSmaller(nums, target):
    nums.sort()
    result = 0
    for i in range(len(nums)-2):
        result += twoSumSmaller(nums, i+1, target - nums[i])
    return result

def twoSumSmaller(nums, startIndex, target):
    sum = 0
    for i in range(startIndex,len(nums)-1):
        j = binarySearch(nums, i, target - nums[i])
        sum += j - i
    return sum

def binarySearch(nums, startIndex, target):
    left = startIndex
    right = len(nums) - 1
    while left < right:
        mid = (left + right + 1) / 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid - 1
    return left

'''
Method2: Two Pointers
Time Complexity:
Space Complexity:
'''

def threeSumSmaller(nums,  target):
    nums.sort()
    sum = 0
    for i in range(len(nums)-2):
        sum += twoSum(nums, i+1, target-nums[i]);/lllll
    return sum

def twoSum(numbers, startIndex, target):
    sum = 0
    left = startIndex
    right = len(numbers) - 1

    while (left < right):
        if numbers[left] + numbers[right] < target:
            sum += right - left
            left += 1
        else:
            right -= 1
    return sum