'''
TC: O(N)
SC: O(N-D)
Input: s = "azxxzy"
Output: "ay"
'''



def removeDuplicates(s):

    stack = []
    if not s: return stack
    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def removeDuplicatesALL(s):

    output = []
    if not s: return output
    i = 0
    while i < len(s):
        if output and s[i] == output[-1]:
            while i < len(s) and output and s[i] == output[-1]:
                i += 1
            output.pop()
        else:
            output.append(s[i])
            i += 1
    return "".join(output)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []  # char, freq
        for c in s:
            if len(st) == 0 or st[-1][0] != c:
                st.append([c, 1])
            else:
                st[-1][1] += 1
            if st[-1][1] == k:
                st.pop()
        ans = []
        for c, freq in st:
            ans.append(c * freq)
        return "".join(ans)

print(removeDuplicates("azxxzy"))
print(removeDuplicatesALL("abcd"))
print(removeDuplicatesALL("ABCDEEEFFFDD"))
print(removeDuplicatesALL("pbbcggttciiippooaais"))