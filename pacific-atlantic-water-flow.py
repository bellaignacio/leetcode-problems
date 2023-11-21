class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def _dfs(row, col, visited, prevHeight):
            if (row, col) in visited or not _inBound(row, col) or heights[row][col] < prevHeight:
                return

            visited.add((row, col))

            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for dir in directions:
                newRow = row + dir[0]
                newCol = col + dir[1]
                _dfs(newRow, newCol, visited, heights[row][col])

        def _inBound(row, col):
            rowInbound = 0 <= row < ROWS
            colInbound = 0 <= col < COLS
            return rowInbound and colInbound

        results = []
        pacificVisited = set()
        atlanticVisited = set()

        for col in range(COLS):
            # first row (start search from north)
            _dfs(0, col, pacificVisited, heights[0][col])
            # last row (start search from south)
            _dfs(ROWS - 1, col, atlanticVisited, heights[ROWS - 1][col])

        for row in range(ROWS):
            # first col (start search from west)
            _dfs(row, 0, pacificVisited, heights[row][0])
            # last col (start search from east)
            _dfs(row, COLS - 1, atlanticVisited, heights[row][COLS - 1])

        for coord in pacificVisited:
            if coord in atlanticVisited:
                results.append(list(coord))

        return results
