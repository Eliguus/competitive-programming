# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def tracking(root):
            if not root:
                return [0,0]

            right = tracking(root.right)
            left = tracking(root.left)

            arr1 = root.val + right[1] + left[1]
            arr2 = max(right)+max(left)

            return [arr1,arr2]
        return max(tracking(root))