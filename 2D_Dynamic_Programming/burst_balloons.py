# Problem: Burst Balloons (#312)
# Difficulty: Hard
# Approach: Bottom-Up 2D Dynamic Programming (Interval DP)
# Pattern: Dynamic Programming, Interval DP, Divide and Conquer
# Time Complexity: O(n^3) where n is the number of balloons (3 nested loops)
# Space Complexity: O(n^2) for the 2D DP array
# Link: https://leetcode.com/problems/burst-balloons/

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = [1] + nums + [1]
        n = len(A)
        
        dp = [[0] * n for _ in range(n)]
        
        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                for k in range(i + 1, j):
                    coins = dp[i][k] + (A[i] * A[k] * A[j]) + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)
                    
        return dp[0][n - 1]