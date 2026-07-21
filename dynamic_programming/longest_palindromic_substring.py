# Problem: Longest Palindromic Substring (#5)
# Difficulty: Medium
# Approach: Expand Around Center
# Pattern: Two Pointers, String
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        def expand_around_center(left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1

            return right-left-1

        start=end=0
        for i in range(len(s)):
            len1= expand_around_center(i,i)
            len2= expand_around_center(i,i+1)

            max_len= max(len1, len2)

            if max_len>end-start:
                start= i-(max_len-1)//2
                end= i+ max_len//2

        return s[start:end+1]
    
# Problem: Longest Palindromic Substring (#5)
# Difficulty: Medium
# Approach: Bottom-Up Dynamic Programming (2D Matrix)
# Pattern: Dynamic Programming, Palindromes
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Link: https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome(s):
    n = len(s)
    if n <= 1:
        return s
        
    dp = [[False] * n for _ in range(n)]
    
    longest_start = 0
    max_length = 1

    for i in range(n - 1, -1, -1):
        
        for j in range(i, n):

            if s[i] == s[j]:

                if j - i <= 2 or dp[i+1][j-1]:
                    dp[i][j] = True

                    current_length = j - i + 1
                    if current_length > max_length:
                        longest_start = i
                        max_length = current_length
                        
    return s[longest_start : longest_start + max_length]