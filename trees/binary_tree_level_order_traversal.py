# Problem: Binary Tree Level Order Traversal (#102)
# Difficulty: Medium
# Pattern: BFS (Queue)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue= deque([root])
        result=[]
        while queue:
            level_size= len(queue)
            level=[]
            for i in range(level_size):
                node= queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(level)  

        return result