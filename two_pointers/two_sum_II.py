# Problem: Two Sum II - Input Array Is Sorted (#167)
# Difficulty: Medium
# Pattern: Two Pointers (move based on sum vs target)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1
        while numbers[left]+ numbers[right]!= target :
            if numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1

        
        return [left+1, right+1]
        
