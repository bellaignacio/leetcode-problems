class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # binary search vertically
        top, bottom = 0, n - 1
        while top <= bottom:
            mid_row = ((bottom - top) // 2) + top
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            else:
                break

        if top > bottom:
            return False

        # binary search horizontally
        row = ((bottom - top) // 2) + top
        left, right = 0, m - 1

        while left <= right:
            mid_col = ((right - left) // 2) + left
            if target > matrix[row][mid_col]:
                left = mid_col + 1
            elif target < matrix[row][mid_col]:
                right = mid_col - 1
            else:
                return True
