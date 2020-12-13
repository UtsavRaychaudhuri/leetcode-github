# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pathtop=[]
        self.pathtoq=[]
        res=""
        def pathtonode(root,path,p,q):
            if root is None:
                return
            path.append(root)
            if root==p:
                self.pathtop=path.copy()
            if root==q:
                self.pathtoq=path.copy()
            pathtonode(root.left,path,p,q)
            pathtonode(root.right,path,p,q)
            path.pop()
        pathtonode(root,[],p,q)
        i=0
        while(i<len(self.pathtop) and i<len(self.pathtoq)):
            if self.pathtop[i]==self.pathtoq[i]:
                res=self.pathtop[i]
            else:
                return res
            i+=1
        return res
