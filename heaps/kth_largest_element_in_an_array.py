# Problem: Kth Largest Element in an Array (#215)
# Difficulty: Medium
# Pattern: Min Heap of Size K / Quick Select
# Time Complexity: O(n log k) Heap, O(n) Average Quick Select
# Space Complexity: O(k) Heap, O(1) Quick Select
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap=[]
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)

        return heap[0]