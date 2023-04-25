# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return
            if root.val%2==0:
                if root.left:
                    if root.left.right:
                        count+=root.left.right.val
                    if root.left.left:
                        count+=root.left.left.val
                if root.right:
                    if root.right.right:
                        count+=root.right.right.val
                    if root.right.left:
                        count+=root.right.left.val

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return count