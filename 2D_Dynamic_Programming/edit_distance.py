# Problem: Edit Distance (#72)
# Difficulty: Hard
# Approach: Bottom-Up 2D Dynamic Programming
# Pattern: Dynamic Programming, String Transformation
# Time Complexity: O(m * n) where m is len(word1) and n is len(word2)
# Space Complexity: O(m * n) for the 2D DP table
# Link: https://leetcode.com/problems/edit-distance/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
  
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                   
                    dp[i][j] = 1 + min(
                        dp[i - 1][j - 1],  
                        dp[i - 1][j],      
                        dp[i][j - 1]       
                    )
                    
      
        return dp[m][n]