# Problem: Valid Palindrome (#125)
# Difficulty: Easy
# Pattern: Two Pointers (inward from both ends)
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/valid-palindrome/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s= [c.lower() for c in s if c.isalnum()]
        left= 0
        right= len(new_s)-1
        while left<right:
            if(new_s[left]==new_s[right]):
                left+=1
                right-=1
            else:
                return False
        return True