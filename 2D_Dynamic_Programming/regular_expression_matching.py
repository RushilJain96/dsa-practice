# Problem: Regular Expression Matching (#10)
# Difficulty: Hard
# Approach: Bottom-Up 2D Dynamic Programming
# Pattern: Dynamic Programming, String Comparison, Wildcard Matching
# Time Complexity: O(m * n) where m = len(s) and n = len(p)
# Space Complexity: O(m * n) for the 2D DP array
# Link: https://leetcode.com/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    preceding_char = p[j - 2]
                    if preceding_char == s[i - 1] or preceding_char == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]