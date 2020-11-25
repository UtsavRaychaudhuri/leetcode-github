# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        my_heap=[]
        if len(lists)==0:
            return
        res=[]
        for i,v in enumerate(lists):
            if v:
                my_heap.append([v.val,i])
        heapq.heapify(my_heap)
        if not my_heap:
            return
        val,idx=heapq.heappop(my_heap)
        node=ListNode(val)
        if lists[idx].next:
            heapq.heappush(my_heap,[lists[idx].next.val,idx])
            lists[idx]=lists[idx].next
        head=node
        while(my_heap):
            val,idx=heapq.heappop(my_heap)
            node.next=ListNode(val)
            if lists[idx].next:
                heapq.heappush(my_heap,[lists[idx].next.val,idx])
                lists[idx]=lists[idx].next
            node=node.next
        return head
        
                            
            
        
