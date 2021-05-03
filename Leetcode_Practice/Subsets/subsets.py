'''
TC: O(N*2^N)
SC: O(N*2^N)
'''
from itertools import combinations


def find_subsets(nums):
    subsets = []
    # TODO: Write your code here
    for i in range(len(nums) + 1):
        lic = list(combinations(nums, i))
        for c in lic:
            subsets.append(c)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()


'''
Method2:
TC:
SC:
'''
def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set1 = list(subsets[i])
      set1.append(currentNumber)
      subsets.append(set1)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
