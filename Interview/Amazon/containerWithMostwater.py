'''
Method1: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def maxArea(height):
    '''
    a[i]: list -> height[]
    n: int -> len(height)
    i: int -> [1:len(heingt)+1]
    (i,a[i]): coordinate
    '''
    max_area = 0
    n = len(height)
    for i in range(n):
        for j in range(i+1,n):
            current = min(height[i],height[j]) * (j-i)
            max_area = max(max_area, current)
    return max_area


'''
Method2: Two Pointer Approach
Time Complexity: O(n)
Space Complexity: O(1)
'''
def maxArea2(height):
    '''
    a[i]: list -> height[]
    n: int -> len(height)
    i: int -> [1:len(heingt)+1]
    (i,a[i]): coordinate
    '''
    max_area = i = 0
    j = len(height) - 1
    while (i < j):
        current = min(height[i],height[j]) * (j-i)
        max_area = max(max_area, current)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area
print(maxArea2([1,8,6,2,5,4,8,3,7]))
print(maxArea2([1,1]))
print(maxArea2([4,3,2,1,4]))
print(maxArea2([1,2,1]))