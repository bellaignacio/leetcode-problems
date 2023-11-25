class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for value in range(1, amount + 1):
            for coin in coins:
                if value - coin >= 0:
                    dp[value] = min(dp[value], dp[value - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]


# from collections import defaultdict

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def _dfs(remainder, memo):
#             if remainder == 0:
#                 return 0
#             if remainder in memo:
#                 return memo[remainder]

#             memo[remainder] = float('inf')
#             for coin in coins:
#                 if remainder - coin >= 0:
#                     memo[remainder] = min(memo[remainder], _dfs(remainder - coin, memo) + 1)

#             return memo[remainder]

#         memo = defaultdict(int)
#         result = _dfs(amount, memo)
#         return result if result != float('inf') else -1
