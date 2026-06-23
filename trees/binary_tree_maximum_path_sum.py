# Problem: Binary Tree Maximum Path Sum (#124)
# Difficulty: Hard
# Pattern: DFS + Global Answer + Return Best Branch
# Time Complexity: O(n)
# Space Complexity: O(h)
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.weight=root.val
        def maxPath(node):
            if not node:
                return 0

            left_weight= max(maxPath(node.left),0)
            right_weight= max(maxPath(node.right),0)
            self.weight= max(self.weight, left_weight+node.val+right_weight)
             
            return node.val+max(left_weight, right_weight)

        maxPath(root)
        return self.weight
        