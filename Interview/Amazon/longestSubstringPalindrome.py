def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):

        # if len(s) % 2 == 0:
        temp = helper (s, i,i+1)
        if len(temp) > len(res):
            res = temp
        # else:
        temp = helper (s, i,i)
        if len(temp) > len(res):
            res = temp
    return res


def helper(s, left, right):
    while (left >= 0 and right < len(s) and s[left] == s[right]):
        left -= 1
        right += 1
    print (left+1,right,s[left+1:right])
    return s[left+1:right]

assert longestPalindrome("babad") == "bab"
# assert longestPalindrome("cbbd") == "bb"
# assert longestPalindrome("a") == "a"
#print(longestPalindrome("ac"))
