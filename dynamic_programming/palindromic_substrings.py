# Problem: Palindromic Substrings (#647)
# Difficulty: Medium
# Approach: Expand Around Center
# Pattern: Two Pointers, String
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/palindromic-substrings/

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0

        def count_palindromes_from_center(left, right):
            count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        
            return count

        total_pallindromes=0
        for i in range(len(s)):
            total_pallindromes+= count_palindromes_from_center(i,i)
            total_pallindromes+= count_palindromes_from_center(i,i+1)

        return total_pallindromes