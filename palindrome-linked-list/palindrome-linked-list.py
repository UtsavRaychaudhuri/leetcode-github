# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.ptr=head
        self.ret=False
        def rec(head):
            if head is None or self.ret:
                return
            rec(head.next)
            if self.ptr.val==head.val:
                self.ptr=self.ptr.next
            else:
                self.ret=True
                return
        rec(head)
        return not self.ret
            
            
