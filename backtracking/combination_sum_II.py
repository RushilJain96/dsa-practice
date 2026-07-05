# Problem: Combination Sum II (#40)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()

        result = []
        combination = []

        def backtrack(start, remaining):
            # Base Case
            if remaining == 0:
                result.append(combination.copy())
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                combination.append(candidates[i])

                backtrack(i + 1, remaining - candidates[i])

                combination.pop()

        backtrack(0, target)
        return result


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        combination=[]
        candidates.sort()
        def backtrack(i, sum):
            if sum==target:
                result.append(combination[:])
                return
            if sum>target:
                return
            
            if i== len(candidates):
                return
            
            newSum= sum+ candidates[i]

            combination.append(candidates[i])
            backtrack(i+1, newSum)
            combination.pop()
            while i+1<len(candidates) and candidates[i]== candidates[i+1]:
                i+=1
            backtrack(i+1, sum)

        backtrack(0,0)
        return result