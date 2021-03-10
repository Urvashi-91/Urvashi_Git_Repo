'''
Method: two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
'''
def twoSum(numbers,target):
    i = 0
    j = len(numbers)-1
    if len(numbers) <= 1:
        return numbers

    while(i<j):
        if numbers[i] + numbers[j] == target:
            return i+1,j+1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4],6))
print(twoSum([-1,0],-1))