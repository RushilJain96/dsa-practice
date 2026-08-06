# Problem: Maximum Subarray (#53)
# Difficulty: Medium
# Approach: Kadane's Algorithm (Greedy Prefix Reset)
# Pattern: Greedy, Array, Dynamic Programming
# Time Complexity: O(n) where n is the number of elements in the array (single pass)
# Space Complexity: O(1) using constant extra space for tracking running sums
# Link: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum= nums[0]
        current_sum=0

        for num in nums:
            current_sum+=num

            max_sum= max(max_sum, current_sum)

            if current_sum<0:
                current_sum=0

        return max_sum
        