# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode()
        tmp=head
        carry=0
        while(l1 or l2):
            if l1 and l2:
                tmp.next=ListNode((l1.val+l2.val+carry)%10)
                if l1.val+l2.val+carry>9:
                    carry=1
                else:
                    carry=0
                tmp,l1,l2=tmp.next,l1.next,l2.next
            elif l1:
                tmp.next=ListNode((l1.val+carry)%10)
                if l1.val+carry>9:
                    carry=1
                else:
                    carry=0
                tmp,l1=tmp.next,l1.next
            elif l2:
                tmp.next=ListNode((l2.val+carry)%10)
                if l2.val+carry>9:
                    carry=1
                else:
                    carry=0
                tmp,l2=tmp.next,l2.next
        if carry>0:
            tmp.next=ListNode(1)
        return head.next
                
                
        
