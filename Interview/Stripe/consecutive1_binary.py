'''
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3
'''

def get_lcos(num):
    current = longest = 0

    def reset_current():
        nonlocal current, longest
        if current > longest:
            longest = current
        current = 0

    while num:
        if num % 2:
            current += 1
        else:
            reset_current()
        num = num // 2 #48 >> 2 means 48 divided by 2^2 or shift bitwise position to right by 2 positions

    reset_current()

    return longest


# Tests
assert get_lcos(0) == 0
assert get_lcos(4) == 1
assert get_lcos(6) == 2
assert get_lcos(15) == 4
assert get_lcos(21) == 1
assert get_lcos(156) == 3

# def decimalTobinary(num):
#     return bin(num).replace('0b','')
#
# def countOnes(num):
#     if num >= 1:
#         bin_num = list(decimalTobinary(num))
#
#         counter = 0
#         consecutive_ones = []
#
#         for i in range(len(bin_num)):
#
#             if (bin_num[i] == '1'):
#
#                 counter += 1
#
#             else:
#                 consecutive_ones.append(counter)
#                 counter = 0
#
#         return max(consecutive_ones)
#     else:
#         return 0
#
# assert countOnes(0) == 0
