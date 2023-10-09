# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        if not root:
            return result
        def tracking(root,curSum,arr):
            if not root:
                return
            if curSum == targetSum and not root.left and not root.right:
                
                result.append(arr)
                return
            if root.left:
                tracking(root.left,curSum+root.left.val,arr+[root.left.val])
            if root.right:
                tracking(root.right,curSum+root.right.val,arr+[root.right.val])
        tracking(root,root.val,[root.val])
        return result