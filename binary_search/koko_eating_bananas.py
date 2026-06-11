# Problem: Koko Eating Bananas (#875)
# Difficulty: Medium
# Pattern: Binary Search on Answer Range
# Time Complexity: O(n log m) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/koko-eating-bananas/

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        low= 1
        hours=0
        high= max(piles)
        while low<=high:
            hours=0
            k= (low+high)//2
            for i in range(len(piles)):
                hours+=(piles[i]+k-1)//k

            if hours<=h:
                result=k
                high=k-1
               
            elif hours>h:
                low= k+1

        return result
                
            
                