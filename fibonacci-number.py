class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0, 1]
        i = 2

        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1

        return dp[1]


# class Solution:
#     def fib(self, n: int, memo = {}) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         if n in memo:
#             return memo[n]

#         memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
#         return memo[n]


# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1

#         return self.fib(n - 1) + self.fib(n - 2)
