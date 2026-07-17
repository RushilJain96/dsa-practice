# Problem: Decode Ways (#91)
# Difficulty: Medium
# Approach: Bottom-Up Dynamic Programming (1D Array)
# Pattern: Dynamic Programming, String DP
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        
        n= len(s)
        dp= [0]* (n+1)

        dp[0]=1
        dp[1]=1

        for i in range(2, n+1):
            single_digit= int(s[i-1:i])
            double_digit= int(s[i-2:i])

            if single_digit!=0:
                dp[i]+=dp[i-1]
                
            if 10<= double_digit <=26:
                dp[i]+=dp[i-2]

        return dp[n]
    
# Problem: Decode Ways (#91)
# Difficulty: Medium
# Approach: Space-Optimized Dynamic Programming
# Pattern: Dynamic Programming, String DP
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        
        n= len(s)
        
        one_back=1
        two_back=1

        for i in range(2, n+1):
            curr=0
            single_digit= int(s[i-1:i])
            double_digit= int(s[i-2:i])

            if single_digit!=0:
                curr+=one_back
                
            if 10<= double_digit <=26:
                curr+=two_back

            two_back=one_back
            one_back= curr

        return one_back