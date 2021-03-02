# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.ctr=0
        self.result=None
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.ctr+=1
            if self.ctr==k:
                self.result=root.val
            inorder(root.right)
        inorder(root)
        return self.result