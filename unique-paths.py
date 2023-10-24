class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def path_count(m, n):
            if m == 0 or n == 0:
                return 0
            elif m == 1 and n == 1:
                return 1
            return path_count(m - 1, n) + path_count(m, n - 1)

        return path_count(m, n)
