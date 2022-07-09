
https://leetcode.com/problems/coin-change/discuss/1475250/Python-4-solutions%3A-Top-down-DP-Bottom-up-DP-Space-O(amount)-Clean-and-Concise

  class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dp(i, amount):
            if (i, amount) in memo:
                return memo[(i, amount)]
            if amount == 0:
                return 0
            if i == n:
                return math.inf
            
            ans = dp(i+1, amount)  # Skip ith coin
            if amount >= coins[i]:  # Used ith coin
                ans = min(ans, dp(i, amount - coins[i]) + 1)
            memo[(i, amount)] = ans
            return ans
        
        n = len(coins)
        ans = dp(0, amount)
        return ans if ans != math.inf else -1
