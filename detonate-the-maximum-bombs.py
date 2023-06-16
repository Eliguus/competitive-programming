class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri**2 >= (xi-xj)**2 + (yi-yj)**2:
                    graph[i].append(j)

        def dfs(cur):
            visited.add(cur)
            for nei in graph[cur]:
                if nei not in visited:
                    dfs(nei)
            return len(visited)
        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i))
        return ans