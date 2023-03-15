# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic=defaultdict(int)
        def search(root):
            if not root:
                return
            
            dic[root.val]+=1
            search(root.left)
            search(root.right)
            return
        search(root)
        
        arr=[]
        for key,val in dic.items():
            arr.append([val,key])
        
        arr.sort(reverse=True)
        ans=[]
        ptr=1
        
        ans.append(arr[0][1])
        while ptr<len(arr) and arr[0][0]==arr[ptr][0]:
            ans.append(arr[ptr][1])
            ptr+=1
        
        return ans
