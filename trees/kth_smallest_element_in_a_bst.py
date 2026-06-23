# Problem: Kth Smallest Element in a BST (#230)
# Difficulty: Medium
# Pattern: Inorder Traversal (BST)
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        inorder=[]
        
        def inOrderTraversal(root):

            if not root:
                return 
            
            inOrderTraversal(root.left)
            inorder.append(root.val)
            inOrderTraversal(root.right)

        inOrderTraversal(root)
        return inorder[k-1]