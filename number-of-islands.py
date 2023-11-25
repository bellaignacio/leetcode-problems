class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _dfs(row, col):
            if not _inBound(row, col):
                return False

            position = f'{row},{col}'
            if position in visited:
                return False
            else:
                visited.add(position)

            if grid[row][col] == '0':
                return False

            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                _dfs(newRow, newCol)

            return True

        def _inBound(row, col):
            rowInbound = 0 <= row < len(grid)
            colInbound = 0 <= col < len(grid[0])
            return rowInbound and colInbound

        count = 0
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if _dfs(row, col):
                    count += 1

        return count
