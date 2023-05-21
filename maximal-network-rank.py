class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        rank = [0]*n
        graph = defaultdict(set)

        for c1, c2 in roads:
            rank[c1]+=1
            rank[c2]+=1
            graph[c1].add(c2)
            graph[c2].add(c1)
        max_network = 0
        for c1 in range(n):
            for c2 in range(c1+1,n):
                if c2 in graph[c1]:
                    max_network = max(max_network,rank[c1]+rank[c2]-1)
                else:
                    max_network = max(max_network,rank[c1]+rank[c2])
        return max_network