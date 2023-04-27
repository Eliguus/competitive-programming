# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
       
        ans = []

        queue = deque()
        queue.append(root)
        while queue:
            count = 0
            summ = 0
            newQueue = deque()
            while queue:
                
                node = queue.popleft()
                summ+=node.val
                count+=1
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            queue=newQueue
            ans.append(summ/count)
        return ans