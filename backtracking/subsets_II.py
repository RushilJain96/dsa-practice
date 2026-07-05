# Problem: Subsets II (#90)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(n × 2^n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/subsets-ii/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset=[]
        result=[]
        nums.sort()
        def backtrack(i):
            if i== len(nums): 
                result.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            while i+1<len(nums) and nums[i]== nums[i+1]:
                i+=1
            backtrack(i+1)
        
        backtrack(0)
        return result