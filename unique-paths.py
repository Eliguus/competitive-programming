class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        matrix = [[1 if _==0 or i==0 else 0 for _ in range(n)  ] for i in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i][j-1]+matrix[i-1][j]
        return matrix[m-1][n-1]
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