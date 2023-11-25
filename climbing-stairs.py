class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [1, 2]
        i = 3

        while i <= n:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i += 1

        return dp[1]


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n < 3:
#             return n
#         dp = [None for _ in range(n + 1)]
#         dp[1], dp[2] = 1, 2
#         i = 3

#         while i <= n:
#             dp[i] = dp[i - 1] + dp[i - 2]
#             i += 1

#         return dp[-1]


# class Solution:
#     def climbStairs(self, n: int, memo = {}) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n in memo:
#             return memo[n]

#         memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
#         return memo[n]


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1: # if 1 step, there is only 1 way up (1 step)
#             return 1
#         if n == 2: # if 2 steps, there are 2 ways up (2 steps, 1 step + 1 step)
#             return 2

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
