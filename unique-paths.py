class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                dp[col][row] = dp[col - 1][row] + dp[col][row - 1]

        return dp[-1][-1]


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         memo = {}

#         def path_count(m, n):
#             if m == 0 or n == 0:
#                 return 0
#             elif m == 1 and n == 1:
#                 return 1

#             key = f'({m}, {n})'
#             if key in memo:
#                 return memo[key]
#             memo[key] = path_count(m - 1, n) + path_count(m, n - 1)
#             return memo[key]

#         return path_count(m, n)


# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def path_count(m, n):
#             if m == 0 or n == 0:
#                 return 0
#             elif m == 1 and n == 1:
#                 return 1
#             return path_count(m - 1, n) + path_count(m, n - 1)

#         return path_count(m, n)
