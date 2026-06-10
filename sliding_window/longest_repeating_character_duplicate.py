# Problem: Longest Repeating Character Replacement (#424)
# Difficulty: Medium
# Pattern: Sliding Window (window size - max frequency <= k)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count= {}
        output=0
        max_freq=0
        left=0
        for i in range(len(s)):
           count[s[i]]= count.get(s[i],0)+1
           max_freq= max(max_freq, count[s[i]])

           while (i-left+1)- max_freq> k:
                count[s[left]]-=1
                left+=1

           output= max(output, i-left+1)
        
        return output