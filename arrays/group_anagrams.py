# Problem: Group Anagrams (#49)
# Difficulty: Medium
# Pattern: Hashmap - group by shared property as key
# Time Complexity: O(n·k) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

# Approach 1 - Sort word as key
# Time: O(n·k log k) | Simple and clean
class Solution_v1(object):
    def groupAnagrams(self, strs):
        group = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            group[key].append(word)
        return list(group.values())

# Approach 2 - Frequency array as key (optimal)
# Time: O(n·k) | Avoids sorting entirely
class Solution_v2(object):
    def groupAnagrams(self, strs):
        group = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            group[tuple(freq)].append(word)
        return list(group.values())