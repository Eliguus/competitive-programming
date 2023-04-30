class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        dic = defaultdict(list)
        for idx,parent in enumerate(edges):
            dic[parent[0]].append(parent[1])
            dic[parent[1]].append(parent[0])
        ans = 0
        def dfs(node,parent):
            total = 0
            child = 0
            for nodes in dic[node]:
                if nodes==parent:
                    continue
                child = dfs(nodes,node)
                if child or hasApple[nodes]:
                    total+=child+2
            return total
        return dfs(0,-1)