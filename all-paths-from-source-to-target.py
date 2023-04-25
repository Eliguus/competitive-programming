class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []

        def dfs(num):
            if num==len(graph)-1:
                arr.append(num)
                ans.append(arr.copy())
               
                return

            arr.append(num)

            for i in graph[num]:
                 
                dfs(i)
                arr.pop()
                
        for num in graph[0]:
            
            arr=[0]
            dfs(num)
        return ans