# Problem: Maximum Depth of Binary Tree (#104)
# Difficulty: Easy
# Pattern: DFS Recursion (Height Calculation)
# Time Complexity: O(n)
# Space Complexity: O(h)
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        depth_left=1+ self.maxDepth(root.left)
        depth_right= 1+ self.maxDepth(root.right)

        return max(depth_left, depth_right)