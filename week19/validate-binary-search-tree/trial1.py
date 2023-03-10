# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre=-2**32
        def search(root):
            nonlocal pre
            if not root:
                return True
            if not search(root.left):
                return False
            if root.val<=pre:
                return False
            pre=root.val
            return search(root.right)
            
        return search(root)
