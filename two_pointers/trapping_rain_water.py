# Problem: Trapping Rain Water (#42)
# Difficulty: Hard
# Pattern: Two Pointers (track max_left and max_right)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_left=max_right=0
        water=0
        while left<right:
            if height[left]< height[right]:
                max_left= max(max_left, height[left])
                water+= max_left- height[left]
                left+=1
            else:
                max_right= max(max_right, height[right])
                water+= max_right- height[right]
                right-=1
                
        return water 
        