# Problem: Two Sum (#1)
# Difficulty: Easy
# Pattern: Hashmap
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/two-sum/



class Solution:
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        return []