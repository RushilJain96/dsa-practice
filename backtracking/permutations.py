# Problem: Permutations (#46)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(n × n!)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        permutation=[]
        visited=set()
        def backtrack():
            if len(permutation)== len(nums):
                result.append(permutation[:])
                return
            
            for num in nums:
                if num in visited:
                    continue

                permutation.append(num)
                visited.add(num)
                backtrack()

                permutation.pop()
                visited.remove(num)

        backtrack()
        return result
            
