class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()

        # find out rows/columns that originally contain 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        # rewrite all values in those rows/columns with 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in row_set or col in col_set:
                    matrix[row][col] = 0
