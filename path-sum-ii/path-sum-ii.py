# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.res=[]
        def ps(root,sum,path):
            if root is None:
                return
            if root.left is None and root.right is None and sum+root.val==targetSum:
                path.append(root.val)
                self.res.append(path.copy())
                path.pop()
            path.append(root.val)
            ps(root.left,sum+root.val,path)
            ps(root.right,sum+root.val,path)
            path.pop()
        ps(root,0,[])
        return self.res
        