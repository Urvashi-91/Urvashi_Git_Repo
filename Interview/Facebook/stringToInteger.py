'''
Method1:
Time Complexity:
'''
import re
def myAtoi(s: str) -> int:
    # I am looking for something that starts with +-(optional) and digits. Basically searching for an int
    numString = re.findall('^[\+\-]?\d+',s.strip())
    print(numString)
    # If no integer is found, return 0
    if len(numString) == 0:
        return 0
    if int(numString[0]) > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif int(numString[0]) < -2 ** 31:
        return -2 ** 31
    else:
        # returning as int for positive int with + sign
        return int(numString[0])

'''
Method 2
Time Complexity: O(n^2)
'''
# def myAtoi(self, s: str) -> int:
#     n = len(s)
#
#     def is_valid(i):
#         return 0 <= i < n
#
#     i_s = 0
#     while is_valid(i_s) and s[i_s] == ' ':
#         i_s += 1
#
#     sign = 1
#     if is_valid(i_s) and s[i_s] in "+-":
#         if s[i_s] == "-":
#             sign = -1
#         i_s += 1
#
#     magnitude = 0
#     while is_valid(i_s) and s[i_s].isdigit():
#         magnitude *= 10
#         magnitude += ord(s[i_s]) - ord('0') # result * 10 + (str[i] - '0')
#         if sign * magnitude < -(2 ** 31):
#             magnitude = 2 ** 31
#             break
#         elif sign * magnitude > 2 ** 31 - 1:
#             magnitude = 2 ** 31 - 1
#             break
#         else:
#             i_s += 1
#     return sign * magnitude

print(myAtoi(" -456"))

'''
'''
def str_to_int(input_str):

    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int



s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))