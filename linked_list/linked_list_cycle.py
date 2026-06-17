# Problem: Linked List Cycle (#141)
# Difficulty: Easy
# Pattern: Floyd's Cycle Detection (slow/fast pointers)
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next==None:
            return False

        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True

        return False