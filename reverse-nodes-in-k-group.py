# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def __init__(self):
        self.chainthislist=ListNode(0)
        self.returnthislist=self.chainthislist
        self.new_head=None
        self.msg=False
        self.lastiter=False
​
    def reverseKGroup(self,head,k):
        self.new_head=head
        if not head:
            return None
        if head.next is None:
            return head 
        try:
            self.callmerecursive(head,k,0)
            return self.returnthislist.next
        finally:
            self.__init__()
​
    def callmerecursive(self,head,k,m):
        if head==None:
            self.msg=False
            return
        if k==m:
            self.new_head=head
            self.msg=True
            return
        self.callmerecursive(head.next,k,m+1)
        if self.msg:
            self.chainthislist.next=ListNode(head.val)
            self.chainthislist=self.chainthislist.next
            if m==0:
                head=self.new_head
                self.callmerecursive(head,k,0)
        elif not self.msg:
            if m==0:
                if self.new_head:
                    self.chainthislist.next=ListNode(self.new_head.val)
                    self.chainthislist=self.chainthislist.next
                return
            if m+1==k:
                self.lastiter=True
            if self.lastiter:
                self.chainthislist.next=ListNode(head.val)
                self.chainthislist=self.chainthislist.next
            else:
                while self.new_head!=None:
                    self.chainthislist.next=ListNode(self.new_head.val)
