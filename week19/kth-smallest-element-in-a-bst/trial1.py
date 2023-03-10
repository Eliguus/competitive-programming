# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def all_nodes(root):
            if not root:
                return arr
            all_nodes(root.left)
            arr.append(root.val)
            all_nodes(root.right)
            return arr
        ans = all_nodes(root)
        ans.sort()
        return ans[k-1]
