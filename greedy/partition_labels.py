# Problem: Partition Labels (#763)
# Difficulty: Medium
# Approach: Greedy (Track furthest last occurrence)
# Pattern: Greedy, Hash Table, Two Pointers
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(1) as the hash map stores at most 26 lowercase English letters
# Link: https://leetcode.com/problems/partition-labels/

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        result = []
        size = 0
        end = 0
        
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_occurrence[char])
            
            if i == end:
                result.append(size)
                size = 0  
                
        return result