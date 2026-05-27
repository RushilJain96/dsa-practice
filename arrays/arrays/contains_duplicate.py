# Problem: Contains Duplicate (#217)
# Difficulty: Easy
# Pattern: Set
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        myset= set(nums)
        
        m= len(myset)
        if(m==n):
            return False
        else:
            return True
        