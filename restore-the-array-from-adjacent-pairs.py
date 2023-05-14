class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        indegree = defaultdict(int)
        graph = defaultdict(list)

        for parent,child in adjacentPairs:
            indegree[parent]+=1
            indegree[child]+=1
            graph[parent].append(child)
            graph[child].append(parent)

        ans = []
        
        for node, val in indegree.items():
            if val==1 and node in graph:
                start = node
        visited = set()
        def dfs(node):
            ans.append(node)
            visited.add(node)
            if node not in graph:
                return
            
            for vals in graph[node]:
                if vals not in visited:
                    dfs(vals)
        dfs(start)

        return ans