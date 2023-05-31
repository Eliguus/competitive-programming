class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        def dp(row,col):
            if row==n-1 and col == m-1:
                return 1
            if row>=n or col>=m:
                return 0
            if (row,col) in memo:
                return memo[(row,col)]
            path1 = dp(row+1,col)
            path2 = dp(row,col+1)
            memo[(row,col)] = path1+path2
            return path1+path2
        return dp(0,0)