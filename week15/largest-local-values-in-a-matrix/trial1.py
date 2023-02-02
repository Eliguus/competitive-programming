class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        largest_local = []
        for _ in range(len(grid)-2):
            largest_local.append([0]*(len(grid)-2))
        for row in range(1,len(largest_local)+1):
            for col in range(1,len(largest_local)+1):
                largest_local[row-1][col-1] = max( 
                grid[row-1][col-1],grid[row-1][col],grid[row-1][col+1],
                grid[row][col-1],grid[row][col],grid[row][col+1],
                grid[row+1][col-1],grid[row+1][col],grid[row+1][col+1] )
        return largest_local
