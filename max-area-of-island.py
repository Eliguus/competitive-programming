class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited=set()

        def inside(row,col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        
        def dfs(row,col):
            nonlocal island_count
            for i,j in directions:
                new_col = col+i
                new_row = row+j
                if inside(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]:
                    visited.add((new_row,new_col))
                    dfs(new_row,new_col)
                    island_count+=1

            return

        max_island = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col]:
                    island_count=1
                    visited.add((row,col))
                    dfs(row,col)
                    max_island=max(max_island,island_count)
        return max_island