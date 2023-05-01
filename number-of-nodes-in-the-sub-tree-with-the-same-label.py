class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], la: str) -> List[int]:
        graph = defaultdict(list)

        for parent,child in edges:
            graph[parent].append(child)
            graph[child].append(parent)
        ans = [1]*n
        def dfs(node,parent):
            counter = defaultdict(int)
            counter[la[node]] = 1
            for child in graph[node]:
                if child==parent:
                    continue
                childCounter = dfs(child,node)
                for key,val in childCounter.items():
                    counter[key]+=val

            ans[node] = counter[la[node]]
            return counter
        dfs(0,-1)
        return ans