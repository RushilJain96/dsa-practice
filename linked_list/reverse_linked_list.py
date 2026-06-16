# Problem: Reverse Linked List (#206)
# Difficulty: Easy
# Pattern: Three Pointer Reversal (prev, curr, next)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev= None
        curr= head
        while curr:
            nxt= curr.next
            curr.next=prev
            prev=curr
            curr= nxt
        return prev