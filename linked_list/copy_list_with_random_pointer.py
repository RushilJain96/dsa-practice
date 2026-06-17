# Problem: Copy List with Random Pointer (#138)
# Difficulty: Medium
# Pattern: Hashmap (old node to new node mapping)
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        old_to_new={}
        curr= head
        while curr:
            copy= Node(curr.val)
            old_to_new[curr]= copy
            curr= curr.next

        curr=head
        while curr:
            copy= old_to_new[curr]

            copy.next= old_to_new.get(curr.next)
            copy.random= old_to_new.get(curr.random)

            curr=curr.next

        return old_to_new[head]
