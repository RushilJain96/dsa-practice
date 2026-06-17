# Problem: Add Two Numbers (#2)
# Difficulty: Medium
# Pattern: Dummy Node + Carry Handling
# Time Complexity: O(n) | Space Complexity: O(n)
# Link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        tail=dummy
        carry=0
        while l1 or l2 or carry:
            digit1= l1.val if l1 else 0
            digit2= l2.val if l2 else 0
            add= digit1+digit2+carry
            value= add%10
            carry= add//10
            tail.next= ListNode(value)
            tail=tail.next
            
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        

        return dummy.next

