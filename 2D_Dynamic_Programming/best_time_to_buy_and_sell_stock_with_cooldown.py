# Problem: Best Time to Buy and Sell Stock with Cooldown (#309)
# Difficulty: Medium
# Approach: State Machine Dynamic Programming
# Pattern: Dynamic Programming, State Machine
# Time Complexity: O(n) where n is the number of days
# Space Complexity: O(1) as we only use three variables
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        hold = -prices[0] # Bought the stock on day 0
        sold = 0          # Impossible to sell on day 0
        rest = 0          # Did nothing on day 0
        
        for i in range(1, len(prices)):
        
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            hold = max(prev_hold, prev_rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(prev_rest, prev_sold)
            
        return max(sold, rest)