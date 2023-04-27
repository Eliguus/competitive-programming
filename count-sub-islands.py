class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def inside(row,col):
            return (0<=row<len(grid1) and 0<=col<len(grid1[0]))
        
        
        def dfs(row,col):
            res = grid1[row][col]==1
            visited.add((row,col))
            for i,j in directions:
                new_row = row+i
                new_col = col+j
                if inside(new_row,new_col) and (new_row,new_col) not in visited and grid2[new_row][new_col]:
                    res = dfs(new_row,new_col) and res
            return res
        counter=0
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if (row,col) not in visited and grid2[row][col]:
                    
                    visited.add((row,col))
                    
                    
                    if dfs(row,col):
                        
                        
                        counter+=1
        return counter