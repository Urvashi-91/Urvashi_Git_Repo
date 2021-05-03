'''
Method: Bottom Up approach
TC:
SC:
'''
def can_partition(num, sum):
  n = len(num)
  dp = [[False for x in range(sum+1)] for y in range(n)]

  # populate the sum = 0 columns, as we can always form '0' sum with an empty set
  for i in range(0, n):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for s in range(1, sum+1):
    dp[0][s] = True if num[0] == s else False

  # process all subsets for all sums
  for i in range(1, n):
    for s in range(1, sum+1):
      # if we can get the sum 's' without the number at index 'i'
      if dp[i - 1][s]:
        dp[i][s] = dp[i - 1][s]
      elif s >= num[i]:
        # else include the number and see if we can find a subset to get the remaining sum
        dp[i][s] = dp[i - 1][s - num[i]]

  # the bottom-right corner will have our answer.
  return dp[n - 1][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()


'''
Method: Top Down Approach
TC: O(NS)
SC: O(NS)
'''


def can_partition(num, sum):
    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[-1 for x in range(sum + 1)] for y in range(len(num))]
    return True if can_partition_recursive(dp, num, sum, 0) == 1 else False


def can_partition_recursive(dp, num, sum, currentIndex):
    # base check
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # if we have not already processed a similar problem
    if dp[currentIndex][sum] == -1:
        # recursive call after choosing the number at the currentIndex
        # if the number at currentIndex exceeds the sum, we shouldn't process this
        if num[currentIndex] <= sum:
            if can_partition_recursive(dp, num, sum - num[currentIndex], currentIndex + 1) == 1:
                dp[currentIndex][sum] = 1
                return 1

        # recursive call after excluding the number at the currentIndex
        dp[currentIndex][sum] = can_partition_recursive(
            dp, num, sum, currentIndex + 1)

    return dp[currentIndex][sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()

'''
Method: Bottom UP modified
TC: O(NS)
SC: O(N)
'''
def can_partition(num, sum):
    n = len(num)
    dp = [False for x in range(sum+1)]

    # handle sum=0, as we can always have '0' sum with an empty set
    dp[0] = True

    # with only one number, we can have a subset only when the required sum is equal to its value
    for s in range(1, sum+1):
        dp[s] = num[0] == s

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            # if dp[s]==true, this means we can get the sum 's' without num[i], hence we can move on to
            # the next number else we can include num[i] and see if we can find a subset to get the
            # remaining sum
            if not dp[s] and s >= num[i]:
                dp[s] = dp[s - num[i]]

    return dp[sum]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()

