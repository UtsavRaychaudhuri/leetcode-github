# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pathtop=[]
        self.pathtoq=[]
        def lca(root,p,q,arr):
            if root is None:
                return
            arr.append(root)
            if root==q:
                self.pathtoq=arr.copy()
            if root==p:
                self.pathtop=arr.copy()
            lca(root.left,p,q,arr)
            lca(root.right,p,q,arr)
            arr.pop()
        lca(root,p,q,[])
        for i in range(min(len(self.pathtop),len(self.pathtoq))):
            if self.pathtop[i]!=self.pathtoq[i]:
                return self.pathtop[i-1]
        return self.pathtop[min(len(self.pathtop),len(self.pathtoq))-1]
            
                       
                