class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        memo = {}
        def dp(row,col):
            if row >= len(grid) or col >= len(grid[0]):
                return 10**6
            if row == len(grid)-1 and col == len(grid[0])-1:
                return max(1,1-grid[row][col])
            if (row,col) in memo:
                return memo[(row,col)]
            pat1 = max(1,dp(row,col+1) - grid[row][col])
            pat2 = max(1,dp(row+1,col) - grid[row][col])

            memo[(row,col)] = min(pat1,pat2)
            return memo[(row,col)]
        return dp(0,0)