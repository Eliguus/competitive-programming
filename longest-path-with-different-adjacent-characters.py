class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for i in range(1,len(parent)):
            graph[parent[i]].append(i)
            
        def dfs(val):
            nonlocal path
            longChain = 0
            second = 0

            for child in graph[val]:
                longest = dfs(child)
                if s[val] == s[child]:
                    continue
                
                if longest > longChain:
                    second = longChain
                    longChain = longest
                elif longest>second:
                    second = longest

            path = max(path,longChain+second+1)
            return longChain+1
        path = 1
        dfs(0)
        return path