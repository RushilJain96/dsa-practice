# Problem: Jump Game II (#45)
# Difficulty: Medium
# Approach: Greedy (Implicit BFS / Zone Expansion)
# Pattern: Greedy, Array
# Time Complexity: O(n) where n is the length of the array (single pass)
# Space Complexity: O(1) as we only use a few tracking variables
# Link: https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums):
    
        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1            
                current_end = farthest 
                
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps