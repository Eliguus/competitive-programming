# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        arr = []
        def dfs(root):
            if not root:
                return 
            
            arr.append(str(root.val))
            if (not root.left and not root.right):
                return
            arr.append('(')

            dfs(root.left)
            arr.append(')')
            if root.right:
                arr.append('(')
                dfs(root.right)
                arr.append(')')
        dfs(root)
        return ''.join(arr)