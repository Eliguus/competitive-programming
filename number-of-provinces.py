class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count=0

        def dfs(num):
            for nums in dic[num]:
                if nums not in visited:
                    visited.add(nums)
                    dfs(nums)
            return
        dic = defaultdict(list)
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col]==1:
                    dic[row+1].append(col+1)
        for i in range(len(isConnected)):
            if i+1 not in visited:
                visited.add(i+1)
                dfs(i+1)
                count+=1
        return count