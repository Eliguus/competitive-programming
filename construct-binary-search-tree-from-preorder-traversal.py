# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        def tree(root,key):
            if not root:
                return TreeNode(key)
            else:
                if root.val<key:
                    root.right = tree(root.right,key)
                else:
                    root.left = tree(root.left,key)
            return root
        
        for i in range(1,len(preorder)):
            tree(root,preorder[i])

        return root