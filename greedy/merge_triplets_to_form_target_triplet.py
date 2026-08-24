# Problem: Merge Triplets to Form Target Triplet (#1899)
# Difficulty: Medium
# Approach: Greedy (Filter and Accumulate)
# Pattern: Greedy, Array
# Time Complexity: O(n) where n is the number of triplets
# Space Complexity: O(1) using three boolean variables
# Link: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

class Solution:
    def mergeTriplets(self, triplets, target):
        found_a = False
        found_b = False
        found_c = False
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
                
            if t[0] == target[0]:
                found_a = True
            if t[1] == target[1]:
                found_b = True
            if t[2] == target[2]:
                found_c = True
                
            if found_a and found_b and found_c:
                return True
                
        return found_a and found_b and found_c