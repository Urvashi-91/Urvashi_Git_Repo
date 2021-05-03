'''
Method1: Python functions
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))

'''
Method: Elementary Math
TC: O(max(N,M))
SC: O(max(N,M))
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry % 2)
            carry //= 2
        return result[::-1]


'''
Bit Manipulation (Without using +)
TC:O(N+M)
SC: O(max(N.M))
'''
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
