'''
Method1: Cyclic Sort
TC: O(n)
SC:O(1)
'''
def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]
    else:
      i += 1

  return -1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()


'''
Method2: Fast and Slow Pointer
TC: O(n)
SC: o(1)
'''
def find_duplicate(arr):
  slow, fast = arr[0], arr[arr[0]]
  while slow != fast:
    slow = arr[slow]
    fast = arr[arr[fast]]

  # find cycle length
  current = arr[arr[slow]]
  cycleLength = 1
  while current != arr[slow]:
    current = arr[current]
    cycleLength += 1

  return find_start(arr, cycleLength)


def find_start(arr, cycleLength):
  pointer1, pointer2 = arr[0], arr[0]
  # move pointer2 ahead 'cycleLength' steps
  while cycleLength > 0:
    pointer2 = arr[pointer2]
    cycleLength -= 1

  # increment both pointers until they meet at the start of the cycle
  while pointer1 != pointer2:
    pointer1 = arr[pointer1]
    pointer2 = arr[pointer2]

  return pointer1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()




