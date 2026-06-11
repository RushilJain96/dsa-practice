# Problem: Find Minimum in Rotated Sorted Array (#153)
# Difficulty: Medium
# Pattern: Binary Search (compare mid to high to find rotation point)
# Time Complexity: O(log n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        low=0
        high= n-1
        minimum=nums[0]
        while low<= high :
            mid= (low + high)//2
            minimum= min(nums[mid], minimum)
            if nums[mid]> nums[high]:
                low= mid+1
            else:
                high= mid-1

        return minimum
    


    class Solution(object):
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            n= len(nums)
            low=0
            high= n-1
            while low<high :
                mid= (low + high)//2
                if nums[mid]> nums[high]:
                    low= mid+1
                else:
                    high= mid

            return nums[low]
            