# Problem: Coin Change II (#518)
# Difficulty: Medium
# Approach: Bottom-Up 1D Dynamic Programming (Unbounded Knapsack)
# Pattern: Dynamic Programming, Unbounded Knapsack, Combinations
# Time Complexity: O(n * amount) where n is the number of coin denominations
# Space Complexity: O(amount) for the 1D DP array
# Link: https://leetcode.com/problems/coin-change-ii/

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
                
        return dp[amount]