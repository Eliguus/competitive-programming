class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] =1
        dp[1] = 1
        for idx in range(2,n+1):
            left = 1

            while left<=idx:
                dp[idx] += dp[left-1] * dp[idx-left]
                left+=1
                
        return dp[n]