# Problem: Subtree of Another Tree (#572)
# Difficulty: Easy
# Pattern: DFS Search + Tree Comparison
# Time Complexity: O(m * n)
# Space Complexity: O(h)
# Link: https://leetcode.com/problems/subtree-of-another-tree/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSameTree(p,q):
            if not p and not q :
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False

            left= isSameTree(p.left, q.left)
            right= isSameTree(p.right, q.right)

            return left and right 
        
        if not root:
            return False
        
        if isSameTree(root, subRoot):
            return True
        
        left= self.isSubtree(root.left, subRoot)
        right= self.isSubtree(root.right, subRoot)

        return left or right