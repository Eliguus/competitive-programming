class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        distance = defaultdict(list)        
        for u,v,x in roads:
            graph[u].append(v)
            graph[v].append(u)
            distance[u].append(x)
            distance[v].append(x)
        
        queue = deque()
        queue.append(1)
        mini = 10**4 + 1
        while queue:
            node = queue.popleft()
            visited.add(node)
            mini = min(mini,min(distance[node]))
            for i in graph[node]:
                if i not in visited:
                    queue.append(i)
        
        return mini