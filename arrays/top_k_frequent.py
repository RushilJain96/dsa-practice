# Problem: Top K Frequent Elements (#347)
# Difficulty: Medium
# Pattern: Bucket Sort
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        for num, i in count.items():
            freq[i].append(num)
        result = []
        for j in range(len(freq) - 1, 0, -1):
            for num in freq[j]:
                result.append(num)
                if len(result) == k:
                    return result