class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        memo = {}

        def dp(row,col):

            if row>=rows:
                return 0

            if (row,col) not in memo:
                memo[(row,col)] = triangle[row][col]+min(dp(row+1,col),dp(row+1,col+1))
            return memo[(row,col)]
        
        return dp(0,0)