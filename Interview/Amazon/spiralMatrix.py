'''
Method: Layer By Layer
Time Complexity: O(MN)
Space Complexity: O(MN)
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L = 0
        R = len(matrix[0])
        T = 0
        B = len(matrix)
        result = []

        while L < R and T < B:
            # from left to right
            for i in range(L, R):
                result.append(matrix[T][i])
            T += 1
            # from Top to Bottom
            for i in range(T, B):
                result.append(matrix[i][R - 1])
            R -= 1

            if not (L < R and T < B):
                break

            # from right to left
            for i in range(R - 1, L - 1, -1):
                result.append(matrix[B - 1][i])
            B -= 1
            # from bottom to top
            for i in range(B - 1, T - 1, -1):
                result.append(matrix[i][L])
            L += 1
        return result

'''
Method: Simulation
Time Complexity: O(mn)
Space Complexity: O(1)
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        R, C = len(matrix),len(matrix[0])
        seen = [[False]*C for _ in matrix]
        ans = []
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        r = c = di = 0
        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr,cc = r + dr[di], c + dc[di]
            if 0 <= cr <R and 0 <= cc < C and not seen[cr][cc]:
                r,c = cr,cc
            else:
                di = (di+1)%4
                r,c = r+dr[di],c+dc[di]
        return ans