class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp = [0]*(n+1)
        if n==0:
            return 0
        dp[1] = 1

        for i in range(2,n+1):
            if i%2:
                dp[i] = dp[(i-1)//2] + dp[i//2+1]
            else:
                dp[i]=dp[i//2]
        
        return max(dp)