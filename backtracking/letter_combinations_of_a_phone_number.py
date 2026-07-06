# Problem: Letter Combinations of a Phone Number (#17)
# Difficulty: Medium
# Pattern: Backtracking
# Time Complexity: O(n × 4^n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result=[]
        combination=[]
        def backtracking(index):
            if len(combination)== len(digits):
                result.append("".join(combination))
                return

            curr_digit= digits[index]
            letters= mapping[curr_digit]
            
            for letter in letters:
                combination.append(letter)
                backtracking(index+1)
                combination.pop()

        backtracking(0)
        return result
            
