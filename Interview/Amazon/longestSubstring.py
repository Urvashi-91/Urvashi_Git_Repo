'''
Method: Brute Force
Time Complexity: O(n^3)
Space Complexity: O(min(n,m))
'''

class Solution:
    def allUnique(self, s, start, end):
        set_list = {}
        set_list = defaultdict(lambda: 0, set_list)
        for i in range(start, end):

            ch = s[i]
            set_list[ch] += 1
            if set_list[ch] > 1:
                return False

        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if self.allUnique(s, i, j):
                    ans = max(ans, j - i + 1)
        return ans

'''
Method: Brute Force (OrderedDict)
Time Complexity: O(n^3)
Space Complexity: O(min(n,m))
'''
from collections import OrderedDict
def allUnique_OrderedDict(s):
    x = ''.join(OrderedDict.fromkeys(s).keys())
    if x == s:
        return True
    return False

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if allUnique_OrderedDict(s[i:j]):
                ans = max(ans, j - i)
    return ans

'''
Method: Sliding Window
Time Complexity: O(2n)
Space Complexity: O(min(n,m))'''

from collections import defaultdict
def lengthOfLongestSubstring_SlidingWindow(s:str):
    set_list = {}
    set_list = defaultdict(lambda: 0, set_list)

    left,right,result = 0,0,0
    while (right < len(s)):
        r = s[right]
        set_list[r] += 1
        while (set_list[r] > 1):
            l = s[left]
            set_list[l] -= 1
            left += 1
        result = max(result, right - left + 1)
        right += 1
    return result

'''
Method: Sliding Window Optimised
Time Complexity: O(n)'''


def lengthOfLongestSubstring_slidingWindow_Optimised(s: str) -> int:
    set_list = {}
    result, right = 0, 0
    for idx, value in enumerate(s):
        if value in set_list:
            right = max(right, set_list[value] + 1)
        result = max(result, idx - right +1)
        set_list[value] = idx
    return result

print(lengthOfLongestSubstring_slidingWindow_Optimised("abcabcbb"))


def lengthOfLongestSubstring_neetcode(s:str):
    result = 0
    left = 0
    charSet = set()
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result
