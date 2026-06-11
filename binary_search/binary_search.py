# Problem: Binary Search (#704)
# Difficulty: Easy
# Pattern: Binary Search
# Time Complexity: O(log n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high= len(nums)-1
        
        
        while(low<= high):
            mid= (low+high)//2
            if target== nums[mid]:
                return mid
            elif target> nums[mid]:
                low= mid+1
            else:
                high=mid-1

        return -1