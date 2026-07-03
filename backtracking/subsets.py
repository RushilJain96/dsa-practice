# Problem: Subsets (#78)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(n × 2^n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        subset=[]
        def backtrack(i):
            if i== len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return result