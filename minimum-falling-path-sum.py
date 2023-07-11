class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dic = {}
        def dp(row,col):
            if row>=len(matrix):
                return 0
            left,right= 10**5, 10**5
            if (row,col) in dic:
                return dic[(row,col)]
            if col+1<len(matrix[0]):
                right = dp(row+1,col+1)
            if col-1>=0:
                left = dp(row+1,col-1)
            middle = dp(row+1,col)
            dic[(row,col)] = matrix[row][col]+min(left,right,middle)
            return dic[(row,col)]
            
        ans = 10**5
        for i in range(len(matrix)):
            ans = min(ans,dp(0,i))
        
        return ans