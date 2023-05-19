class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(node):
            while graph[node]!=node:
                node=graph[node]

            return node

        def union(x,y):
            dx = find(x)
            dy = find(y)
            if dx==dy:
                return False
            
            if rank[dx]>rank[dy]:
                graph[dy]=dx
            elif rank[dx]<rank[dy]:
                graph[dx]=dy
            else:
                graph[dy]=dx
                rank[dx]+=1
            return True
        graph = {i:i for i in range(1,len(edges)+1)}
        rank = [0]*(len(edges)+1)

        for x,y in edges:
            if not union(x,y):
                return [x,y]
        return -1