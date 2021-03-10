'''
Method1: Greedy Approach
Time Complexity:O(1)
Space Complexity:O(1)
'''
def intToRoman(self, num: int) -> str:
    roman = ""
    roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
                  900: 'CM', 1000: 'M'}
    if num == 0:
        return roman
    while (num > 0):
        if 1 <= num < 5:
            if num >= 4:
                roman += roman_dict[4]
                num = num - 4
            else:
                roman += roman_dict[1]
                num = num - 1
        elif 5 <= num < 10:
            if num >= 9:
                roman += roman_dict[9]
                num = num - 9
            else:
                roman += roman_dict[5]
                num = num - 5
        elif 10 <= num < 50:
            if num >= 40:
                roman += roman_dict[40]
                num = (num - 40)
            else:
                roman += roman_dict[10]
                num = (num - 10)
        elif 50 <= num < 100:
            if num >= 90:
                roman += roman_dict[90]
                num = (num - 90)
            else:
                roman += roman_dict[50]
                num = (num - 50)
        elif 100 <= num < 500:
            if num >= 400:
                roman += roman_dict[400]
                num = (num - 400)
            else:
                roman += roman_dict[100]
                num = (num - 100)
        elif 500 <= num < 1000:
            if num >= 900:
                roman += roman_dict[900]
                num = (num - 900)
            else:
                roman += roman_dict[500]
                num = (num - 500)
        else:
            roman += roman_dict[1000]
            num = (num - 1000)
    return roman

'''
Method2: Greedy Approach with For loops
Time Complexity:O(1)
Space Complexity: O(1)
'''


def intToRoman(self, num: int) -> str:
    roman = ""
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_dict = dict((zip(values, symbols)))
    if num == 0:
        return roman
    while (num > 0):
        for values in reversed(roman_dict):
            if values > num:
                continue
            else:
                roman += roman_dict[values]
                num -= values
                break

    return roman

'''
Method 3: hardcoded
Time Complexity:O(1)
Space Complexity: O(1)
'''


def intToRoman(self, num: int) -> str:
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    return thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]
print(intToRoman(140))
