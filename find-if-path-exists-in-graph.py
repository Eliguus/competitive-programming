class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        visited=set()
        def dfs(vertex,visited,destination):
            if vertex==destination:
                return True

            visited.add(vertex)

            for neigh in graph[vertex]:
                if neigh not in visited:
                    
                    found = dfs(neigh,visited,destination)
                    if found:
                        return True
            return False
        return dfs(source,visited,destination)