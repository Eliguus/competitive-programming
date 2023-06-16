# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total = float('-inf')

        def dfs(root):
            nonlocal total

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            tri = left+right+root.val
            left_sum = left+root.val
            right_sum = right+root.val

            total = max(total,tri,left_sum,right_sum,root.val)
            return max(left_sum,right_sum,root.val)
        dfs(root)

        return total