"""Question1: Minimum Path in Unix"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not str:
            return str
        s = []

        for i in path.split('/'):

            if i == '.' or not i:
                continue
            elif i == '..':
                if s:
                    s.pop()

            else:
                s.append(i)
        final = '/' + '/'.join(s)
        return final

"""Time Complexity: O(n) and Space Complexity O(2n)"""