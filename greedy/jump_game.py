# Problem: Jump Game (#55)
# Difficulty: Medium
# Approach: Greedy (Track furthest reachable index)
# Pattern: Greedy, Array
# Time Complexity: O(n) where n is the length of the array (single pass)
# Space Complexity: O(1) as we only use a single variable for tracking
# Link: https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums):
        farthest = 0
        last_index = len(nums) - 1
        
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + jump)
            
            if farthest >= last_index:
                return True
                
        return True