from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def _inBound(row, col):
            rowInbound = 0 <= row < ROWS
            colInbound = 0 <= col < COLS
            return rowInbound and colInbound

        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1 # placeholder until processed

        while queue:
            row, col = queue.popleft()
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if not _inBound(newRow, newCol) or mat[newRow][newCol] != -1:
                    continue
                mat[newRow][newCol] = mat[row][col] + 1
                queue.append((newRow, newCol))

        return mat
