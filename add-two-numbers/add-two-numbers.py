#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
​
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=""
        b=""
        head=l1
        head1=l2
        while l1!=None:
            a= str(l1.val) + a
            l1 = l1.next
​
        while l2!=None:
            b= str(l2.val) + b
            l2 = l2.next
​
        total = str(int(a)+int(b))
        head,new_node = None,None
        for i in total:
            if head is None:
                head = ListNode(int(i))
            else:
                new_node = ListNode(int(i))
