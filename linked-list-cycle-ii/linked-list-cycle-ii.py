# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def findcycle(head):
            while(self.slow is not None and self.fast is not None):
                if self.slow.next:
                    self.slow=self.slow.next
                else:
                    return False
                if self.fast.next and self.fast.next.next:
                    self.fast=self.fast.next.next
                else:
                    return False
                if self.slow==self.fast:
                    return self.slow
        self.slow=self.fast=head
        if not findcycle(head):
            return None
        self.slow,self.fast=head,self.slow
        while(self.slow!=self.fast):
            self.slow=self.slow.next
            self.fast=self.fast.next
        return self.slow
        
                
            
