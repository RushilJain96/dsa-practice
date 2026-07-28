# Problem: Target Sum (#494)
# Difficulty: Medium
# Approach: Math Reduction to Subset Sum + 1D Dynamic Programming
# Pattern: Dynamic Programming, 0/1 Knapsack
# Time Complexity: O(n * P) where n is array length and P is subset target sum
# Space Complexity: O(P) for the 1D DP array
# Link: https://leetcode.com/problems/target-sum/

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)

        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0
            
        subset_target = (total_sum + target) // 2

        dp = [0] * (subset_target + 1)
        dp[0] = 1 
        
        for num in nums:
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_target]