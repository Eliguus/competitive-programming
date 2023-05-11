class Solution:
    def eventualSafeNodes(self, input: List[List[int]]) -> List[int]:
        indegree = [0]*len(input)
        graph = defaultdict(list)

        for idx, val in enumerate(input):
            for num in val:
                indegree[idx]+=1
                graph[num].append(idx)
        queue = deque()
        for idx,val in enumerate(indegree):
            if not val:
                queue.append(idx)
        ans = []
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            
            for val in graph[node]:
                indegree[val]-=1
                if not indegree[val]:
                    queue.append(val)
        
        return sorted(ans)