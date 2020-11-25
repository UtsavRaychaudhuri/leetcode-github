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
        myhead=Node(-1)
        returnhead=myhead
        rheadc=myhead
        headc=head
        d=dict()
        l=[]
        r=dict()
        i=0
        while(head!=None):
            d[head]=i
            myhead.next=Node(head.val)
            myhead=myhead.next
            l.append(myhead)
            head=head.next
            i+=1
        rheadc=rheadc.next
        while(headc!=None):
            if headc.random is not None:
                rheadc.random=l[d[headc.random]]
            headc=headc.next
            rheadc=rheadc.next
        return returnhead.next
                    
                
            
