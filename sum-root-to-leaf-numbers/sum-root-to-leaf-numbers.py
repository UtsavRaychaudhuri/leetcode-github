# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res=0
        if root is None:
            return 0
        def sn(root,sumn):
            if root is None:
                return
            if not root.left and not root.right:
                sumn=sumn*10+root.val
                self.res+=sumn
                return
            sn(root.left,sumn*10+root.val)
            sn(root.right,sumn*10+root.val)
        sn(root,0)
        return self.res
