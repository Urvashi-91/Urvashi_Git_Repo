'''
Approach: Heap
TC: O(min(K,N)+K∗logN)
Sc: O(N)
'''
from heapq import *


def find_Kth_smallest(matrix, k):
    minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
    # if the row of the top element has more elements, add the next element to the heap
    numberCount, number = 0, 0
    while minHeap:
        number, i, row = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        if len(row) > i+1:
            heappush(minHeap, (row[i+1], i+1, row))
    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()

'''
Same Approach in my language
'''
from heapq import *


def find_Kth_smallest(matrix, k):
    number = -1
    minheap = []
    # TODO: Write your code here
    for row in matrix:
        heappush(minheap, (row[0], 0, row))
    while minheap and k > 0:
        number, idx, row = heappop(minheap)
        k -= 1
        if idx + 1 < len(row):
            heappush(minheap, (row[idx + 1], idx + 1, row))

    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()


'''
Approach: Binary search:
TC:The Binary Search could take O(log(max−min)) iterations where ‘max’ is the largest 
and ‘min’ is the smallest element in the matrix and in each iteration we take 
O(N) for counting, therefore, the overall time complexity of the algorithm will be 
O(N∗log(max−min)).
SC: O(1)
'''


def find_Kth_smallest(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[-5]], 1)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main()