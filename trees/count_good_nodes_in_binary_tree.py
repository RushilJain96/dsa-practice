# Problem: Count Good Nodes in Binary Tree (#1448)
# Difficulty: Medium
# Pattern: DFS + Information Propagation
# Time Complexity: O(n)
# Space Complexity: O(h)
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_so_far):
            if not node:
                return 0
            good= 0
            if node.val>= max_so_far:
                good=1
            max_so_far= max(max_so_far, node.val)

            left= dfs(node.left, max_so_far)
            right= dfs(node.right, max_so_far)

            return good+left+right

        return dfs(root, root.val)