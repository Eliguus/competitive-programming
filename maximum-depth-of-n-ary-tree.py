"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 1
        if not root:
            return 0
        def dfs(root,count):
            nonlocal ans
            if not root:
                return
            for i in root.children:
                dfs(i,count+1)
                ans = max(ans,count+1)
            return
        dfs(root,1)
        return ans