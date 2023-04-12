# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = ['0']
        count = 0
        def dfs(root):
            nonlocal count
            if not root:
                return
            if not root.left and not root.right: 
                arr.append(str(root.val))
                num = int(''.join(arr))
                count+=num
                print(arr)
                arr.pop()
                
            # if not root.right:
            #     arr.append(str(root.val))
            #     num = int(''.join(arr))
            #     count+=num
            #     print(arr)
            #     arr.pop()
            
            arr.append(str(root.val))
            
            dfs(root.left)
            
            dfs(root.right)
            arr.pop()

        dfs(root)
        return count