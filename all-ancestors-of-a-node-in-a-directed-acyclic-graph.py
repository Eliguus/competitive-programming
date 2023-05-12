class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = [0]*n
        graph = defaultdict(list)

        for n1,n2 in edges:
            graph[n1].append(n2)
            indegree[n2]+=1

        queue = deque()
        for idx,val in enumerate(indegree):
            if not val:
                queue.append(idx)
        ans = [[] for _ in range(n)]
        while queue:
            node = queue.popleft()

            for val in graph[node]:
                indegree[val]-=1
                
                ans[val].append(node)
                for item in ans[node]:
                    if item not in ans[val]:
                        ans[val].append(item)

                if indegree[val]==0:
                    queue.append(val)
        for idx,lists in enumerate(ans):
            ans[idx].sort()
            
        return ans