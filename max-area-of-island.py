class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def _searchIsland(row, col):
            if not _inBound(row, col) or grid[row][col] == 0:
                return 0

            position = (row, col)
            if position in visited:
                return 0
            else:
                visited.add(position)

            size = 1
            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                size += _searchIsland(newRow, newCol)

            return size

        def _inBound(row, col):
            rowInbound = 0 <= row < len(grid)
            colInbound = 0 <= col < len(grid[0])
            return rowInbound and colInbound

        maxArea = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, _searchIsland(row, col))

        return maxArea
