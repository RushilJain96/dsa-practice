# Problem: Find Median from Data Stream (#295)
# Difficulty: Hard
# Pattern: Two Heaps (Max Heap + Min Heap)
# Time Complexity:
#   addNum()     -> O(log n)
#   findMedian() -> O(1)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/find-median-from-data-stream/

import heapq
class MedianFinder(object):

    def __init__(self):
        self.maxHeap=[]
        self.minHeap=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.maxHeap or -self.maxHeap[0]>= num:
            heapq.heappush(self.maxHeap, -num)

        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap)> len(self.minHeap)+1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        
        elif len(self.minHeap)> len(self.maxHeap)+1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap)== len(self.maxHeap):
            return (self.minHeap[0]- self.maxHeap[0])/2.0
        
        elif len(self.minHeap)>len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()