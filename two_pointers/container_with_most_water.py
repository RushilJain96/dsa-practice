# Problem: Container With Most Water (#11)
# Difficulty: Medium
# Pattern: Two Pointers (move smaller height inward)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        left=0
        right= len(height)-1
        while left<right:
            area= max((right-left)*min(height[left], height[right]), area)
            if height[left]>height[right]:
                right-=1
                
            elif height[right]>height[left]:
                left+=1
                
            else:
                left+=1
        return area