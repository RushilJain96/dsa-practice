# Problem: Remove Nth Node From End (#19)
# Difficulty: Medium
# Pattern: Two Pointer Gap Technique + Dummy Node
# Time Complexity: O(n) | Space Complexity: O(1)
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        length=0
        curr=head
        
        while curr:
            curr=curr.next
            length+=1
        
        dummy= ListNode(0)
        dummy.next= head
        curr= dummy

        for _ in range(length-n):
            curr= curr.next

        curr.next= curr.next.next

        return dummy.next
        

def removeNthFromEnd(self, head, n):
    dummy = ListNode(0)
    dummy.next = head
    left = dummy
    right = head

    
    for _ in range(n):
        right = right.next

    
    while right:
        left = left.next
        right = right.next

    
    left.next = left.next.next
    return dummy.next