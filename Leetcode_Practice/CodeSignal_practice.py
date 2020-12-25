
# def centuryFromYear(year):
#     century_actual = year / 100
#     print (century_actual)
#     century_close = float(year // 100)
#     print(century_close)
#     if century_actual > century_close:
#
#         return century_close + 1
#     else:
#         return century_close
#
# century = centuryFromYear(1905)
# print (century)

def checkPalindrome(inputString):
    rev_string = inputString[::-1]
    print(rev_string)
    if inputString == rev_string:

        return True
    else:
        return False

result = checkPalindrome('aabaa')
print (result)