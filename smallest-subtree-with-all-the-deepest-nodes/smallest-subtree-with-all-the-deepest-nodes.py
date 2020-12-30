# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.hashmap=collections.defaultdict(lambda:-1)
        def populate_depth(root):
            if root is None:
                return -1
            self.hashmap[root]=1+max(populate_depth(root.left),populate_depth(root.right))
            return self.hashmap[root]
        populate_depth(root)
        def dfs(root):
            if self.hashmap[root.left]==self.hashmap[root.right]:
                return root
            if self.hashmap[root.left]>self.hashmap[root.right]:
                return dfs(root.left)
            return dfs(root.right)
        return dfs(root)
            
