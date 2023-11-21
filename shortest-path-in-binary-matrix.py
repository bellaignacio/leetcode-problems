from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        # initialize a queue with starting value(s)
        queue = deque()
        queue.append((0, 0, 1)) # (row, col, level)

        directions = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
        visited = set()
        visited.add((0, 0))

        def _inBound(row, col):
            rowInbound = 0 <= row < ROWS
            colInbound = 0 <= col < COLS
            return rowInbound and colInbound

        while queue:
            # shift current node from queue
            row, col, level = queue.popleft()
            # process current node
            if row == ROWS - 1 and col == COLS - 1:
                return level
            # push (valid) neighbors into queue
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                if _inBound(newRow, newCol) and (newRow, newCol) not in visited and grid[newRow][newCol] == 0:
                    queue.append((newRow, newCol, level + 1))
                    visited.add((newRow, newCol))
            # continue until queue is empty

        return -1
