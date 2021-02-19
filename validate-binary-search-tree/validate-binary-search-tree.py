# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev=None
        def isvbst(root):
            if root is None:
                return True
            leftflag=isvbst(root.left)
            if self.prev is not None and self.prev>=root.val:
                return False
            else:
                self.prev=root.val
            rightflag=isvbst(root.right)
            return leftflag and rightflag
        return isvbst(root)
        
        