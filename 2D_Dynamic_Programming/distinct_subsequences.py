# Problem: Distinct Subsequences (#115)
# Difficulty: Hard
# Approach: Bottom-Up 2D Dynamic Programming
# Pattern: Dynamic Programming, String Comparison, Subsequence Counting
# Time Complexity: O(m * n) where m is len(s) and n is len(t)
# Space Complexity: O(m * n) for the 2D DP array
# Link: https://leetcode.com/problems/distinct-subsequences/


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[m][n]