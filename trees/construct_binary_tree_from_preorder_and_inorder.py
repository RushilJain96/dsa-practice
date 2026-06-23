# Problem: Construct Binary Tree from Preorder and Inorder Traversal (#105)
# Difficulty: Medium
# Pattern: DFS Recursion + Tree Reconstruction
# Time Complexity: O(n²)   # slicing solution
# Space Complexity: O(n²)
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None

        root= TreeNode(preorder[0])
        root_indx= inorder.index(preorder[0])

        root.left= self.buildTree(preorder[1:root_indx+1], inorder[0:root_indx])

        root.right= self.buildTree(preorder[root_indx+1:], inorder[root_indx+1:])

        return root


# Problem: Construct Binary Tree from Preorder and Inorder Traversal (#105)
# Difficulty: Medium
# Pattern: DFS Recursion + Tree Reconstruction
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


class Solution(object):                           #More Optimized Solution- O(n) space and time
    def buildTree(self, preorder, inorder):

        inorder_map = {}

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        self.pre_idx = 0

        def build(left, right):

            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)