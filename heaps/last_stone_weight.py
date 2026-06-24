# Problem: Last Stone Weight (#1046)
# Difficulty: Easy
# Pattern: Max Heap (Simulated with Negative Values)
# Time Complexity: O(n log n)
# Space Complexity: O(1) Extra Space
# Link: https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i]=-stones[i]

        heapq.heapify(stones)

        while len(stones)>1:
            x= heapq.heappop(stones)
            y= heapq.heappop(stones)
            if x==y:
                continue
            if x!=y:
                heapq.heappush(stones, x-y)
            
            if len(stones)==1:
                return -stones[0]
        
        return 0