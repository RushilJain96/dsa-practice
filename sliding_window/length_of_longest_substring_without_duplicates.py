# Problem: Longest Substring Without Repeating Characters (#3)
# Difficulty: Medium
# Pattern: Sliding Window (expand right, shrink left on duplicate)
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window= set()
        left=0
        length=0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            
            window.add(s[right])
            length= max(length, right-left+1)

        return length