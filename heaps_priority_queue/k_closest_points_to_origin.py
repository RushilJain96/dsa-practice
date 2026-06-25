# Problem: K Closest Points to Origin (#973)
# Difficulty: Medium
# Pattern: Fixed Size Max Heap (Top K Elements)
# Time Complexity: O(n log k)
# Space Complexity: O(k)
# Link: https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap=[]
        for i in range(len(points)):
            x,y= points[i]
            dist= x*x +y*y
                    
            heapq.heappush(heap, (-dist, points[i]))
            if len(heap)>k:
                heapq.heappop(heap)

        return [point for dist, point in heap]

            