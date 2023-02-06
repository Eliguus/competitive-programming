class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(1,len(grid)-1):
            for col in range(1,len(grid[0])-1):
                col1 = grid[row-1][col-1] + grid[row][col-1] + grid[row+1][col-1]
                col2 = grid[row-1][col] + grid[row][col] + grid[row+1][col]
                col3 = grid[row-1][col+1] + grid[row][col+1] + grid[row+1][col+1]
                row1 = grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1]
                row2 = grid[row][col-1] + grid[row][col] + grid[row][col+1]
                row3 = grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
                diag1 = grid[row-1][col-1] + grid[row][col] + grid[row+1][col+1]
                diag2 = grid[row-1][col+1] + grid[row][col] + grid[row+1][col-1]
                if col3 == row3 == diag2 == col2 == row2 == col1 == row1 == diag1:
                    if set((1,2,3,4,5,6,7,8,9))==set((grid[row-1][col-1],grid[row][col-1],grid[row+1][col-1],grid[row-1][col],grid[row][col],grid[row+1][col],grid[row-1][col+1],grid[row][col+1],grid[row+1][col+1])):
                        count+=1
        
        return count
