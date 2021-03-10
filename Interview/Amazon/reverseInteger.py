'''
Method1: Brute Force using /10 amd %10 formula --> O(n)
Method1: O(1)
'''
class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)[::-1]
        if abs(x) // 10 == 0:
            return x

        elif x < 0:

            rev_x = int(x_str[:len(x_str) - 1])
            rev_x = -rev_x
        else:
            rev_x = int(x_str)
        if rev_x < -2 ** 31 or rev_x > 2 ** 31 - 1:
            return 0
        return rev_x
