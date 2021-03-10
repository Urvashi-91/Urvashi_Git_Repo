'''
Method1: Brute Force with Two Pointers
Time Complexity: O(nlogn + n^2)
Space Complexity: O(n)
'''
def threeSum(nums):
    '''
    Given an array nums of n integers, are there elements a, b, c in nums such that
    a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    Notice that the solution set must not contain duplicate triplets.
    '''
    nums = sorted(nums)
    result = []
    pivot = []
    for i in range(len(nums)-2):
        if nums[i] in pivot:
            continue
        else:
            pivot.append(nums[i])
            left = i+1
            right = len(nums)-1
            while (left < right):
                if nums[left] + nums[right] == -(nums[i]):
                    x = [nums[i],nums[left],nums[right]]
                    if x in result:
                        left += 1
                        right -= 1
                        continue
                    else:
                        result.append(x)
                        left += 1
                        right -= 1
                elif nums[left] + nums[right] < -(nums[i]):
                    left += 1
                else:
                    right -= 1

    return result

print(threeSum([-1,0,1,2,-1,-4]) )
# == [[-1,-1,2],[-1,0,1]]
print(threeSum([]))
print(threeSum([0]))
print(threeSum([-2,0,0,2,2]))

'''
Method2: Two Pointers With Two Functions
Time Complexity: O(n^2) + O(nlogn)
Space Complexity: O(log n) to O(n)
'''
def threeSum2(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            twoSumII(nums, i, res)
    return res


def twoSumII(nums, i, res):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1

print(threeSum2([-1,0,1,2,-1,-4]) )
# == [[-1,-1,2],[-1,0,1]]
print(threeSum2([]))
print(threeSum2([0]))
print(threeSum2([-2,0,0,2,2]))

'''
Method3: Hashset
Time Complexity: O(n^2) + O(nlogn)
Spac Complexity: O(n)
'''


def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            self.twoSum(nums, i, res)
    return res


def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1

'''
Method 4: No Sort
Time Complexity:O(n^2)
Space Complexity:O(n)
'''


def threeSum(self, nums: List[int]) -> List[List[int]]:
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i + 1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return res