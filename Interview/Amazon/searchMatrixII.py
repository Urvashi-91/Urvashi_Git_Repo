'''
Method: Brute Force
Time Complexity: O(mn)
Space Complexity: O(m)
'''







'''
Method: Search Space reduction
Time Complexity: O(n+m)
Space Complexity: O(1)
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)  # Rows
        N = len(matrix[0])  # Columns

        if not matrix:  # Base cases
            return False

        R = M - 1
        C = 0

        if matrix[M - 1][N - 1] < target or matrix[0][0] > target:
            return False

        while R >= 0 and C < N:
            if matrix[R][C] == target:
                return True
            elif matrix[R][C] > target:
                R -= 1
            else:
                C += 1

        return False


'''
Method: Ddivide and OCnquer
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # an empty matrix obviously does not contain `target`
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # this submatrix has no height or no width.
            if left > right or up > down:
                return False
            # `target` is already larger than the largest element or smaller
            # than the smallest element in this submatrix.
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            return search_rec(left, row, mid - 1, down) or \
                   search_rec(mid + 1, up, right, row - 1)

        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
