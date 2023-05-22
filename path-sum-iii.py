# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        dic = defaultdict(int)
        count = 0

        def dfs(root,summ):
            nonlocal count
            nonlocal targetSum
            if not root:
                return 0

            if summ == targetSum:
                count+=1

            count+=dic[summ-targetSum]

            dic[summ]+=1
            if root.left:
                dfs(root.left,summ+root.left.val)
            if root.right:
                dfs(root.right,summ+root.right.val)

            dic[summ]-=1

        dfs(root,root.val)
        return count