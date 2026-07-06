# Problem: Palindrome Partitioning (#131)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(n × 2^n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/palindrome-partitioning/

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(left, right):
            while left<right:
                if s[left]!= s[right]:
                    return False
                left+=1
                right-=1

            return True

        
        result=[]
        partition=[]

        def backtrack(start_index):
            if start_index== len(s):
                result.append(partition[:])
                return
            for end_index in range(start_index, len(s)):
                if is_palindrome(start_index, end_index):
                    partition.append(s[start_index:end_index+1])
                    
                    backtrack(end_index+1)
                    partition.pop()

        backtrack(0)
        return result
