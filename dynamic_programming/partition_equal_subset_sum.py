# Problem: Partition Equal Subset Sum (#416)
# Difficulty: Medium
# Approach: Bottom-Up Dynamic Programming (1D Space Optimized 0/1 Knapsack)
# Pattern: Dynamic Programming, Subset Sum
# Time Complexity: O(n * target) where n is array length and target is sum/2
# Space Complexity: O(target)
# Link: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum= sum(nums)

        if total_sum%2!=0:
            return False

        target= total_sum//2

        dp= [False]* (target+1)
        dp[0]= True

        for num in nums:
            for i in range(target, num-1, -1):
                if dp[i-num]:
                    dp[i]= True

            if dp[target]:
                return True

        return dp[target]