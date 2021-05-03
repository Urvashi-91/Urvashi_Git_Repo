'''
Given a string S, we can split S into 2 strings: S1 and S2.
Return the number of ways S can be split such that the number of
unique characters between S1 and S2 are the same.

Example1:
Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a

Example2:
Input: "bac"
Output: 0

Example3:
Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba
'''

'''
Method1: Ord value
TC: n+n = 2n
SC: n
'''
def splitWays(string):
    if len(string) < 2:
        return 0

    left = [0]*26
    right = [0]*26
    right_unique, left_unique,equal = 0,0,0
    #calculate frequency
    for s in string:
        if right[ord(s) - ord('a')] == 0:
            right_unique += 1
        right[ord(s) - ord('a')] += 1

    #compare uniqueness
    for s in string:
        if left[ord(s) - ord('a')] == 0:
            left_unique += 1

        left[ord(s) - ord('a')] += 1
        right[ord(s) - ord('a')] -= 1

        if right[ord(s) - ord('a')] == 0:
            right_unique -= 1

        if left_unique == right_unique:
            equal += 1
    return equal

