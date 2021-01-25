# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def helper(head):
            if head is None or head.next is None:
                return head
            noder=helper(head.next)
            head.next.next=head
            head.next=None
            return noder
            
        return helper(head)
