"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def conn(root,arr,i):
            if root is None:
                return
            if i<len(arr) and arr[i]!=root:
                arr[i].next=root
                arr[i]=root
            else:
                arr.append(root)
            conn(root.left,arr,i+1)
            conn(root.right,arr,i+1)
        conn(root,[],0)
        return root
        
        
        
