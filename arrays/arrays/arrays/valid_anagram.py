# Problem: Valid Anagram (#242)
# Difficulty: Easy
# Pattern: Counter / Hashmap
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/valid-anagram/
from collections import  Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s)==Counter(t)
        