# Problem: Unique Paths (#62)
# Difficulty: Medium
# Approach: Bottom-Up 2D Dynamic Programming
# Pattern: Dynamic Programming, Grid
# Time Complexity: O(m * n) where m is rows and n is columns
# Space Complexity: O(m * n) for the 2D DP array
# Link: https://leetcode.com/problems/unique-paths/

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp= [[1]*n for _ in range (m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i-1][j]+ dp[i][j-1]

        return dp[m-1][n-1]


# Problem: Unique Paths (#62)
# Difficulty: Medium
# Approach: Bottom-Up 1D Dynamic Programming (Space Optimized)
# Pattern: Dynamic Programming, Grid, Space Optimization
# Time Complexity: O(m * n) where m is rows and n is columns
# Space Complexity: O(n) because we only store one row of size n
# Link: https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                # dp[j] (new value) = dp[j] (old value, from row above) + dp[j-1] (new value, from left)
                dp[j] += dp[j-1]
                
        return dp[-1]