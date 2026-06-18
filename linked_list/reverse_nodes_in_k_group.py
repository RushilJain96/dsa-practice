# Problem: Reverse Nodes in K-Group (#25)
# Difficulty: Hard
# Pattern: Linked List Segment Reversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):

    def getKth(self, curr, k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next= head
        groupPrev= dummy
        while True:
            kth= self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext= kth.next

            prev= kth.next
            curr= groupPrev.next
            while curr!= groupNext:
                nxt= curr.next
                curr.next=prev
                prev= curr
                curr= nxt

            tmp= groupPrev.next
            groupPrev.next=kth
            groupPrev= tmp
        return dummy.next
