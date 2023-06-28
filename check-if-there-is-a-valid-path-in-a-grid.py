class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def find(x):
            while x!=dic[x]:
                x=dic[x]
            return x

        def union(x,y):
            dx = find(x)
            dy = find(y)

            if dx == dy:
                return
            
            if rank[dx[0]][dx[1]]>rank[dy[0]][dy[1]]:
                dic[dy] = dx
                rank[dx[0]][dx[1]] += rank[dy[0]][dy[1]]
            
            else:
                dic[dx] = dy
                rank[dy[0]][dy[1]] += rank[dx[0]][dx[1]]
            
        
        def inside(x,y):
            return ((0<=x<len(grid)) and (0<=y<len(grid[0])))

        directions = [(0,1),(1,0)]

        right = {1: {1, 3, 5}, 2: {}, 3: {}, 4: {1, 3, 5}, 5: {}, 6: {1, 3, 5}}
        down = {1: {}, 2: {2, 5, 6}, 3: {2, 5, 6}, 4: {2, 5, 6}, 5: {}, 6: {}}
        dic = {}
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dic[(row,col)] = (row,col)

        rank = [[0]*len(grid[0]) for _ in range(len(grid))]


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for x,y in directions:
                    dx = row + x
                    dy = col + y
                    if inside(dx,dy) and grid[dx][dy] in right[grid[row][col]] and dy-col==1:
                        union((dx,dy),(row,col))
                    if inside(dx,dy) and grid[dx][dy] in down[grid[row][col]] and dx-row==1:
                        union((dx,dy),(row,col))
        return find((0,0)) == find((len(grid)-1,len(grid[0])-1))