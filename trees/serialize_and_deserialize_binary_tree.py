# Problem: Serialize and Deserialize Binary Tree (#297)
# Difficulty: Hard
# Pattern: BFS (Level Order Traversal) + Tree Reconstruction
# Time Complexity: O(n)
# Space Complexity: O(n)
# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue= deque([root])
        res=[]
        while queue:
            node= queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N") 

        return ",".join(res)       

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals= data.split(",")
        root= TreeNode(int(vals[0]))
        q= deque([root])
        i=1
        while q:
            node=q.popleft()

            if vals[i]!="N":
                node.left= TreeNode(int(vals[i]))
                q.append(node.left)

            i+=1

            if vals[i]!="N":
                node.right= TreeNode(int(vals[i]))
                q.append(node.right)
            i+=1
        return root              

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))