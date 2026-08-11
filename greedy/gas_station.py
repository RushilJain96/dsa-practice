# Problem: Gas Station (#134)
# Difficulty: Medium
# Approach: Greedy (Prefix Reset + Global Check)
# Pattern: Greedy, Array
# Time Complexity: O(n) where n is the number of stations (single pass)
# Space Complexity: O(1) using constant extra space
# Link: https://leetcode.com/problems/gas-station/

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
            
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index