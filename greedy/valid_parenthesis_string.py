# Problem: Valid Parenthesis String (#678)
# Difficulty: Medium
# Approach: Greedy (Track Range of Open Parentheses)
# Pattern: Greedy, String
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(1) as we only use two variables
# Link: https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0 
        max_open = 0  

        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1

            elif char == ')':
                min_open -= 1
                max_open -= 1

            elif char == '*':
                min_open -= 1
                max_open += 1

            if max_open < 0:
                return False
                
            min_open = max(min_open, 0)
            
        return min_open == 0