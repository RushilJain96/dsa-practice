# Problem: Search a 2D Matrix (#74)
# Difficulty: Medium
# Pattern: Binary Search (treat matrix as flat sorted array)
# Time Complexity: O(log m*n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        low= 0
        high= len(matrix)-1

        while low<= high:
            mid= (low+high)//2
            if matrix[mid][0]<= target <= matrix[mid][-1]:
                innerLow= 0
                innerHigh= len(matrix[mid])-1
                while(innerLow <= innerHigh):
                    innerMid= (innerLow+ innerHigh)//2
                    if target== matrix[mid][innerMid]:
                        return True
                    elif target<matrix[mid][innerMid]:
                        innerHigh= innerMid-1
                    else:
                        innerLow= innerMid+1
                return False
            

            elif target< matrix[mid][0]:
                high=mid-1
            elif target> matrix[mid][len(matrix[mid])-1]:
                low= mid+1

        return False
    


    def searchMatrix(self, matrix, target):  #alternative and better solution by considering whole as one 
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False