from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        oranges = 0
        minutes = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    oranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))

        def _inBound(row, col):
            rowInbound = 0 <= row < ROWS
            colInbound = 0 <= col < COLS
            return rowInbound and colInbound

        while queue:
            row, col, min = queue.popleft()
            minutes = max(minutes, min)

            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if _inBound(newRow, newCol) and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    oranges -= 1
                    queue.append((newRow, newCol, min + 1))

        return -1 if oranges else minutes
