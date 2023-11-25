class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n in memo:
            return memo[n]

        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
