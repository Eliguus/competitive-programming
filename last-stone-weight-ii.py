class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        def dp(x,sum1,sum2):
            if x == len(stones):
                return abs(sum1-sum2)
            if (x,sum1,sum2) in memo:
                return memo[(x,sum1,sum2)]
            temp = min(dp(x+1,sum1+stones[x],sum2),dp(x+1,sum1,sum2+stones[x]))
            memo[(x,sum1,sum2)]=temp
            return temp
        
        return dp(0,0,0)