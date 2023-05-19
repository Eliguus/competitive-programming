class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequality = []
        
        graph = {i:i for i in range(26)}
        rank = [0]*26
        def find(node):
            while graph[node]!=node:
                node=graph[node]
            return node
        def union(x,y):
            dx=find(x)
            dy=find(y)

            if dx==dy:
                return
            if rank[dx]>rank[dy]:
                graph[dy]=dx
            elif rank[dy]>rank[dx]:
                graph[dx]=dy
            else:
                rank[dx]+=1
                graph[dy]=dx
        for items in equations:
            if '!' in items:
                inequality.append(items)
            else:
                union(ord(items[0])-ord('a'),ord(items[3])-ord('a'))
        for items in inequality:
            if find(ord(items[0])-ord('a'))==find(ord(items[3])-ord('a')):
                return False
        return True