# Problem: Minimum Window Substring (#76)
# Difficulty: Hard
# Pattern: Sliding Window (expand right until valid, shrink left to minimize)
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/minimum-window-substring/
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t)> len(s):
            return ""
        
        countT= Counter(t)
        have=0
        need= len(countT)
        window={}
        left=0
        res_len= float("inf")
        res=[-1,-1]
        
        for right in range(len(s)):
            window[s[right]]= window.get(s[right],0)+1
            if s[right] in countT and window[s[right]]== countT[s[right]]:
                have+=1
                while have== need:
                    if (right-left+1)< res_len:
                        res_len= right-left+1
                        res=[left, right]

                    window[s[left]]-=1
                                                                    
                    if s[left] in countT and( window[s[left]]< countT[s[left]]):
                        have-=1

                    left+=1

        l,r = res
        
        return s[l:r+1] 