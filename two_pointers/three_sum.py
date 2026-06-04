# Problem: 3Sum (#15)
# Difficulty: Medium
# Pattern: Two Pointers + Sort + Skip Duplicates
# Time Complexity: O(n²) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output=[]
        for i in range (len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right= len(nums)-1

            while left<right:
                total= nums[i]+ nums[left]+ nums[right]

                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    left+=1

                    while left<right and nums[left]== nums[left-1] :
                        left+=1



        return output
