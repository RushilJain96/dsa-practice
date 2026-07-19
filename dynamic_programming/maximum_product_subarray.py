# Problem: Maximum Product Subarray (#152)
# Difficulty: Medium
# Approach: Space-Optimized Dynamic Programming (Kadane's adaptation)
# Pattern: Dynamic Programming, Subarray
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        current_max= nums[0]
        current_min= nums[0]
        global_max= nums[0]

        for i in range(1, len(nums)):
            num= nums[i]

            temp_max= max(current_max* num, num, current_min*num)
            current_min= min(num, current_max*num, current_min*num)

            current_max= temp_max
            global_max= max(global_max, current_max)

        return global_max