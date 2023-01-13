class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum=0
        for row in range(1,len(grid)-1):
            for col in range(1,len(grid[0])-1):
                temp=grid[row-1][col-1]+grid[row-1][col]+grid[row-1][col+1]+grid[row][col]+grid[row+1][col-1]+grid[row+1][col]+grid[row+1][col+1]
                max_sum=max(max_sum,temp)
        return max_sum
