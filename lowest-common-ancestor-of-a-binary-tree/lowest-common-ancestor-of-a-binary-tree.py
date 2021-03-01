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
        def pathtonode(root,path):
            if root is None:
                return
            path.append(root)
            if root==p:
                self.pathtop=path.copy()
            if root==q:
                self.pathtoq=path.copy()
            pathtonode(root.left,path)
            pathtonode(root.right,path)
            path.pop()
        pathtonode(root,[])
        for i in range(min(len(self.pathtop),len(self.pathtoq))):
            if self.pathtop[i]!=self.pathtoq[i]:
                return self.pathtop[i-1]
        return self.pathtop[i]
    
            
                
                    
                
        