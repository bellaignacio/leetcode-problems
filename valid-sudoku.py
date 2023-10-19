from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subs = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                digit = board[r][c]
                if digit != '.':
                    if digit in rows[r]:
                        return False
                    if digit in cols[c]:
                        return False
                    if digit in subs[f'{r // 3}{c // 3}']:
                        return False

                    rows[r].add(digit)
                    cols[c].add(digit)
                    subs[f'{r // 3}{c // 3}'].add(digit)

        return True
