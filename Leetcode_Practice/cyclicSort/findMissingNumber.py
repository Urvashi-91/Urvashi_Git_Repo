'''
Method1: Cyclic Sort
TC: O(N) + O(N-1) + O(N) `= O(N)
SC: O(1)
'''
def find_missing_number(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i]
    if nums[i] < n and nums[i] != nums[j]:

      nums[i], nums[j] = nums[j], nums[i]  # swap
      print (nums)
    else:
      i += 1

  # find the first number missing from its index, that will be our required number
  for i in range(n):
    if nums[i] != i:
      return i

  return n


def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()

'''
Method2: Bitwise XOR
TC: O(N)
SC: O(1)
'''


def find_missing_number(arr):
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1
  for i in range(2, n + 1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n - 1):
    x2 = x2 ^ arr[i]

  # missing number is the xor of x1 and x2
  return x1 ^ x2


def main():
  arr = [1, 5, 2, 6, 4]
  print('Missing number is:' + str(find_missing_number(arr)))


main()

'''
Method3: Sum of n nums and subtract each in array
TC: O(N)
SC: O(1)
'''


def find_missing_number(arr):
  n = max(arr)
  # find sum of all numbers from 1 to n.
  s1 = (n * (n + 1)) // 2

  # subtract all numbers in input from sum.
  for i in arr:
    s1 -= i

  # s1, now, is the missing number
  return s1


def main():
  arr = [1, 5, 2, 6, 4]
  print('Missing number is:' + str(find_missing_number(arr)))


main()



