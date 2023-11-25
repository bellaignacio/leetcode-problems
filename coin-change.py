from collections import defaultdict

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def _dfs(remainder, memo):
            if remainder == 0:
                return 0
            if remainder in memo:
                return memo[remainder]

            memo[remainder] = float('inf')
            for coin in coins:
                if remainder - coin >= 0:
                    memo[remainder] = min(memo[remainder], _dfs(remainder - coin, memo) + 1)

            return memo[remainder]

        memo = defaultdict(int)
        result = _dfs(amount, memo)
        return result if result != float('inf') else -1
