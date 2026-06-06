# Problem: Best Time to Buy and Sell Stock (#121)
# Difficulty: Easy
# Pattern: Sliding Window (track running minimum)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        smallest= prices[0]
        for i in range(len(prices)):
            smallest= min(smallest, prices[i])
            max_profit=max(max_profit, prices[i]- smallest) 

        return max_profit