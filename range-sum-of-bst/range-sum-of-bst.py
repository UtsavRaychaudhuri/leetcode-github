# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def rsumbst(root):
            if root is None:
                return 0
            if root.val<low:
                return rsumbst(root.right)
            if root.val>high:
                return rsumbst(root.left)
            return root.val+rsumbst(root.left)+rsumbst(root.right)
        return rsumbst(root)