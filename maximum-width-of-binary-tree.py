# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        memo = {}
        maxWid = 0
        def dfs(root,level,pos):
            nonlocal maxWid
            if not root:
                return
            if level not in memo:
                memo[level] = pos
            else:
                maxWid = max(maxWid,pos-memo[level])
            if root.left:
                dfs(root.left,level+1,2*pos)
            if root.right:
                dfs(root.right,level+1,2*pos+1)
        dfs(root,0,0)
        return maxWid+1