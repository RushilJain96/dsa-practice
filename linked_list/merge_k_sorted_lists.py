# Problem: Merge K Sorted Lists (#23)
# Difficulty: Hard
# Pattern: Divide & Conquer (Merge Sort) + Merge Two Sorted Lists
# Time Complexity: O(N log K)
# Space Complexity: O(1) Extra Space
# Link: https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        dummy= ListNode(0)
        tail= dummy
        while l1 and l2:
            if l1.val<= l2.val:
                tail.next=l1
                l1= l1.next
            else:
                tail.next= l2
                l2= l2.next
            tail=tail.next
        if l1:
            tail.next= l1
        if l2:
            tail.next=l2

        return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
       
        
        if not lists:
            return None

        while len(lists)>1:
            mergedLists=[]
            for i in range (0, len(lists), 2):
                l1= lists[i]
                if i+1<len(lists):
                    l2= lists[i+1]
                else:
                    l2= None
                mergedLists.append(self.mergeTwoLists(l1,l2))
                
            lists=mergedLists

        return lists[0]