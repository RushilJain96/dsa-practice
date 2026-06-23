# Problem: Validate Binary Search Tree (#98)
# Difficulty: Medium
# Pattern: DFS + Range Constraints
# Time Complexity: O(n)
# Space Complexity: O(h)
# Link: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node, low, high):

            if not node:
                return True

            if not(low< node.val< high):
                return False
            
            left= dfs(node.left, low, node.val)
            right= dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float('-inf'), float('+inf'))