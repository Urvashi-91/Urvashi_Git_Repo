class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        L = 0
        R = len(matrix) - 1
        while L < R:
            for i in range(R - L):
                T = L
                B = R

                topleft = matrix[T][L + i]
                matrix[T][L + i] = matrix[B - i][L]
                matrix[B - i][L] = matrix[B][R - i]
                matrix[B][R - i] = matrix[T + i][R]
                matrix[T + i][R] = topleft
            L += 1
            R -= 1
'''
Time Complexity: O(n^2)'''