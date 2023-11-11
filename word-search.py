class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # base cases
        #   1. if word is found, return True
        #       - keep track of index, done when i == len(word)
        #   2. otherwise
        #       - cell is out of bounds
        #       - cell does not match word[i]
        #       - already visited cell

        ROWS, COLS = len(board), len(board[0])
        visited = set()


        def _backtrack(r, c, i):
            if i == len(word):
                return True
            if not _inbound(r, c) or word[i] != board[r][c] or (r, c) in visited:
                return False

            visited.add((r, c))

            # go down a level - try the 4 possible adjacent cells
            res = (_backtrack(r + 1, c, i + 1) or
                _backtrack(r - 1, c, i + 1) or
                _backtrack(r, c + 1, i + 1) or
                _backtrack(r, c - 1, i + 1))

            visited.discard((r, c)) # "backtrack": undo modification, go back up one level
            return res

        def _inbound(r, c):
            rowInbound = r >= 0 and r < ROWS
            colInbound = c >= 0 and c < COLS
            return rowInbound and colInbound


        # optimization:
        # create a hash table of counts for all letters in the board
        # if any letter in the word exceeds its count, return False (no need to search at all)
        # count = defaultdict(int)
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         count[board[r][c]] += 1

        # for char in word:
        #     if char not in count:
        #         return False
        #     else:
        #         count[char] -= 1
        #         if count[char] < 0:
        #             return False


        # backtracking/DFS traversal for EACH cell
        for r in range(ROWS):
            for c in range(COLS):
                if _backtrack(r, c, 0):
                    return True
                else: # if false, try the next cell starting point
                    visited.clear()

        return False
