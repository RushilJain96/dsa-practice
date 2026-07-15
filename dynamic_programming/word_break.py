# Problem: Word Break (#139)
# Difficulty: Medium
# Approach: Bottom-Up Dynamic Programming (1D Array)
# Pattern: Dynamic Programming, String DP
# Time Complexity: O(n^3)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        word_set= set(wordDict)

        n= len(s)
        dp= [False]* (n+1)

        dp[0]= True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]= True

                    break
        
        return dp[n]