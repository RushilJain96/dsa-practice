# Problem: Coin Change (#322)
# Difficulty: Medium
# Approach: Bottom-Up Dynamic Programming (1D Array)
# Pattern: Dynamic Programming, Knapsack DP
# Time Complexity: O(A * C) where A is amount and C is the number of coins
# Space Complexity: O(A)
# Link: https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1]* (amount+1)

        dp[0]= 0
        for i in range(1, amount+1):
            for coin in coins:
                
                if i-coin>=0:
                    dp[i]= min(dp[i], dp[i-coin]+1)

        if dp[amount]== amount+1:
            return -1

        return dp[amount]
        

