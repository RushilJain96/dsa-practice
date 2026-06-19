# Problem: Diameter of Binary Tree (#543)
# Difficulty: Easy
# Pattern: DFS + Height Computation
# Time Complexity: O(n)
# Space Complexity: O(h)
# Link: https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter=0

        def height( node):
            if not node:
                return 0
            left_height= height(node.left)
            right_height=height(node.right)
            self.diameter= max(self.diameter, left_height+right_height)
            
            return 1+ max(left_height, right_height)
        
        height( root)
        return self.diameter