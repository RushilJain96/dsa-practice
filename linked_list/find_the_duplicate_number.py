# Problem: Find the Duplicate Number (#287)
# Difficulty: Medium
# Pattern: Floyd's Cycle Detection (array as implicit linked list)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=0
        while True:
            slow= nums[slow]
            fast= nums[nums[fast]]
            if slow==fast:
                break
        
        slow=0
        while slow!= fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow


         
        
