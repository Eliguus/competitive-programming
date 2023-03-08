# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(root1,root2):

            if not root1 and not root2:
                return True

            if (not root1 and root2) or (root1 and not root2):
                return False
            
            if root1.val!=root2.val:
                return False
            return check(root1.left,root2.right) and check(root1.right,root2.left)

        return check(root.left,root.right)
