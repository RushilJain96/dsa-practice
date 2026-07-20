# Problem: Min Cost Climbing Stairs (#746)
# Difficulty: Easy / Medium
# Approach: Space-Optimized Dynamic Programming
# Pattern: Dynamic Programming, Fibonacci-style
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n= len(cost)

        one_back=0
        two_back=0

        for i in range(2, n+1):

            jump_two= two_back+ cost[i-2]
            jump_one= one_back+ cost[i-1]

            min_reach_cost= min(jump_one, jump_two)

            two_back= one_back
            one_back= min_reach_cost

        return one_back