# Problem: Longest Common Subsequence (#1143)
# Difficulty: Medium
# Approach: Bottom-Up 2D Dynamic Programming
# Pattern: Dynamic Programming, String Comparison
# Time Complexity: O(m * n) where m is length of text1 and n is length of text2
# Space Complexity: O(m * n) for the 2D DP array
# Link: https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m,n= len(text1), len(text2)

        dp= [[0]*(n+1) for _ in range (m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):

                if text1[i-1]== text2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]

                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]