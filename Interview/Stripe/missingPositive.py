'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
def get_positive_subset(array):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] > 0 and array[j] <= 0:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] > 0:
            j -= 1
        else:
            i += 1

    # print("i: {}, j: {}".format(i, j))
    # print("partitioned_array:", array)
    pivot = i if array[i] > 0 else i + 1
    return array[pivot:]


def get_missing_number(array):
    if not array:
        return 1

    array = get_positive_subset(array)
    array_len = len(array)
    # print("array: {}".format(array))

    if not array:
        return 1

    if max(array) == len(array):
        return max(array) + 1

    for num in array:
        current_num = abs(num)
        if (current_num - 1) < array_len:
            array[current_num - 1] *= -1
    # print("mutated_array: {}".format(array))

    for i, num in enumerate(array):
        if num > 0:
            return i + 1


assert get_missing_number([3, 4, -1, 1]) == 2
assert get_missing_number([1, 2, 0]) == 3
assert get_missing_number([1, 2, 5]) == 3
assert get_missing_number([1]) == 2
assert get_missing_number([-1, -2]) == 1
assert get_missing_number([]) == 1


# def firstMissingPositive(nums):
#     """
#     if nums == []:
#         return 1
#     for i in range(0,len(nums)):
#         if nums[i] <= 0 or nums[i] > len(nums):
#             continue
#         val = nums[i]
#         while nums[val-1] != val:
#             nextVal = nums[val-1]
#             nums[val-1] = val
#             val = nextVal
#             if val <= 0 or val > len(nums):
#                 break
#     for i in range(0,len(nums)):
#         if nums[i] != i+1:
#             return i+1
#     return len(nums)+1
#     """
#     nums = list(set(nums)) + [0]
#     n = len(nums)
#     for i in range(len(nums)):  # delete those useless elements
#         if nums[i] < 0 or nums[i] >= n:
#             nums[i] = 0
#     for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
#         nums[nums[i] % n] += n
#     for i in range(1, len(nums)):
#         if nums[i] // n == 0:
#             return i
#     return n