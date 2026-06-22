# Problem: Binary Tree Right Side View (#199)
# Difficulty: Medium
# Pattern: BFS (Level Order Traversal)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue= deque([root])
        result= []
        while queue:
            level_size=len(queue)

            for i in range(level_size):
                node= queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i== level_size-1:
                    result.append(node.val)

        return result