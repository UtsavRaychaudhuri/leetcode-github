"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def conn(root,l,arr):
            if root is None:
                return
            if l==len(arr):
                arr.append(root)
            else:
                arr[l].next=root
                arr[l]=root
            conn(root.left,l+1,arr)
            conn(root.right,l+1,arr)
        conn(root,0,[])
        return root