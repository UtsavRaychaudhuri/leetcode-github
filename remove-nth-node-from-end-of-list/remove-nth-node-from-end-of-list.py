# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.idx=1
        self.removed=False
        def remove(head):
            if head is None or self.removed:
                return
            remove(head.next)
            if self.idx==n+1:
                head.next=head.next.next
                self.removed=True
            self.idx+=1
        remove(head)
        if not self.removed:
            return head.next
            self.idx+=1
        return head
            
