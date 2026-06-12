# Problem: Median of Two Sorted Arrays (#4)
# Difficulty: Hard
# Pattern: Binary Search on partition point
# Time Complexity: O(log min(m,n)) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1)>len(nums2):
            nums1, nums2= nums2, nums1

        A, B= nums1, nums2
        total= len(nums1)+len(nums2)
        half= total//2
        left=0
        right= len(A)
        while True:
            i=(left+right)//2
            j= half-i

            Aleft= A[i-1] if i>0 else float("-inf")
            Aright= A[i] if i<len(A) else float("inf")

            Bleft= B[j-1] if j>0 else float("-inf")
            Bright= B[j] if j<len(B) else float("inf")


            if Aleft<= Bright and Aright>= Bleft:
                if total%2 ==0:
                    return (max(Aleft,Bleft)+ min(Aright, Bright))/2.0
                    
                else:
                    return float(min(Aright, Bright))

            elif Aleft>Bright:
                right=i-1
            else:
                left=i+1        


        