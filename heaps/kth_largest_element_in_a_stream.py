# Problem: Kth Largest Element in a Stream (#703)
# Difficulty: Easy
# Pattern: Min Heap of Size K
# Time Complexity: O(log k) per add()
# Space Complexity: O(k)
# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.heap=nums

        heapq.heapify(self.heap)
        while len(self.heap)>self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        
        if len(self.heap)>self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)