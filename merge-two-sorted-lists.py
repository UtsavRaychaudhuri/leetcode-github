# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node=ListNode()
        head=node
        if l1 is None or l2 is None:
            if l1:
                return l1
            else:
                return l2
        if l1.val<l2.val:
            node.val=l1.val
            l1=l1.next
        else:
            node.val=l2.val
            l2=l2.next
        while(l1 or l2):
            if l1 and l2:
                if l1.val<l2.val:
                    node.next=ListNode(l1.val)
                    node=node.next
                    l1=l1.next
                else:
                    node.next=ListNode(l2.val)
                    node=node.next
                    l2=l2.next
            elif l1 is not None:
                node.next=ListNode(l1.val)
                node=node.next
                l1=l1.next
            else:
                node.next=ListNode(l2.val)
                node=node.next
                l2=l2.next
