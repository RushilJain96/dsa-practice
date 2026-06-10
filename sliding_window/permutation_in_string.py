# Problem: Permutation in String (#567)
# Difficulty: Medium
# Pattern: Sliding Window (fixed size window, frequency array comparison)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left=0
        right=len(s1)
        if len(s1)>len(s2):
            return False

        s1count= [0]*26
        s2count= [0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i])- ord('a')]+=1
            s2count[ord(s2[i])- ord('a')]+=1

        if s1count== s2count:
            return True
        
        left=0

        for right in range(len(s1), len(s2)):
            s2count[ord(s2[right])- ord('a')]+=1
            s2count[ord(s2[left])-ord('a')]-=1
            left+=1

            if s1count== s2count:
                return True

        return False