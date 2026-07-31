# Problem: Interleaving String (#97)
# Difficulty: Medium
# Approach: Bottom-Up 2D Dynamic Programming
# Pattern: Dynamic Programming, String Comparison, Grid Traversal
# Time Complexity: O(m * n) where m = len(s1) and n = len(s2)
# Space Complexity: O(m * n) for the 2D DP array
# Link: https://leetcode.com/problems/interleaving-string/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False
            
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                match_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                
                dp[i][j] = match_s1 or match_s2
                
        return dp[m][n]