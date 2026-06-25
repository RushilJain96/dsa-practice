# Problem: Task Scheduler (#621)
# Difficulty: Medium
# Pattern: Greedy + Max Heap + Queue (Cooldown Simulation)
# Time Complexity: O(n)
# Space Complexity: O(1) (or O(26) for uppercase English letters)
# Link: https://leetcode.com/problems/task-scheduler/

from collections import Counter, heapq, deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count= Counter(tasks)
        maxHeap=[]
        q= deque()
        time=0 
        maxHeap= [-freq for freq in count.values()]
        heapq.heapify(maxHeap)
            
        while maxHeap or q:
            time+=1
            if maxHeap:
                freq= heapq.heappop(maxHeap)
                freq+=1
                if freq!=0:
                    q.append((freq, time+n))

            if q and time==q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])


        return time   