'''

Complexity Analysis

Assume, n is the length of the string s

Time Complexity:
O(maxK ⋅ n), where maxK is the maximum value of k and n is the length of a given string s. We traverse a string of size
n and iterate k times to decode each pattern of form k[string]. This gives us worst case time complexity as
O(maxK ⋅ n)

Space Complexity:
O(m+n), where m is the number of letters(a-z) and n is the number of digits(0-9) in string s. In worst case, the maximum size of
stringStack and countStack could be
m and n respectively.
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [["", 1]]
        num = ""

        for ch in s:
            if ch.isnumeric():
                num += ch

            elif ch == '[':
                stack.append(["", int(num)])
                num = ""

            elif ch == ']':
                string, k = stack.pop()
                stack[-1][0] += string * k

            else:
                stack[-1][0] += ch

        return stack[-1][0]
