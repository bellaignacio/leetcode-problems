from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        freshOranges = 0
        time = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshOranges += 1
                elif grid[row][col] == 2:
                    queue.append((row, col, 0))

        def _inBound(row, col):
            rowInbound = 0 <= row < ROWS
            colInbound = 0 <= col < COLS
            return rowInbound and colInbound

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while queue:
            row, col, level = queue.popleft()
            time = level

            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if _inBound(newRow, newCol) and grid[newRow][newCol] == 1:
                    queue.append((newRow, newCol, level + 1))
                    grid[newRow][newCol] = 2
                    freshOranges -= 1

        return -1 if freshOranges else time
