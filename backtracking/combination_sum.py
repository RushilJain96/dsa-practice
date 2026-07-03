# Problem: Combination Sum (#39)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(2^(T/m)) (approximate, where T = target and m = smallest candidate)
# Space Complexity: O(T/m)
# Link: https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        combination=[]
        def backtracking(i, sum):
            if sum== target:
                result.append(combination[:])
                return
            if i== len(candidates):
                return
            if sum> target:
                return
            newSum= sum+ candidates[i]
            
            combination.append(candidates[i])
            backtracking(i, newSum)
             
            combination.pop()
            backtracking(i+1, sum)

        backtracking(0, 0)
        return result


            