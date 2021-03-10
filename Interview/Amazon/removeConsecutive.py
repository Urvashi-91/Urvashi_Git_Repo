Remove consecutive same elements in an array in such a way that the result list should not have any consecutive same elements in the result list

input array: [0,9,9,9,7,7,9,6,6,8]

output array: [0,8] // Note the last 9 in the input has also been removed otherwise the output would have become [0,9,9,8] which is not valid

input: [0.9.9,9,7,7,6,6,8]

output: [0,9,8]


def con_number(self, nums: list):
    a = []
    a.append(nums[0])
    for n in range(1, len(nums)):
        if nums[n] != a[-1]:
            a.append(nums[n])
        else:
            a.pop()

    return a


def remove_consecutives(nums):
    stack = []

    for num in nums:
        stack.append(num)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack = stack[:-2]
    return stack
