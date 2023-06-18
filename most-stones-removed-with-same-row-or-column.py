class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dic = {i:i for i in range(len(stones))}
        rank = [0]*len(stones)
        def find(x):
            while x!=dic[x]:
                x=dic[x]
            return x
        
        def union(x,y):
            dx = find(x)
            dy = find(y)

            if dx==dy:
                return False
            if rank[dy] >= rank[dx]:
                dic[dx] = dy
                rank[dy] += rank[dx]
            
            elif rank[dy] < rank[dx]:
                dic[dy] = dx
                rank[dx] += rank[dy]
        def same(r,c):
            return stones[r][0] == stones[c][0] or stones[r][1] == stones[c][1]

        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if same(i,j):
                    union(i,j)
        sames = [find(x) for x in dic.keys()]

        return len(stones) - len(set(sames))