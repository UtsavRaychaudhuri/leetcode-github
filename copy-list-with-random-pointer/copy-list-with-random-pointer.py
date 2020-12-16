​
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
​
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        headcopy=head
        while(head):
            tmp=head.next
            head.next=Node(head.val)
            head.next.next=tmp
            head=head.next.next
        head=headcopy
        while(head):
            if head.random:
                head.next.random=head.random.next
            head=head.next.next
        head=headcopy
        head=head.next
        while(head and head.next):
            head.next=head.next.next
            head=head.next
        return headcopy.next
        
                    
                
            
