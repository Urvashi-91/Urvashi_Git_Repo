'''
Method1: Two pointer Left-to-Right Pass Improved
Time Complexity: O(1) or O(n)
Space Complexity: O(1)
'''
def romanToInt(s):
    symbols = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    values = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman_dict = dict((zip(symbols,values)))
    i = result = 0

    while (i<len(s)):
        j = i + 2
        # print (i,result,s[i:j],s[i])
        if s[i:j] in roman_dict:
            # print (s[i:j])
            result += roman_dict[s[i:j]]
            i += 2
            # print(i,result)
        else:
            # print(s[i])
            result += roman_dict[s[i]]
            i += 1
            # print(i,result)
    return result

'''
Method: Right to left Pass
'''


def romanToInt(self, s: str) -> int:
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_dict = dict((zip(symbols, values)))
    total = roman_dict.get(s[-1])
    for i in reversed(range(len(s) - 1)):
        if roman_dict[s[i]] < roman_dict[s[i + 1]]:
            total -= roman_dict[s[i]]
        else:
            total += roman_dict[s[i]]
    return total




print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))