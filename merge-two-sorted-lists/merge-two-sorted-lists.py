# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        tmp=dummy
        while(l1 or l2):
            if l1 and l2 and l1.val<=l2.val:
                dummy.next=l1
                l1=l1.next
            elif l1 and l2 and l2.val<=l1.val:
                dummy.next=l2
                l2=l2.next
            elif l1:
                dummy.next=l1
                l1=l1.next
            else:
                dummy.next=l2
                l2=l2.next
            dummy=dummy.next
        return tmp.next
            
            
                
