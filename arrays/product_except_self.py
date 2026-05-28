# Problem: Product of Array Except Self (#238)
# Difficulty: Medium
# Pattern: Prefix and Suffix products
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output