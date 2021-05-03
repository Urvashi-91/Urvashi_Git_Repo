'''
Approach: for loop and heap
TC: O(n^2)
'''
from heapq import *
def find_k_largest_pairs(nums1, nums2, k):
  result = []
  maxheap = []
  # TODO: Write your code here
  for num1 in nums1:
    for num2 in nums2:
      s = num1 + num2
      heappush(maxheap,(-s,num1,num2))
  while k:
    sum, num1, num2 = heappop(maxheap)
    result.append((num1,num2))
    k -= 1
  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([5,2,1], [2,-1], 3)))


main()

'''
Approach: Heap with modification
TC:Since, at most, we’ll be going through all the elements of both arrays and we will 
add/remove one element in the heap in each step, the time complexity of the above algorithm will be 
O(N∗M∗logK) where ‘N’ and ‘M’ are the total number of elements in both arrays, respectively.
If we assume that both arrays have at least ‘K’ elements then the time complexity can be simplified to 
O(K^2logK), because we are not iterating more than ‘K’ elements in both arrays.
SC:O(K) because, at any time, our Min Heap will be storing ‘K’ largest pairs.
'''
from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
  minHeap = []
  for i in range(0, min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(minHeap) < k:
        heappush(minHeap, (nums1[i] + nums2[j], i, j))
      else:
        # if the sum of the two numbers from the two arrays is smaller than the smallest(top)
        # element of the heap, we can 'break' here. Since the arrays are sorted in the
        # descending order, we'll not be able to find a pair with a higher sum moving forward
        if nums1[i] + nums2[j] < minHeap[0][0]:
          break
        else:  # we have a pair with a larger sum, remove top and insert this pair in the heap
          heappop(minHeap)
          heappush(minHeap, (nums1[i] + nums2[j], i, j))

  result = []
  for (num, i, j) in minHeap:
    result.append([nums1[i], nums2[j]])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()







